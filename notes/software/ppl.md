---
title: PPLs
subject: AI 4 Attribution
short_title: PPL
authors:
  - name: J. Emmanuel Johnson
    affiliations:
      - CSIC
      - UCM
      - IGEO
    orcid: 0000-0002-6739-0053
    email: juanjohn@ucm.es
license: CC-BY-4.0
keywords: simulations
---



## PPL

[Numpyro](https://num.pyro.ai/en/stable/index.html) | [Github](https://github.com/pyro-ppl/numpyro)


***

### Example: Bayesian Regression



#### Model

The first step, we need to build a model

$$
p(\mathcal{D},\boldsymbol{\theta})=p(y|x,\boldsymbol{\theta})p(\boldsymbol{\theta})
$$

In this joint distribution, we have a likelihood and a prior.
The likelihood is given by a Gaussian

$$
p(y|x,\boldsymbol{\theta})=\mathcal{N}(y|wx+b,\sigma^2)
$$

We also have the parameters given by

$$
\boldsymbol{\theta} = \{w,b,\sigma\}
$$

so we need prior distributions on these as well.

```python
def model(x: Array, y: Optional[Array]=None):
    # sample parameters
    bias = numpyro.sample("b", dist.Normal(0.0, 0.2))
    weight = numpyro.sample("w", dist.Normal(0.0, 0.5))
    sigma = numpyro.sample("sigma", dist.Exponential(1.0))
    # calculate formula
    mu = weight * x + bias
    # data likelihood
    numpyro.sample("obs", dist.normal(mu, sigma), obs=y)
```

**Prior Predictive Distribution**

$$
p(y^*)=\int p(y^*,\boldsymbol{\theta})d\boldsymbol{\theta}=
\int p(y^*|\boldsymbol{\theta})p(\boldsymbol{\theta})d\boldsymbol{\theta}
$$

So from a more practical perspective, this works by

$$
\begin{aligned}
p(y^*) &\approx \frac{1}{N}\sum_{n=1}^Np(y_n|\boldsymbol{\theta}_n) && &&
\boldsymbol{\theta}_n \sim p(\boldsymbol{\theta}) && &&
n = 1,2,\ldots,N
\end{aligned}
$$

```python
prior_predictive = Predictive(model, num_sample=100)
prior
```

***
## Inference

***
### Example: MCMC

**Perform Inference**

```python
kernel = NUTS(model)
num_samples = 2_000
mcmc = MCMC(kernel, num_warmup=1_000, num_samples=num_samples)
mcmc.run(key, u=u, y=y)
mcmc.print_summary()
samples = mcmc.get_samples()
```


**Posterior Distribution over Regression Parameters**

```python
posterior_mu = samples["weight"] * u + samples["bias"]
mean_ = jnp.mean(posterior_mu, axis=0)
hpdi_mu = hpdi(posterior_mu, quantile=0.90)
```


**Predictive Posterior Distribution**

```python
prior_predictive = Predictive(model, num_sample=100)
prior
```

***
### Example: MLE

*** 
### Example: MAP

```python
```

***

### Example: Variational Inference


**Prior**

$$
\begin{aligned}
\text{Prior}: && &&
\theta &\sim p(\theta) \\
\text{Data Likelihood}: && &&
y &\sim p(y|\theta)
\end{aligned}
$$

```python
def model(data):
    f = numpyro.sample("latent_fairness", dist.Beta(10, 10))
    with numpyro.plate("N", data.shape[0] if data is not None else 10):
        numpyro.sample("obs", dist.Bernoulli(f), obs=data)
```


**Variational Posterior**

$$
q \sim q(\mu, \sigma)
$$

```python
def guide(data):
    alpha_q = numpyro.param("alpha_q", 15., constraint=constraints.positive)
    beta_q = numpyro.param("beta_q", lambda rng_key: random.exponential(rng_key),
                           constraint=constraints.positive)
    numpyro.sample("latent_fairness", dist.Beta(alpha_q, beta_q))
```


**Inference**

$$
\boldsymbol{\phi}^* = \underset{\boldsymbol{\phi}}{\text{argmin}} \hspace{2mm} \text{ELBO}(\boldsymbol{\phi};y)
$$

```python
optimizer = numpyro.optim.Adam(step_size=5e-5)
svi = SVI(model, guide, optimizer, loss=Trace_ELBO())
svi_result = svi.run(random.PRNGKey(0), 2000, data)
params = svi_result.params
```

**Best Parameters**






**Approximate Posterior**


```python
# use guide to make predictive
predictive = Predictive(model, guide=guide, params=params, num_samples=1000)
samples = predictive(random.PRNGKey(1), data=None)
```

**Posterior Samples**

```python
predictive = Predictive(guide, params=params, num_samples=1000)
posterior_samples = predictive(random.PRNGKey(1), data=None)
```

**Posterior Predictive Samples**

```python
# use posterior samples to make predictive
predictive = Predictive(model, posterior_samples, params=params, num_samples=1000)
samples = predictive(random.PRNGKey(1), data=None)
```
