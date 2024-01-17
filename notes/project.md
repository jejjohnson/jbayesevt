---
title: "Game of Dependencies"
subject: AI 4 Attribution
short_title: Project Proposal
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


## Project Goals

> My primary focus is on improving the modeling capabilities using modern data-driven methodologies.
> Most of the current work do manual feature extraction and reduce their statistical models to simple ones.
> I want to take a more data-driven approach whereby we encode as many different prior knowledge as possible into the model itself, and then use modern inference procedures to find the best parameters.
> These additions will hopefully encode more sensible knowledge of the underlying system whilst also respecting the data structure, e.g., spatial, temporal, covariate, dynamical and latent.
> To deal with the small number of samples and inherent uncertainty, we'll adopt the pragmatic Bayesian inference methods, e.g., MCMC and for the larger number of samples, we'll adopt more approximate Bayesian inference methods, e.g., variational inference.
> I hope the tools built here for will be useful for dealing with extremes for Earth sciences in general.
>

 **Note**: 
 this page severely lacks any scientific reasoning and understanding. 
 I will leave this up for discussion with my colleagues at a later time.


***
### Revisiting Foundations

> Part I of this project is to revisit some of the basics of EVT and implement them within a modern framework.
> We examine the basics for extracting extreme values including the block maxima and the peak of thresholds.
> We will look at the basics for modeling extreme values including using custom distributions, e.g., GEVD, GPD, and Poisson processes.
> We will use some of the standard and SOTA Bayesian inference methods using modern PPLs.
> See [Basis](./god/basics) for more information.

$$
\begin{aligned}
\text{Data Representation}: && &&
y_n &\in\mathbb{R}^{D_y} && &&
\mathcal{D} = \{ y_n \}_{n=1}^N, && &&
N = N_t \\
\text{Observation Likelihood}: && &&
y &\sim p(y|\boldsymbol{\theta}) \\
\text{Parameter}: && &&
\boldsymbol{\theta} &\sim p(\boldsymbol{\theta})
\end{aligned}
$$



***

### Safe Goal

> Reimplement the methods proposed in [Philip et al, 2020](https://doi.org/10.5194/ascmo-6-177-2020) where they fitted GEVD and GPD on temperature and precipitation data.
> Instead, we will use more advanced methods for Bayesian inference to improve the parameter uncertainty quantification. We will demonstrate the ease and speed of use using modern PPLs.


**What's Been Done**. 
The original paper showcased different parametric models of extreme values of temperature and precipitation.
The authors explored different ways of implementing process parameterizations.
For example, the authors explored process parameterizations which take a linear or exponential forms.
They also explored covariates like time and/or temperature.


**Data Representation**
We will continuous to use simple representations by assuming the time series is IID.
A major difference between this goal and the above goal is to investigate some of the potential covariates which can help separate the dependencies.
$$
\begin{aligned}
\mathcal{D} = \{ y_n\}_{n=1}^N, && && y_n\in\mathbb{R}^{D_y}&& && N=N_sN_t
\end{aligned}
$$
So we will avoid spatiotemporal aggregation (when possible).

**Model Formulation**.
We will use a hierarchical Bayesian model to try and separate the dependencies viaa  hierarchy of parameters. 
We will include these covariates inside the process parameterization.
$$
\begin{aligned}
\text{Data Likelihood}: && &&
\boldsymbol{y} &\sim p(\boldsymbol{y}|\boldsymbol{\theta},\boldsymbol{x},\mathbf{s},t,\boldsymbol{\alpha})\\
\text{Process Parameterization}: && && 
\boldsymbol{\theta} &\sim p(\boldsymbol{\theta}|\boldsymbol{x},\mathbf{s},t,\boldsymbol{\alpha})\\
\text{Prior Process Hyperparameters}: && &&
\boldsymbol{\alpha} &\sim p(\boldsymbol{\alpha})
\end{aligned}
$$

**What's Lacking**.
They do not focus on the inference methods that can be used to find the parameters.
As far as I see, there is no uncertainty quantification in the parameters of the process nor the hyperparameters of these processes.


**Proposed Improvement**. 
Like the above section, we will use modern PPLs which include advanced inference methods.
In addition, we will thoroughly explore the parameter distributions for the processes and hyperparameters.

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
\boldsymbol{y} &\sim p(\boldsymbol{y}|\boldsymbol{\theta},\boldsymbol{f},\boldsymbol{x},\mathbf{s},t,\boldsymbol{\phi},\boldsymbol{\alpha}) \\
\text{Non-Parametric Parameterization}: && && 
\boldsymbol{\theta} &\sim p(\boldsymbol{\theta}|\boldsymbol{f},\boldsymbol{x},\mathbf{s},t,\boldsymbol{\phi},\boldsymbol{\alpha})\\
\text{Spatial Process}: && &&
\boldsymbol{f} &\sim \mathcal{GP}
\left(\boldsymbol{\mu_\phi}(\boldsymbol{x}), \boldsymbol{k_\alpha}([\mathbf{s},t],[\mathbf{s}',t'])\right) \\
\text{Mean Function Hyperparameters}: && &&
\boldsymbol{\alpha} &\sim p(\boldsymbol{\alpha}) \\
\text{Covariance Function Hyperparameters}: && &&
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