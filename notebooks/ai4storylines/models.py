from dataclasses import dataclass
from typing import Callable, Dict
from functools import partial
import jax
import jax.numpy as jnp
import jax.random as jrandom
from jaxtyping import Float, Array
import numpyro
import numpyro.distributions as dist
from numpyro.infer import Predictive


# @dataclass
# class ModelPredictorMCMC:
#     model: Callable
#     posterior_params: Dict
#     num_spatial: int

#     def predict(self, x: Float[Array, "M D"], rng_key=jrandom.PRNGKey(0), *args, **kwargs) -> Float[Array, "P M N"]:
#         predict_fn = Predictive(self.model, posterior_samples=self.posterior_params, parallel=True, *args, **kwargs)
#         return predict_fn(rng_key, x=x, num_spatial=self.num_spatial)["obs"]

#     def gradient(self, x: Float[Array, "N D"], rng_key=jrandom.PRNGKey(0), *args, **kwargs) -> Float[Array, "P N M D"]:
#         fn = partial(self.predict, rng_key=rng_key, *args, **kwargs)
#         gradient_fn = jax.jacfwd(self.predict)
#         out = gradient_fn(x)[:, 0, ...]
#         return out

#     def gradient_batch(self, x: Float[Array, "N D"], rng_key=jrandom.PRNGKey(0), *args, **kwargs) -> Float[Array, "P N M D"]:
#         raise NotImplemented

@dataclass
class ModelPredictorMCMC:
    model: Callable
    posterior_params: Dict

    def predict(self, x: Float[Array, "M D"], rng_key=jrandom.PRNGKey(0), *args, **kwargs) -> Float[Array, "P M N"]:
        predict_fn = Predictive(self.model, posterior_samples=self.posterior_params, parallel=True, *args, **kwargs)
        return predict_fn(rng_key, x=x)["obs"]

    def gradient(self, x: Float[Array, "N D"], rng_key=jrandom.PRNGKey(0), *args, **kwargs) -> Float[Array, "P N M D"]:
        fn = partial(self.predict, rng_key=rng_key, *args, **kwargs)
        gradient_fn = jax.jacfwd(self.predict)
        out = gradient_fn(x)[:, 0, ...]
        return out

    def gradient_batch(self, x: Float[Array, "N D"], rng_key=jrandom.PRNGKey(0), *args, **kwargs) -> Float[Array, "P N M D"]:
        raise NotImplemented


@dataclass
class LinearRegression:
    num_spatial: int

    def model(self, x: Float[Array, "M D"], y: Float[Array, "M N"]=None):
        if len(x.shape) != 2:
            x = x[None,:]
        num_models, num_covariates = x.shape
        
        # location: (MxD)
        loc = numpyro.param("loc", init_value=jnp.ones((self.num_spatial, num_covariates)))
        # bias
        bias = numpyro.param("bias", init_value=jnp.ones((self.num_spatial,)))
        # location: ()
        scale = numpyro.param("scale", init_value=2.0, constraints=dist.constraints.greater_than(0.0))

        with numpyro.plate("models", num_models):
            
            z = jnp.einsum("ND,MD->MN",loc,x) + bias
            numpyro.sample("obs", dist.Normal(z, scale).to_event(1), obs=y)

@dataclass
class BayesianLinearRegression:
    num_spatial: int

    def model(self, x: Float[Array, "M D"], y: Float[Array, "M N"]=None):
        if len(x.shape) != 2:
            x = x[None,:]
        num_models, num_covariates = x.shape
        
        # location: (MxD)
        loc = numpyro.sample("loc", dist.Normal(0.0, 10.0), sample_shape=(self.num_spatial, num_covariates))
        # bias
        bias = numpyro.sample("bias", dist.Normal(0.0, 10.0), sample_shape=(self.num_spatial,))
        # location: ()
        scale = numpyro.sample("scale", dist.LogNormal(0.0, 10.0))

        with numpyro.plate("models", num_models):
            
            z = jnp.einsum("ND,MD->MN",loc,x) + bias
        
        numpyro.sample("obs", dist.Normal(z, scale), obs=y)


@dataclass
class BayesianHierachicalRegression:
    num_spatial: int

    def model(self, x: Float[Array, "M D"], y: Float[Array, "M N"]=None):
        if len(x.shape) != 2:
            x = x[None,:]
        num_models, num_covariates = x.shape
        # noise
        scale = numpyro.sample("scale", dist.HalfCauchy(10.0))
        z_scale_mu = numpyro.sample("z_scale_mean", dist.Normal(0.0, 10.0))
        z_scale_scale = numpyro.sample("z_scale_scale", dist.HalfCauchy(10.0))
        # priors on mean
        loc_prior_mean = numpyro.sample("loc_prior_mean", dist.Normal(0.0, 10.))
        loc_prior_scale = numpyro.sample("loc_prior_scale", dist.HalfCauchy(10.0))
        # priors on bias
        bias_prior_mean = numpyro.sample("bias_prior_mean", dist.Normal(0.0, 10.))
        bias_prior_scale = numpyro.sample("bias_prior_scale", dist.HalfCauchy(10.0))
        # spatial locations
        with numpyro.plate("spatial", self.num_spatial):
            # sample from bias (N,)
            bias: Float[Array, "N"]  = numpyro.sample("bias", dist.Normal(bias_prior_mean, bias_prior_scale))
            # same noise
            z_scale: Float[Array, "N"] = numpyro.sample("z_scale", dist.LogNormal(z_scale_mu, z_scale_scale))
        with numpyro.plate("covariates", num_covariates), numpyro.plate("spatial", self.num_spatial):
            # sample weights, (N,D)
            weight: Float[Array, "N D"] = numpyro.sample("weight", dist.Normal(loc_prior_mean, loc_prior_scale))
            # conditional latent variable, (M,N)
            z: Float[Array, "M N"] = jnp.einsum("ND,MD->MN",weight, x) + bias + z_scale
            
        # Data Likelihood
        numpyro.sample("obs", dist.Normal(z, scale), obs=y)



def sqeuclidean_distance(x: jnp.array, y: jnp.array) -> float:
    return jnp.sum((x - y) ** 2)

def kernel_rbf(x: jnp.array, y: jnp.array, length_scale=1.0, variance=1.0) -> float:
    return variance * jnp.exp(- sqeuclidean_distance(x/length_scale, y/length_scale))

def gram(kernel_fn, x: jnp.array, y: jnp.array, *args, **kwargs) -> float:
    return jax.vmap(lambda x1: jax.vmap(lambda y1: kernel_fn(x1, y1, *args, **kwargs))(y))(x)


def model_bhm_gp(num_spatial: int, x: Float[Array, "M D"], S: Float[Array, "N"], y: Float[Array, "M N"]=None):
    num_models, num_features = x.shape
    num_spatial = S.shape[0]
    # noise
    scale = numpyro.sample("scale", dist.LogNormal(0.0, 10.0))
    z_scale_mu = numpyro.sample("z_scale_mean", dist.LogNormal(0.0, 10.0))
    z_scale_scale = numpyro.sample("z_scale_scale", dist.LogNormal(0.0, 10.0))
    # priors on mean
    loc_prior_mean = numpyro.sample("loc_prior_mean", dist.Normal(0.0, 10.))
    loc_prior_scale = numpyro.sample("loc_prior_scale", dist.LogNormal(0.0, 10.))
    # priors on bias
    bias_prior_mean = numpyro.sample("bias_prior_mean", dist.Normal(0.0, 10.))
    bias_prior_scale = numpyro.sample("bias_prior_scale", dist.LogNormal(0.0, 10.))
    # prior on spatial process
    variance = numpyro.sample("variance", dist.LogNormal(0.0, 10.0))
    length_scale = numpyro.sample("length_scale", dist.LogNormal(0.0, 10.0))
    K: Float[Array, "N N"] = gram(kernel_rbf, S, S, length_scale=length_scale, variance=variance) 
    K += 1e-6 * jnp.eye(K.shape[0])

    # weights & biases
    with numpyro.plate("spatial", num_spatial), numpyro.plate("covariates", num_features):
        # sample weights, (N,D)
        weight: Float[Array, "N D"] = numpyro.sample("weight", dist.Normal(loc_prior_mean, loc_prior_scale))

    with numpyro.plate("spatial", num_spatial):
        # sample bias
        bias: Float[Array, "N"]  = numpyro.sample("bias", dist.Normal(bias_prior_mean, bias_prior_scale))
        # same noise
        z_scale: Float[Array, "N"] = numpyro.sample("z_scale", dist.LogNormal(z_scale_mu, z_scale_scale))
        
    # sample spatial process
    f: Float[Array, "M"] = numpyro.sample("f", dist.MultivariateNormal(loc=jnp.zeros(S.shape[0]), covariance_matrix=K))

    # conditional latent variable, (M,N)
    z: Float[Array, "M N"] = jnp.einsum("DN,MD->MN",weight, x) + f + bias + z_scale

    # data likelihood
    numpyro.sample("obs", dist.Normal(z, scale), obs=y)


def model_gp(x: Float[Array, "M D"], S: Float[Array, "N"], y: Float[Array, "M N"]=None):
    num_models, num_features = x.shape
    num_spatial = S.shape[0]
    # noise
    scale = numpyro.sample("scale", dist.HalfCauchy(scale=10))
    # prior on spatial process
    variance = numpyro.sample("variance", dist.HalfNormal(5.0))
    length_scale = numpyro.sample("length_scale", dist.HalfNormal(5.0))
    K: Float[Array, "N N"] = gram(kernel_rbf, S, S, length_scale=length_scale, variance=variance) 
    K += (scale + 1e-6) * jnp.eye(K.shape[0])

    # weights & biases
    with numpyro.plate("spatial", num_spatial), numpyro.plate("covariates", num_features):
        # sample weights, (N,D)
        weight: Float[Array, "N D"] = numpyro.sample("weight", dist.Normal(0.0, 10.))

    with numpyro.plate("spatial", num_spatial):
        # sample bias
        bias: Float[Array, "N"]  = numpyro.sample("bias", dist.Normal(0.0, 10.))
    
    
    with numpyro.plate("model", num_models):
        # sample spatial process
        z: Float[Array, "M N"] = numpyro.deterministic("z", jnp.einsum("DN,MD->MN",weight, x) +  bias)
        f: Float[Array, "M"] = numpyro.sample(
            "obs", 
            dist.MultivariateNormal(loc=z, covariance_matrix=K), 
            obs=y
        )

def gp_mean(
    s: Float[Array, "N 2"], 
    x: Float[Array, "D"], 
    weight_x: Float[Array, "N D"], 
    weight_s: Float[Array, "2"], 
    bias: Float[Array, ""]):
    return jnp.einsum("D,ND->N", weight_s, s) + jnp.einsum("ND,D->N",weight_x, x) + bias

def model_gp_v2(x: Float[Array, "M D"], S: Float[Array, "N"], y: Float[Array, "M N"]=None):
    num_models, num_features = x.shape
    num_spatial = S.shape[0]
    # noise
    scale = numpyro.sample("scale", dist.HalfCauchy(scale=10))
    # prior on spatial process
    variance = numpyro.sample("variance", dist.LogNormal(0.0, 10.0))
    length_scale = numpyro.sample("length_scale", dist.LogNormal(0.0, 10.0))
    K: Float[Array, "N N"] = gram(kernel_rbf, S, S, length_scale=length_scale, variance=variance) 
    K += (scale + 1e-6) * jnp.eye(K.shape[0])

    weight_s: Float[Array, "N D"] = numpyro.sample("weight_s", dist.Normal(0.0, 2.0), sample_shape=(2,))

    # weights & biases
    with numpyro.plate("spatial", num_spatial), numpyro.plate("covariates", num_features):
        # sample weights, (N,D)
        weight: Float[Array, "N D"] = numpyro.sample("weight", dist.Normal(0.0, 10.))

    with numpyro.plate("spatial", num_spatial):
        # sample bias
        bias: Float[Array, "N"]  = numpyro.sample("bias", dist.Normal(0.0, 10.))
    
    # z: Float[Array, "M N"] = jnp.einsum("DN,MD->MN",weight, x) +  bias
    z = jax.vmap(gp_mean, in_axes=(None,0,None,None,None))(S, x, weight.T, weight_s, bias)
    # sample spatial process
    f: Float[Array, "M"] = numpyro.sample(
        "obs", 
        dist.MultivariateNormal(loc=z, covariance_matrix=K), 
        obs=y
    )


    # z: Float[Array, "M N"] = jnp.einsum("DN,MD->MN",weight, x) +  bias
    # # sample spatial process
    # f: Float[Array, "M"] = numpyro.sample(
    #     "obs", 
    #     dist.MultivariateNormal(loc=z, covariance_matrix=K), 
    #     obs=y
    # )
    