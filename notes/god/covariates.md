---
title: Covariate Effects
subject: AI 4 Attribution
short_title: Covariates
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

> **TLDR**: 
> We will incorporate covariates to try and make the data more IID. 
> We will look at covariates such as the spatial coordinates, the temporal coordinates and any related variables of interest. 
> Some variables include temperature and precipitation. 
> We can also explore local and global covariates like “warming”. 
> We will explore simple statistical models like linear functions and then more complex functions like basis functions or perhaps nonlinear functions. 
> We will use Bayesian Hierarchical Models (BHMs) to separate the parameter uncertainty of the process with the hyper-parameters of the process Parameterization. To select the best parameterization, we can use some traditional model selection techniques like AIC or BIC.


## Conditional Models

A second attempt would be to construct a conditionally parameterized distribution.
In this case, we introduce some dependencies on the variable itself.

$$
u \sim p\left(\theta (u)\right)
$$

This changes this function from a generative parametric model to a likelihood model, i.e., a model that generates the parameters wrt some external parameter like time.

In general, most of the distributions that were mentioned above have a mean and standard deviation parameter.
One could easily try to parameterize those parameters with functions that are dependent upon some space and time parameters.
For example, the mean function could be depending upon space, time, and some control vector and likewise the standard deviation.

### Data

For fitting this data, we assume that all elements within the time series are a sequential set of observations

$$
\mathcal{D} = \{ t, u_t\}_{t=1}^{N_t}
$$

where $u\in\mathbb{R}$.


:::{note} Case Study: Temperature Anomaly Tendency & Scale
:class: dropdown

In the paper of [Phillip et al, 2020](https://doi.org/10.5194/ascmo-6-177-2020), they parameterize the mean and scale function using a linear function of the temperature. 
They assume that the mean is some function
They remove the dependency that the temperature is independent and they try to fit a conditional parametric distribution to explain the anomalies on the temperature values which have a dependency on time.
So the variable of interest is temperature and we assume it is iid

$$
\begin{aligned}
\mathcal{D} = \{ T_n \}_{n=1}^{N_t}
\end{aligned}
$$

They assume a conditional likelihood function for temperature and time.

$$
y \sim p(y;\theta(T)) 
$$

They use a GEV distribution for the likelihood function

$$
p(y|\theta;T) = \exp 
\left[ - 
\left[ 1 + \xi \left(\frac{u - \mu(T;\boldsymbol{\theta})}{\sigma(T;\boldsymbol{\theta})}\right) \right]^{-1/\xi}
\right]
$$

The authors try to fit a linear function wrt time and a constant scale parameter.
This is given by the equation

$$
\begin{aligned}
\text{Mean}: && && \mu(T;\theta) &= \mu_0 + \alpha T \\
\text{Scale}: && && \sigma(T;\theta) &= \sigma_0
\end{aligned}
$$

where the parameters of the mean function are $\theta_\mu=\{\mu_0, \alpha\}$ and their are no parameters for the scale function. They showcase another example whereby they try to fit a function for the scale

$$
\begin{aligned}
\text{Mean}: && && \mu(T; \theta) &= \mu_0 \exp\left(\frac{\alpha T}{\mu_0}\right) \\
\text{Scale}: && && \sigma(T; \theta) &= \sigma_0 \exp\left(\frac{\alpha T}{\mu_0}\right)
\end{aligned}
$$

where the parameters of the mean function are $\theta_\mu=\{\mu_0, \alpha\}$ and the parameters of the scale function are $\theta_\sigma=\{\sigma_0, \mu_0, \alpha\}$. 
The origin of this function comes from 

:::

### Conditional Parametric Model

We could also include some conditioning variables, $\boldsymbol{u}$.
The parameters, $\boldsymbol{\theta}$, will be functions of the conditioning variable and some hyperparameters, $\boldsymbol{\alpha}$.

$$
\begin{aligned}
\boldsymbol{y}|\boldsymbol{u} \sim p(\boldsymbol{y}|\boldsymbol{u},\boldsymbol{\theta},\boldsymbol{\alpha})
\end{aligned}
$$

Some ideas for conditioning variables, $\boldsymbol{u}$.

**Standard Variables**

* $\boldsymbol{u}$ - standard variables, e.g., temperature, precipitation, ENSO, etc. $\boldsymbol{\theta_\mu} = \exp \left( \mathbf{W}^\top\mathbf{u} + \mathbf{b}\right)$
* $t$ - temporal coordinate encoding, $\boldsymbol{\theta_\mu}=a\sin(2\pi t/\omega L)$
* $\mathbf{x}$ - spatial coordinates encoding 


#### Temporal Encoding

Here, we assume that the parameters of the data are processes which are parameterized functions of time.


$$
\begin{aligned}
\boldsymbol{\theta} \sim p(\boldsymbol{\theta}|t,\boldsymbol{\alpha})
\end{aligned}
$$

where $t$ is the time and $\boldsymbol{\alpha}$ are the parameters of the distribution.
For example, the Gaussian distribution could have a parameterized mean and scale.
Similarly, the GEVD could have a parameterized mean, scale and shape.
Again, this function can be as simple or as complicated as necessary, e.g., a linear model, a basis function, a non-linear function or a stochastic process.
So, we have a conditional data likelihood term.

$$
\boldsymbol{y}\sim 
p(\boldsymbol{y}|\boldsymbol{\theta},t,\boldsymbol{\alpha})
$$

The posterior is given by

$$
p(\boldsymbol{\theta},\boldsymbol{\alpha}|\boldsymbol{y}) =
\frac{1}{Z}
p(\boldsymbol{y}|\boldsymbol{\theta},t,\boldsymbol{\alpha})
p(\boldsymbol{\theta}|t,\boldsymbol{\alpha})
p(\boldsymbol{\alpha})
$$

This is known as a Bayesian Hierarchical Model (BHM) because we have hierarchical processes and priors which condition the data likelihood.

***

*** 

#### Spatial Encoding

$$
\begin{aligned}
\boldsymbol{\theta} \sim p(\boldsymbol{\theta}|\mathbf{x},\boldsymbol{\alpha})
\end{aligned}
$$

where $t$ is the time and $\boldsymbol{\alpha}$ are the parameters of the distribution.
For example, the Gaussian distribution could have a parameterized mean and scale.
Similarly, the GEVD could have a parameterized mean, scale and shape.
Again, this function can be as simple or as complicated as necessary, e.g., a linear model, a basis function, a non-linear function or a stochastic process.
So, we have a conditional data likelihood term.

$$
\boldsymbol{y}\sim 
p(\boldsymbol{y}|\boldsymbol{\theta},\mathbf{x},\boldsymbol{\alpha})
$$

The posterior is given by

$$
p(\boldsymbol{\theta},\boldsymbol{\alpha}|\boldsymbol{y}) =
\frac{1}{Z}
p(\boldsymbol{y}|\boldsymbol{\theta},\mathbf{x},\boldsymbol{\alpha})
p(\boldsymbol{\theta}|\mathbf{x},\boldsymbol{\alpha})
p(\boldsymbol{\alpha})
$$

This is also a BHM because we have hierarchical processes and priors which condition the data likelihood.



## Inference

We can use the standard posterior distribution to best fit the parameters of the distribution given the data.

$$
p(\theta|\mathcal{D}) = \frac{1}{Z}p(\mathcal{D}|\theta)p(\theta)
$$

Here, we have many examples of different inference methods to use. 
For example, we can use simple methods like Maximum Likelihood Estimation (MLE) or Maximum-A-Posterior (MAP). 
We can use approximate inference methods like Laplace or Variational Inference (VI).
We could even use sampling methods like Markov Chain Monte-Carlo (MCMC).


## Literature Review

::: {seealso} Applications
:class: dropdown

**Temperature** - [Phillip et al, 2020](https://doi.org/10.5194/ascmo-6-177-2020)
***
**Wave Height** - [Wang et al, 2004](https://doi.org/10.1175/1520-0442(2004)017<2368:NAOWCC>2.0.CO;2) | [Sartini et al, 2015](https://doi.org/10.1002/2015JC011061)
***
**Ocean Environments** - [Jonathan & Ewans, 2013](https://doi.org/10.1016/j.oceaneng.2013.01.004)

:::