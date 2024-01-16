---
title: Extreme Value Practice
subject: AI 4 Attribution
short_title: Extreme Value Practice
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

## Problems

EVT is not a watertight explanation.
In fact, there are many issues that could occur.
On one hand, there are issues with the IID assumptions which could limit the amount of data which limits the model correctness.
On the other hand, there could be some fundamentally wrong explanations which might incorrectly explain our results.
Below we will outline a few of these issues.

***

### IID Assumptions

The issue is with the assumptions placed upon the distributions: **independent, identically distributed random variables**.

**Independence**. This assumes that each sample is independent from all other assumptions.

**Identically distributed**. This assumes that each sample is taken from the same underlying distribution.
For example, this assumes that there is no seasonality and assumes that the sequence is stationary.
There are many ways to correct for this, e.g., remove the seasonality and correct for known trends.

**Random**. This assumes that this was sampled from a prob. distribution which varies due to chance. 
This assumes that the measurements are unbiased estimators of the desired quantity.
In the case of Earth sciences, this is rarely every true as points that are close to other in space and time are almost always correlated.


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
Some example covariates that one can include would be atmospheric drivers (e.g., ENSO, PDO, NAO), trends (e.g., urbanization, climate), or season cycle.

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

#### Insufficient Data

This is a by-product of not having enough data.
As shown in the previous theory section, we have methods like the block maxima and POT which result in a reduced number of data points.
This induces a 


***

### Component Events

A big problem is the causality associated with the extreme events.
In particular, we could have **compound extreme events** ([Bevacqua et al, 2021](https://doi.org/10.1029/2021EF002340)).
These occur when two or more extreme events occur simultaneously or successively.
Flip through the tabs below to see some examples of these extreme events.

::::{tab-set}
:::{tab-item} Case I
:sync: tab1

Let's say that we directly *observe* a sequence of extreme events.
We could believe that they are connected due to our statistical model.

```{mermaid}
flowchart LR
  A(Drought) --> B(Flooding)
```
However, we could have the true causal relationship between includes some intermediate processes,i.e.:
 
```{mermaid}
flowchart LR
  A(Drought) --> B
  B(Wildfire) --> C
  C(Precipitation) --> D(Flooding)
```
One could very easily get a dataset which links wildfires to floods but this would not be the correct explanation.
The best way to prevent this is to have a domain scientist validate the claims of the model.
However, for extremely complex datasets, one would need a better model or stronger assumptions.
:::
:::{tab-item} Case II
:sync: tab2

Let's say we have combination of extreme events with underlying conditions that amplify the impact of other events.
For example, we could observe two sequential extreme events:
```{mermaid}
flowchart LR
  A(Sea Level Rise) --> B(Flooding)
```

One could easily connect the notion of sea level rise directly to flooding.
However, a better explanation might be the fact that the flooding was caused by the cyclone extreme event which increased the intensity of the flood due to the strong winds.
```{mermaid}
flowchart LR
  A(Sea Level Rise) --> B(Tropical Cyclone Landfall)
  B --> C(Flooding)
```
Again, the best way to prevent this is to have a domain scientist validate the claims.
In addition, one should also try alternative, plausible explanations and compare the results. 
:::
:::{tab-item} Case III
:sync: tab2

We could also have a combination of events which are not classified an extreme event itself however, it leads to an extreme event when combined.
For example, we could observe many cumulative days of no precipitation which could lead to drought.

```{mermaid}
flowchart LR
  A(Cumulative Days without Precipitation) --> B(Drought)
```

We could impose other explanations of drought, e.g., high temperatures, but this is not what we directly observe.

```{mermaid}
flowchart LR
  A(Cumulative Days without Precipitation) --> B(Drought)
  C(Cumulative Days of High Temperature) --> B
```

Again, the best way to prevent this is to have a domain scientist validate the claims.
In addition (again), one should also try alternative, plausible explanations and compare the results. 

:::
::::



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

*** 




**Questions**:

* What is the likelihood of event X with a magnitude Y occuring within a period $\tau$.
* What is the magnitude of variable X for which there is a  % chance of occurring within a $\tau$ period.

