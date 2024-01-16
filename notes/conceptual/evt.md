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

### Definition of Extremes

There is no exact definition of an "extreme".
This is because it is an arbitrary classification of a real quantity.

**Extreme Indices**.
These are based on the probability of relative occurrence.
For example, we could say that the $90^{th}$ percentile of the observed maximum temperature.
We typically assign a threshold which characterizes the severity of a probable outcome should the threshold be crossed.
These are typically *moderate extremes* which are in the $5^{th}$ percentile.

**Extreme Value Theory**.
These are based on a theory called the Extreme Value Theory (EVT).
This is a more rigorous definition of extremes which involves more theory.
We need EVT because of the sampling issues associated with these rare events; typically we only observe $<1-5\%$ percentile of the total samples.
In addition, EVT will allow us to estimate the probability of "values never seen".


***
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

**Extreme value distributions** (EVD) are the limiting distributions for the maximum/minimum of large collections of independent random variables from the same arbitrary distribution.

There are many instances of ways to measure extreme values.
In particular, there are 3 ways of defining extremes: 1) maxima, 2) thresholding, 3) counting exceedences. 
The  most common methods are the maxima

```{figure} ./assets/evt_trifecta.jpeg
:name: extremes
:width: 490px
:alt: Random image of the beach or ocean!
:align: center

A figure from Philippe showcasing how we can model extreme values with three different perspectives: 1) maxima values and GEV, 2) tail behaviour with GPD, and 3) counting exceedences with Poisson processes. [[Source]()]
```




***

### Maxima

Here, we are looking at a maximum or minimum within a block of data (see example [figure](https://analystprep.com/study-notes/wp-content/uploads/2019/10/page-43.jpg))
A block is a set time period such as a week, a month, a season or a year.
**Note**: we have to be careful about what we define as a valid time period because some scales exhibit high variability which could be miscategorized as an extreme.
A typical application is to first find the annual maximum value of a spatiotemporal field.

:::{note} Example: Binning
:class: dropdown

A very simple example for maximum block estimation is to use a histogram which discretizes a continuous field.
A good package is the [`boost-histogram``]() package which works well with spatiotemporal data structures like `xarray`.


First, let's get some pseudo data
```python
y: Array["Ds Dt"] = ...
```
Now, we need to describe the spatiotemporal discretization.
This can be done via [binning](https://boost-histogram.readthedocs.io/en/latest/_images/histogram_design.png).
```python
# create bins
latbins = np.arange(-90, 90, 100)
lonbins = np.arange(-180, 180, 100)
tbins = np.arange("1950", "2020", "Yearly")
```
Now, we want to take the max value of each bin (TODO)
```python
```
:::

***

#### Generalized Extreme Value Distribution

In either case, the Fisher-Tippet Asymptotic Theorem dictates that extremes generated via a block maxima/minima method will converge to a generalized extreme value distribution (GEVD).
$$
p(y) \sim 
\begin{cases}
\exp \left[ 1+ \xi 
\left(\frac{y-\mu}{\sigma}\right)\right]_+^{-1/\xi}, && \xi \neq 0 \\
\exp \left[-\exp\left( - \frac{y - \mu}{\sigma} \right) \right]_+, && \xi=0
\end{cases}
$$
where $(y)_+=\text{max}\left\{ 0, y \right\}$, $\boldsymbol{\mu}$ is the location parameter, $\boldsymbol{\sigma}$ is the scale parameter and $\boldsymbol{\xi}$ is the shape parameter.
The location parameter, $\mu$, is not the mean of the distribution but rather the *center* of the distribution.
Similarly, the scale parameter, $\sigma$, is not the standard deviation of the distribution but rather it governs the size of the deviations about $\mu$.
The shape parameter $\xi$ describes the tail behaviour of the GEV distribution which is arguably the most important choice as it dictates the shape of the distribution (see [figure](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*cCIER1t6-MCEi9Usyt3D2w.png)). Below, we outline the cases:

**Type I**.
The Gumbel distribution occurs when $\xi=0$ which results in light tails.
It is used to model the maximum/minimum of a dataset as it extends over the entire range of real numbers.
This is similar to other "light tailed" distributions like the Normal, LogNormal, Hyperbolic, Gamma, and Chi-Squared distributions.
This is common when trying to describe the *domain of attraction* for common distributions like the normal, exponential or gamma.
This is not typically found in *real world data* but there could be some transformed space whereby this is useful.

**Type II**. The Frechet distribution occurs when $\xi>0$ which results in heavy tails.
This is similar to other "heavy tailed" distributions like the InverseGamma, LogGamma, T-student, and Pareto distributions.
This is typically found for variables like precipitation / rainfall estimation, stream flow, flood analysis, human lifespan, financial returns and economic damage.

**Case III**.
The Weibull distribution occurs when $\xi<0$ which results in bounded tails.
This is similar to the Beta distribution
This distribution is common for many variables like temperature, wind speed, pollutants, and sea level.
It has also been known to 

Once we have the parameters of this distribution, we can calculate the return levels. See my [evaluation guide](./eval.md) for more information on calculating return levels.

$$
\begin{aligned}
\end{aligned}
$$

:::{note} Choosing Distributions
:class: dropdown

On a practical note, we need to decide which case of the shape parameter we need to choose.
We often choose this manually because there is research which shows that it is quite hard to fit via data.
There are a few ways we can choose.

**Strong Prior**. The researcher will manually assign the case because they have strong prior knowledge, aka experience, and domain expertise.

**Hypothesis Testing**. One can conduct hypothesis testing by assigning a hypothesis and null hypothesis to each case.

**Conservative**. Fréchet is the most conservative estimate.

:::

***

### Tail Behaviour

The **peak over threshold** approach is based on the idea of modelling data over a high enough threshold.
We can select the threshold to trade-off the bias and variance.
On one hand, one could select a high threshold which will reduce the number of exceedances. This will increase the estimation variance  and the reliability of the parameter estimates.
On the other hand, one could select a low threshold which will induce a bias because the GPD could fit the exceedances poorly.

$$
F_\mu(y) = \text{Pr}\left\{Y - \mu \leq y|Y>\mu\right\} = \frac{F(y+\mu) - F(\mu)}{1 - F(\mu)}, y > 0
$$

***

#### Generalized Pareto Distribution

According to the Gnedenko-Pickands-Balkema-DeHaan (GPBdH) theorem, using the POT method will converge to the **generalized Pareto distribution** (GPD).


**Case I**.
The ... distribution occurs when $\xi>0$ which results in heavy tails.
This is similar to "heavy-tailed" distributions like the Pareto-type distributions.

**Case II**.
The ... distribution occurs when $\xi=0$ which results in light tails.
This is similar to other "light tail" distributions like the exponential-type distribution.

**Case III**.
The ... distribution occurs when $\xi<0$ which results in bounded tails.
This is similar to other "bounded tailed" distributions like the Beta-type distributions.



***

### Counting Exceedences (**TODO**)

#### Poisson Process (**TODO**)

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
## Problems

```{figure} https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fsrep05884/MediaObjects/41598_2014_Article_BFsrep05884_Fig1_HTML.jpg?as=webp
:name: extremes
:width: 490px
:alt: Random image of the beach or ocean!
:align: center

A figure showcasing how the location, scale and shape correspond to different distribution shapes. For example, 1) the location parameter can represent the location shifts in maxima, 2) the scale parameter can demonstrate the scale shift in maxima which represents the change in variability, and 3) the shape parameter can demonstrate the distribution shape change which represents a change in symmetry. [[Kodra & Ganguly (2014)](https://doi.org/10.1038/srep05884)]
```
***

### IID Assumptions

The issue is with the assumptions placed upon the distributions: **independent, identically distributed random variables**.
**Independence** assumes that each sample is independent from all other assumptions.
**Identically distributed** assumes that each sample is taken from the same underlying distribution.
For example, this assumes that there is no seasonality and assumes that the sequence is stationary.
There are many ways to correct for this, e.g., remove the seasonality and correct for known trends.
**Random** assumes that this was sampled from a prob. distribution which varies due to chance. 
This assumes that the measurements are unbiased estimators of the desired quantity.
In the case of Earth sciences, this is rarely every true.


:::{note} Quickie: Temporal Stationarity
:class: dropdown

We can remove the temporal stationarity constraint by parameterizing the parameters of the distribution via time, $t$.
$$
\theta \sim p(\theta|t,\alpha)
$$
Then results in data likelihood that is conditionally independent.
$$
p(\alpha,\theta|y) \propto p(y|\theta,t,\alpha)p(\theta|t,\alpha)p(\alpha)
$$

:::

:::{note} Quickie: Spatial Stationarity
:class: dropdown

We can remove the spatial stationarity constraint by parameterizing the parameters of the distribution via the coordinates, $\mathbf{s}$.
$$
\theta \sim p(\theta|\mathbf{s},\alpha)
$$
Then results in data likelihood that is conditionally independent.
$$
p(\alpha,\theta|y) \propto p(y|\theta,\mathbf{s},\alpha)p(\theta|\mathbf{s},\alpha)p(\alpha)
$$

:::


***

### Component Events

::::{tab-set}
:::{tab-item} Case I
:sync: tab1

We could have 

```{mermaid}
flowchart LR
  A(Drought) --> B(Flooding)
```

However, we could have the true causal relationship between includes some intermediate processes.
 
```{mermaid}
flowchart LR
  A(Drought) --> B
  B(Wildfire) --> C
  C(Precipitation) --> D(Flooding)
```
The best way to prevent this is to have a domain scientist validate the claims of the model.
However, for extremely complex datasets, one would need a better model or stronger assumptions.
:::
:::{tab-item} Case II
:sync: tab2

```{mermaid}
flowchart LR
  A(Sea Level Rise) --> B(Tropical Cyclone Landfall)
  B --> C(Flooding)
```

:::
:::{tab-item} Case III
:sync: tab2

```{mermaid}
flowchart LR
  A(Cumulative Days without Precipitation) --> B(Drought)
```

:::
::::

A big problem is the causality associated with the extreme events.
In particular, we could have **compound extreme events** ([Bevacqua et al, 2021](https://doi.org/10.1029/2021EF002340)).
These occur when two or more extreme events occur simultaneously or successively.

**Example I**. 
We could have a sequence of extreme events.
We could have a *drought* which causes a *wildfire* which causes *precipitation* which causes *flooding*.
One could very easily get a dataset which links wildfires to floods but this would not be the correct explanation.

**Example II**. 
We could have a combination of extreme events with underlying conditions that amplify the impact of other events.
We could have *sea level rise* which causes a *tropical cyclone landfall* which causes *flooding*.
One could easily connect the notion of sea level rise directly to flooding.
However, a better explanation might be the fact that the flooding was caused by the cyclone extreme event which was larger due to 

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


***

## Resources

* Presentation by Reider (2014) - [Slides (PDF)](https://www.ldeo.columbia.edu/~amfiore/eescG9910_f14_ppts/Rieder_EVTPrimer.pdf)
* Extreme Value Theory: A Practical Introduction - Herman (200..) - [Slides (PDF)](http://schumacher.atmos.colostate.edu/gherman/EVT_V1P1.pdf)