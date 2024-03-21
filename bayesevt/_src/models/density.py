from dataclasses import dataclass
import equinox as eqx
from jaxtyping import Float, Array
import numpyro
import numpyro.distributions as dist
from tensorflow_probability.substrates.jax import distributions as tfd


class DeterministicGEVD(eqx.Module):
    init_loc: Array
    init_scale: Array
    init_shape: Array

    def model(self, y: Float[Array, "N"]=None):
        # prior parameters
        loc = numpyro.param("loc", init_value=self.init_loc)
        scale = numpyro.param("scale", init_value=self.init_scale, constraints=dist.constraints.greater_than(0.0))
        concentration = numpyro.param("concentration", init_value=self.init_shape, constraints=dist.constraints.greater_than(0.0))
        # likelihood
        numpyro.sample("obs", tfd.GeneralizedExtremeValue(loc, scale, concentration), obs=y)

    def guide(self, y: Float[Array, "N"]=None):
        pass


class ProbabilisticGEVD(eqx.Module):
    loc_dist = dist.Normal(loc=30.0, scale=10.0)
    scale_dist = dist.LogNormal(loc=0.0, scale=10.0)
    shape_dist = dist.LogNormal(loc=0.0, scale=2.0)

    def model(self, y: Float[Array, "N"]=None):
        # prior parameters
        loc = numpyro.sample("loc", self.loc_dist)
        scale = numpyro.sample("scale", self.scale_dist)
        concentration = numpyro.sample("concentration", self.shape_dist)
        
        # likelihood
        numpyro.sample("obs", tfd.GeneralizedExtremeValue(loc, scale, concentration), obs=y)


class DeterministicGPD(eqx.Module):
    init_loc: Array
    init_scale: Array
    init_shape: Array

    def model(self, y: Float[Array, "N"]=None):
        # prior parameters
        loc = numpyro.param("loc", init_value=10.0)
        scale = numpyro.param("scale", init_value=10.0)
        concentration = numpyro.param("shape", init_value=2.0)
        # likelihood
        numpyro.sample("obs", tfd.GeneralizedPareto(loc, scale, concentration), obs=y)



