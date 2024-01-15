---
title: Extreme Value Theory
subject: AI 4 Attribution
short_title: Extreme Value Theory
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

## Introduction

### Issues with Extreme Events


**Spatiotemporal Data**.
The biggest problem is the inherent data with spatiotemporal interactions.
There are dependencies, heterogeneity, data sparsity, and uncertainty.

**Limited data**.
Extreme events are at the tails of the distribution because they are rare events.
This means that there is not a lot of data which means it is difficult to model.

**Dynamical**.
The data is inherently dynamical which means that things (even the definition of an extreme) can change with time.

***
### Modeling Challenges

Because of the issues with the data, we will have issues with the subsequent models.
The Earth is a vastly complex system: it is multiscale, multivariate, high-dimensional, chaotic, and noisy.
This means that we need complex models, i.e., nonlinear, expressive, expensive, to be able to model this type of data.
So, this means that we either need a lot of physics or a lot of data to be able to model this kind of data.
We already have examples of models with a lot of physics like GCMs and RCMs.
They are accurate but they are also known to be expensive, slow and so complicated that they can be considered black boxes.
Data-driven models can learn with a lot of data however, we arrive at the same issue of data that we just described: a vicious cycle.


***
### Potential Solutions

**Better Data Representations**.
We need data representations that highlight the spatial processes and dynamical processes.
We also need to utilize multivariate statistics to couple complex processes when making predictions.
Lastly, we need to include latent variables to capture unseen processes and to reduce the dimensionality of the data which will provide significant speed-ups.

**Better Data-Driven Models**.
Most of the current literature involving extremes utilize very simple linear models which are not sufficient to capture the complexity of the system.
We need more expressive models that capture multiscale, nonlinear relationships. 
They also need to capture the multivariate tendencies.
Lastly, they need to be fast and scalable otherwise it would not be trustworthy in practice.
We see that some of the SOTA weather forecasting almost exclusively use some sort of AI algorithm under the hood.

**Better Uncertainty Quantification**.
We need to be more *pragmatically* Bayesian, meaning be Bayesian for as long as possible until it because too computationally intensive.
We need to incorporate more parameter and process uncertainties.
We also need better predictive uncertainty.
In addition, we need better model uncertainty for physics-based models, e.g., initial conditions, boundary conditions or equations of motions.
We also need better uncertainty for data-driven models, i.e., model parameters.

***
## Formulation

Let's define a spatiotemporal field of a scaler or vector-valued variable of interest, $\boldsymbol{y}$, as:

$$
\begin{aligned}
\boldsymbol{y} = \boldsymbol{y}(\mathbf{x},t) && &&
\boldsymbol{y}:\mathbb{R}^{D_s}\times\mathbb{R}^+\rightarrow\mathbb{R}^{D_y} && &&
\mathbf{x}\in\mathcal{X}\subseteq\mathbb{R}^{D_y} && &&
t \in \mathcal{T} \subseteq\mathbb{R}^{+}
\end{aligned}
$$

where $\mathbf{x}$ is the spatial index and $t$ is the temporal index.

***

### Extreme Values


***

#### Block Maxima/Minima

Here, we are looking at a maximum or minimum within a block of data.
A block is a set time period such as a week, a month, a season or a year.
**Note**: we have to be careful about what we define as a valid time period because some scales exhibit high variability which could be miscategorized as an extreme.

In either case, the theory dictates that extremes generated via a block maxima/minima method will be distributed as a generalized extreme value distribution (GEVD).

***

#### Peak Over Threshold (POT)

***

### Generalized Extreme Value

In the case where we are assume a block maxima method, we have the Generalized Extreme Value Distribution (GEVD).
$$
p(\boldsymbol{y}) \sim \left\{ 1+ \boldsymbol{\xi} 
\left(\frac{\boldsymbol{y}-\boldsymbol{\mu}}{\boldsymbol{\sigma}}\right)\right\}_+^{-1/\xi}
$$
where $\boldsymbol{\mu}$ is the location parameter, $\boldsymbol{\sigma}$ is the scale parameter and $\boldsymbol{\xi}$ is the shape parameter.

***

### Max-Stable Process

Let $\{\boldsymbol{y}(\mathbf{x},t)\}$ be a stochastic process with continuous sample paths.
We assume that we have $N$ IID copies of $\boldsymbol{y}$ available. 
We denote these samples by $\boldsymbol{y}_n$ where $n=1,2,\ldots,N$ and $N\in\mathbb{N}$ denotes the independent replications/realizations.

Let $\{ \boldsymbol{M}_n[\boldsymbol{y}](\mathbf{x},t) \}$ be the pointwise maximum of the underlying process $\boldsymbol{y}_n$.
We can write this explicitly as

$$
\begin{aligned}
\boldsymbol{M}[\boldsymbol{y}](\mathbf{x},t) := \text{max}_{n=1,2,\ldots,N} \hspace{2mm}
\boldsymbol{y}_n(\mathbf{x},t) 
&& &&
 \forall \hspace{2mm} \mathbf{x}\in\mathcal{X}, && t\in\mathcal{T}
\end{aligned}
$$

Our interest is only in the limiting process of $\boldsymbol{M}_n[\boldsymbol{y}](\mathbf{x},t)$ for $n\rightarrow \infty$ because it may provide an appropriate model in order to describe the behaviour of extremes.
In particular, EVT says that if there exists a continuous function

$$
\begin{aligned}
\boldsymbol{z}(\mathbf{x},t) &= \lim_{n\rightarrow\infty}
\left\{ \frac{\boldsymbol{M}_n(\mathbf{x},t) - \boldsymbol{b}_n(\mathbf{x},t)}{\boldsymbol{a}_n(\mathbf{x},t)}\right\} \\
\boldsymbol{a}_n &= \boldsymbol{a}_n(\mathbf{x},t), && && 
\boldsymbol{a}_n:\mathbb{R}^{D_s}\times\mathbb{R}^+\rightarrow \mathbb{R}^{D_y} \\
\boldsymbol{b}_n &= \boldsymbol{b}_n(\mathbf{x},t), && && 
\boldsymbol{b}_n:\mathbb{R}^{D_s}\times\mathbb{R}^+\rightarrow \mathbb{R}^{D_y} 
\end{aligned}
$$

and it has a non-degenerate marginal distribution $\forall \mathbf{x}\in\mathcal{X}$, then this defines an extreme-value process.

*** 

## Algorithm


### 1 - Define Interested Processes


We need to define the extremes we are intersted in as well as the processes we believe cater to those extremes.
For example, we may be interested in the extremes for precipitation so this would be our *Quantity of Interest*.
We also believe that the Mediterranean warming and Jet Stream location are processes which contribute to the precipitation.

**Note**: Not all extreme events are extensions of non-extreme phenomena!

***

### 2 - Analyze Spatiotemporal Correlations.

We need examine how the spatial and temporal dimensions effect each of the observations.
This can come from prior knowledge or from general assumptions.
For example, let's say we have some scattered data at irregular locations.
We may propose that the precipitation is independent of the neighboring weather stations.
However, we propose that the temperature at neighboring locations is informative.
We can do the same for the time domain.

Some widely used tools for detecting the spatial variation is a variogram or information theory metrics.
For time series, we can use the AutoCorrelation function (ACF) or information theory metrics as well.

***

### 3 - Get Samples for Data

Now, we need to acquire samples, preferably IID, but sometimes this is impossible.
From the traditional EVT system, we can use block maximum method over space and time. 
We could also the use Peak Over Threshold (POT) method.

***

### 4 - Describe Extreme Value Data Distribution

We need to describe the data distribution for the extreme values.
For example, we could use the GEVD if we are using the block maximal method.
We could also use the GPD for the POT method.

We also need to describe how the parameters are related. 
For example, we could use a simple parametric model.
We could also use a hierarchical model.
We could also use a dynamical model.

***

### 5 - Fit Parameters of Model

This involves selecting the inference method we wish to use to find the posterior distribution given our model.

***

### 6 - Analysis

This is the most important part.
We can do some post analysis on the distribution of parameters.
We can look at the best fit, i.e., the data likelihood.
We can also look at the return values, i.e.g, the sample distribution at a specific cumulative probability.


**Questions**:

* What is the likelihood of event X with a magnitude Y occuring within a period $\tau$.
* What is the magnitude of variable X for which there is a  % chance of occurring within a $\tau$ period.
