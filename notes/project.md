---
title: Project Proposal
subject: AI 4 Attribution
short_title: Proposed Solutions
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
    GEVD: Generalized Extreme Value Distribution
    GPD: Generalized Pareto Distribution
    PPL: Probabilistic Programming Language
    MLE: Maximum Likelihood Expectation
    MAP: Maximum A Posteriori
    MCMC: Markov Chain Monte Carlo
    HMC: Hamiltonian Monte Carlo
---


## Project Goals

> My primary focus is on improving the modeling capabilities using modern data-driven methodologies.
> Most of the current work do manual feature extraction and reduce their statistical models to simple ones.
> I want to take a more data-driven approach whereby we encode as many different prior knowledge as possible into the model itself, and then use modern inference procedures to find the best parameters.
> To deal with the small number of samples, we'll adopt more Bayesian inference methods, e.g., MCMC and for the larger number of samples, we'll adopt more approximate Bayesian inference methods, e.g., variational inference.

**Application to Attribution**.
For each of the proposed methods, we can train two models on two scenarios: one with anthropogenic effects and one without.

***

### Safe Goal

> Reimplement the methods proposed in [Philip et al, 2020](https://doi.org/10.5194/ascmo-6-177-2020) where they fitted GEVD and GPD on temperature and precipitation data.
> Instead, we will use more advanced methods for Bayesian inference to improve the parameter uncertainty quantification. We will demonstrate the ease and speed of use using modern PPLs.


**What's Been Done**. 
The original paper showcased different parametric models of extreme values of temperature and precipitation.
The authors explored different ways of implementing process parameterizations.
For example, the authors explored process parameterizations which take a linear or exponential forms.
They also explored covariates like time and/or temperature.


$$
\begin{aligned}
\text{Data Likelihood}: && &&
\boldsymbol{y} &\sim p(\boldsymbol{y}|\boldsymbol{u},\boldsymbol{\theta},\boldsymbol{\alpha})\\
\text{Parameterization}: && && 
\boldsymbol{\theta} &\sim p(\boldsymbol{\theta}|\boldsymbol{u},\boldsymbol{\alpha})\\
\text{Prior Process Hyperparameters}: && &&
\boldsymbol{\alpha} &\sim p(\boldsymbol{\alpha})
\end{aligned}
$$

**What's Lacking**.
They do not focus on the inference methods that can be used to find the parameters.
As far as I see, there is no uncertainty quantification in the parameters.


**Proposed Improvement**. 
We can add some Bayesian inference methods on these parametric models.
We can use alternative inference methods like MCMC or approximate variational inference.
This will give users more uncertainty quantification of the parameters found.
We will use modern PPLs which will give users speed and reasonable scalability.
They also implement a number of standard inference routines that should work out of the box.
Some examples include MLE, MAP, Laplace Approximation, Variational Inference ([Wingate & Weber, 2013](https://doi.org/10.48550/arXiv.1301.1299), [Ranganath et al, 2013](https://doi.org/10.48550/arXiv.1401.0118)), MCMC, and HMC.
We will also uphold strict reproducibility standards so that the broader community can engage in further developments of modeling extreme values using modern ML-inspired tools.

***

### Stretch Goal

> Reimplement the methods proposed in ([Garcia et al, 2023](https://doi.org/10.1007/s00382-022-06638-x), [Chen et al, 2022](https://doi.org/10.48550/arXiv.2110.07051), [Mahmoudian & Mahammadzadeh, 2014](https://doi.org/10.1007/s10687-014-0180-2), ).

**What's Been Done**.
These papers are an excellent introduction to incorporating spatial considerations when modeling extremes.
The parameterization of the GEVD/GPD is decomposed into a covariate process and a spatial process.
In general, these papers adopt a 
In general, these papers adopt a non-parametric approach to modeling the spatial processes parameters


This is the method used in ([Garcia et al, 2023](https://doi.org/10.1007/s00382-022-06638-x), [Chen et al, 2022](https://doi.org/10.48550/arXiv.2110.07051)).

$$
\begin{aligned}
\text{Data Likelihood}: && &&
\boldsymbol{y} &\sim p(\boldsymbol{y}|\boldsymbol{\theta},\boldsymbol{w},\mathbf{x},t,\boldsymbol{\phi},\boldsymbol{\alpha}) \\
\text{Parameterization}: && && 
\boldsymbol{\theta} &\sim p(\boldsymbol{\theta}|\boldsymbol{w},\mathbf{x},t,\boldsymbol{\phi},\boldsymbol{\alpha})\\
\text{Spatial Process}: && &&
\boldsymbol{w}_n(\mathbf{x},t) &\sim \mathcal{GP}_n
\left(\boldsymbol{\mu_\alpha}(\mathbf{x},t), \boldsymbol{k_\alpha}([\mathbf{x},t],[\mathbf{x}',t'])\right) \\
\text{Spatial Process Prior Hyperparameters}: && &&
\boldsymbol{\alpha} &\sim p(\boldsymbol{\alpha}) \\
\text{Parameterization Prior Hyperparameters}: && &&
\boldsymbol{\phi} &\sim p(\boldsymbol{\phi}) 
\end{aligned}
$$



**Proposed Improvements**.
We can reimplement some of the methods shown by the above papers including some of the speed-ups introduced.
We can also utilize some simpler methods which make use of parametric methods instead of the (potentially) expensive GP model.


***

### Bold Goal

> Reimplement the methods proposed in [ [Mahmoudian & Mahammadzadeh, 2014](https://doi.org/10.1007/s10687-014-0180-2), [Heurta & Sanso, 2007](https://doi.org/10.1007/s10651-007-0014-3)].
> These methods focus on using state space models as parameterizations of the GEVD and/or GPD.


**What's Been Done**.
These papers are an excellent introduction to incorporating time dynamics when considering modeling extremes. 
In particular, ([Mahmoudian & Mahammadzadeh, 2014](https://doi.org/10.1007/s10687-014-0180-2)) provide an excellent demonstration whereby they showcase how one could model a spatial field as independent entities.
This corresponds to the methods proposed within the **stretch goal** that are outlined above.
Then, they subsequently show how one could model it as a Bayesian linear dynamical system.

In general, both papers make use of a process parameterization which is governed by a Gaussian process.
However, the mean is time dependent which is governed by a latent dynamical model.
Admittedly, this method starts to get very confusing very quickly because there are hierarchical processes everywhere.


::::{tab-set}
:::{tab-item} Parametric Method
:sync: tab1

This is the method used in ([Heurta & Sanso, 2007](https://doi.org/10.1007/s10651-007-0014-3)).

$$
\begin{aligned}
\text{Observation Likelihood}: && &&
\boldsymbol{y}_t &\sim p(\boldsymbol{y}_t|\boldsymbol{\theta}_t,\boldsymbol{\alpha}_t) \\
\text{Parameterization}: && && 
\boldsymbol{\theta}_t &\sim p(\boldsymbol{\theta}_t|\boldsymbol{z}_t,\boldsymbol{\alpha}_t)\\
\text{Latent Dynamics}: && && 
\boldsymbol{z}_t &\sim p(\boldsymbol{z}_{t-1}|\boldsymbol{\alpha}_t)\\
\text{Latent Dynamics Hyper-Parameters}: && &&
\boldsymbol{\alpha}_t &\sim p(\boldsymbol{\alpha}_t)
\end{aligned}
$$

:::
:::{tab-item} Semi-Parametric
:sync: tab2

This is the method used in ([Mahmoudian & Mahammadzadeh, 2014](https://doi.org/10.1007/s10687-014-0180-2)).

$$
\begin{aligned}
\text{Observation Likelihood}: && &&
\boldsymbol{y}_t &\sim p(\boldsymbol{y}_t|\boldsymbol{\theta}_t,\boldsymbol{\alpha}_t) \\
\text{Parameterization Process}: && &&
\boldsymbol{\theta}_t &\sim 
\mathcal{GP}(\boldsymbol{\theta}_t|\boldsymbol{\mu}_t(\mathbf{x};\boldsymbol{\alpha}_t),
\boldsymbol{k}(\mathbf{x},\mathbf{x}';\boldsymbol{\phi})) \\
\text{Parameterization Mean Model}: && && 
\boldsymbol{\mu}_t &\sim p(\boldsymbol{\mu}_t|\boldsymbol{z}_t)\\
\text{Latent Dynamics}: && && 
\boldsymbol{z}_t &\sim p(\boldsymbol{z}_{t-1}|\boldsymbol{\alpha}_t)\\
\text{Spatial Process Hyper-Parameters}: && &&
\boldsymbol{\phi}_t &\sim p(\boldsymbol{\phi})\\
\text{Latent Dynamics Hyper-Parameters}: && &&
\boldsymbol{\alpha}_t &\sim p(\boldsymbol{\alpha}_t)
\end{aligned}
$$

:::
::::



**Proposed Improvement**.
We will reimplement the same methodology as proposed in [ [Mahmoudian & Mahammadzadeh, 2014](https://doi.org/10.1007/s10687-014-0180-2), [Heurta & Sanso, 2007](https://doi.org/10.1007/s10651-007-0014-3)] but applied to extremes for climate variables.
We will utilize the same PPL software that was mentioned in the above goals.
For the dynamical system, we will use some simple filtering approaches such as Kalman filters.
However, we could also implement some other methods that use dynamical systems, e.g., NeuralODEs ([Chen et al, 2018](https://doi.org/10.48550/arXiv.1806.07366)) (see [example](https://sebastiancallh.github.io/post/neural-ode-weather-forecast/)) or Universal DE ([Kackauckas et al, 2021](https://doi.org/10.48550/arXiv.2001.04385)).


***

### Moon Goal


> Add a DL method which uses an autoregressive approach to predictions.
> We can directly modify/re-use this model to train on extremes.

$$
\begin{aligned}
\text{Autoregressive Model}: && && 
\boldsymbol{u}_t &= \boldsymbol{f_\theta}(\boldsymbol{u}_{t-1},t) + \boldsymbol{\eta}_t \\
\text{Process Model}: && && 
\boldsymbol{\theta}_t &= \boldsymbol{h_\theta}({\boldsymbol{u}_t,t}) + \boldsymbol{\varepsilon}_t \\
\text{Extreme Data Model}: && &&
\boldsymbol{y}_t &\sim p(\boldsymbol{y}_t|\boldsymbol{\theta}_t)
\end{aligned}
$$

where $\boldsymbol{u}_t$ is a covariate of interest, e.g., temperature, $\boldsymbol{\theta}_t$ is the parameterization of the GEVD/GPD, and $\boldsymbol{y}_t$ is the observation for the extreme value.

**What's Missing**.
Currently the AI methods have only been used on weather.
However, there has been very little exploration into how these mega-models can be reused for climate and even less attention for detection and attribution of extremes.

**Proposed Method**.
The advantage of this method is that we can potentially utilize pretrained models for specific covariates, e.g., temperature, precipitation, over large scales and reuse them as dynamical models.
We will largely follow the **bold goal** except we won't need to 