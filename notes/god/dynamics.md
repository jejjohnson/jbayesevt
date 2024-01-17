---
title: Dynamical Effects
subject: AI 4 Attribution
short_title: Dynamics
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
> We will make the transition from coordinate-based models to field-based models by way of state space models (SSM). 
> To start, we can examine some simple structural time series methods (STS) where we can manually fit the periodicity and covariates. 
> We can also use an entire family of Bayesian filtering methods like KF, EKF, UKF and ADF. 
> These methods will have more advanced inference methods like approximate Gaussian assumptions and Variational methods. 
> We’re also free to include other sampling methods like MCMC, ensemble methods and particle filters for inference. To deal with scalability issues, we can use convolutions for the spatial Parameterizations and simple time steppers like Euler. We can also include ODEs/PDEs to include more physics within the spatial operators. 
> In addition, we can include more traditional numerical time steppers for more stable rollouts (Autoregressive applications).




### State Space Model

Here, we assume that there is a latent variable, $\boldsymbol{z}$, which is described by a dynamical system.
We also have an optional control variable, $\boldsymbol{u}$, which could be influencing the hidden state.

$$
\begin{aligned}
\text{Initial Distribution}: && && \boldsymbol{z}_0 &\sim p(\boldsymbol{z}_0|\mathbf{\mu}_{z_0}, \mathbf{\Sigma}_{z_0})\\
\text{Transition Distribution}: && && \boldsymbol{z}_t &\sim p(\boldsymbol{z}_t|\boldsymbol{z}_{t-1},\boldsymbol{\alpha}_z) \\
\text{Emission Distribution}: && && \boldsymbol{\theta}_t &\sim p(\boldsymbol{\theta}_t|\boldsymbol{z}_t,\boldsymbol{\alpha}_\theta) \\
\text{Data Likelihood}: && && \boldsymbol{y}_t &\sim p(\boldsymbol{y}_t|\boldsymbol{\theta}_t)
\end{aligned}
$$

where $\boldsymbol{T_\theta}$ is the transition function for the latent variable, $\boldsymbol{z}_t$, and $\boldsymbol{h_\theta}$ is the emission function.
We are free to make these functions as complex as we see fit.
For example, we could have simple linear functions or more complex non-linear functions.
**Note**: these methods have many names including: statistical data assimilation, statistical inverse problem, (dynamical) latent variables, Bayesian filtering methods (Kalman, Particle), Bayesian hierarchical models, and mixed effects models.


### Conditional Dynamical Models

$$
y_t \sim p\left(y|t;\theta\right)
$$


:::{note} Case Study I: Temperature Tendency  & Scale
:class: dropdown

In the paper of [Phillip et al, 2020](https://doi.org/10.5194/ascmo-6-177-2020), they parameterize the mean and scale function using the temperature wrt time. 
They remove the dependency that the temperature is independent and they try to fit a conditional parametric distribution to explain the anomalies on the temperature values which have a dependency on time.
So the variable of interest is temperature which varies wrt time.

