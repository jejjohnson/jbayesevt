---
title: Software
subject: AI 4 Attribution
short_title: Software
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
abbreviations:
    ERA5: ECMWF Reanalysis Version 5
    CMIP6: Coupled Model Intercomparison Project Phase 6
    AMIP6: Atmospherical Model Intercomparison Project Phase 6
    PDEs: Partial Differential Equations
    RHS: Right Hand Side
    TLDR: Too Long Did Not Read
    SSP: Shared Socioeconomic Pathways
    CDS: Climate Data Store
---



## PPL

[Numpyro](https://num.pyro.ai/en/stable/index.html) | [Github](https://github.com/pyro-ppl/numpyro)


***

### Example: Bayesian Regression



**Build a Model**

```python
def model(u: Array, y: Optional[Array]=None):
    # sample parameters
    bias = numpyro.sample("b", dist.Normal(0.0, 0.2))
    weight = numpyro.sample("w", dist.Normal(0.0, 0.5))
    sigma = numpyro.sample("sigma", dist.Exponential(1.0))
    # calculate formula
    mu = weight * u + bias
    # data likelihood
    numpyro.sample("obs", dist.normal(mu, sigma), obs=y)
```

**Prior Predictive Distribution**

```python
prior_predictive = Predictive(model, num_sample=100)
prior
```

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