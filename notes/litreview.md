---
title: Literature Review
subject: AI 4 Attribution
short_title: Literature Review
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

## Extreme Value Theory

[An Introduction to Statistical Modeling of Extreme Values - Stuart Coles (2001)](https://link.springer.com/book/10.1007/978-1-4471-3675-0)

> Probably the most comprehensive, applied introduction to extreme value theory.
> It's a great introduction for applied people because it has a lot of examples.
> I did feel that it didn't go into a lot of detail for some of the more advanced topics (the later chapters like Multivariate extremes and spatial extremes). 


***

[PyData - Extreme Value Analysis - Dimitry Venger(2022)](https://www.youtube.com/watch?v=7XpZjt8cvgs)

> A nice introduction to EVT from a software perspective.

***

[Weather Extremes](https://www.youtube.com/playlist?list=PLJ_1sjucSSZAZjzvB5mRIsgM0TxjNqb8M)

> A good  playlist for looking at weather extremes. 
> They include topics like dynamical downscaling, simulating convective extremes, statistical modeling, and analyzing extreme events.

***

Workshop on Correlated Climate Extremes - Columbia (2020) - [Day 1](https://youtu.be/wPriuGnwHXU?si=VR8YTpkvNr7KMYsX) | [Day 2](https://youtu.be/NvhIBXMoVQw?si=7l43jLJAL69IPswm)  | [Day 3](https://youtu.be/J8ZoM2CgWTs?si=5s_3Kn4Apz5TOQjg)  | [Day 4](https://youtu.be/iArQByeGRlA?si=HYmgUxZD2zkawS1v)

> A decent workshop with some videos on climate extremes.
> A variety of different talks.

***

[ExtremeClimTwin](https://www.youtube.com/@extremeclimtwin2838)

> A youtube channel with a variety of videos for studying hydro-climate extremes in south-east Europe.


***

[Quantitative Philosophy of Risk](https://www.youtube.com/playlist?list=PLgCR5H4IzggHyHw8dalrVHqHAqZfmTeWa)

> A playlist on youtube which outlines extremes from a risk perspective.
> I found it much more intuitive to understand.
> It also digs more into the theory.

***

### Applications of EVT


***

Fast and Scalable Inference for Spatial Extreme Value Models - [Chen et al (2022)](https://doi.org/10.48550/arXiv.2110.07051)

> A paper which accounts for spatial modeling of extreme values with Gaussian processes.
> They use a hierarchical Bayesian Model for their overall framework.
> They also improve the scaling aspect of GPs by using an approximate inference method, i.e., Integrated Nest Laplace Approximation (INLA)
> Their application is extreme snowfall forecasting.


***

A Bayesian hierarchical spatio-temporal model for extreme temperatures in Extremadura (Spain) simulated by a Regional Climate Model - [Garcia et al (2023)](https://doi.org/10.1007/s00382-022-06638-x)

> This paper accounts for spatial and temporal modeling of extreme values using Gaussian processes.
> They also improve the spatial consistency by including altitude coordinates in addition to lat/lon.
> They use a hierarchical Bayesian Model for their overall framework.
> Their application is extreme temperature for extremadura.

***

Time-varying models for extreme values - [Huerta and Sanso (2007)](https://doi.org/10.1007/s10651-007-0014-3)

> This paper accounts for the dynamics of the parameters when modeling extreme values.
> They use a hierarchical Bayesian Model for their overall framework.
> They implement a linear state space model for the parameters, a process convolution (approximate kernel) for the spatial process, and a standard GEVD for the extreme value data likelihood.
> Their application is ozone concentration in Mexico city.


***

Generalized extreme value distribution with time-dependence using the AR and MA models in state space form - [Nakajimi et al (2012)](https://doi.org/10.1016/j.csda.2011.04.017)

> This paper accounts for the dynamics of the parameters when modeling extreme values.
> They use a hierarchical Bayesian Model for their overall framework.
> They implement a non-linear state space model for the parameters which is similar to the standard ARIMA model.
> They also use a mixture model for the data likelihood.
> Their application is daily stock data.


***

State-Space Models for Maxima Precipitation - [Naveau & Poncet (2007)](https://eudml.org/doc/93452)

> This paper accounts for the dynamics of the parameters when modeling extreme values.
> They use a hierarchical Bayesian Model for their overall framework.
> They use a state-space model for the parameters.
> They also use a mixture model for the data likelihood.
> Their application is precipitation.


***

A spatio-temporal dynamic regression model for extreme wind speeds - [Mahmoudian & Mohammadzadeh (2014)](https://doi.org/10.1007/s10687-014-0180-2)

> This paper accounts for the dynamics of the parameters when modeling extremes.
> They also include temperature as a covariate.
> They use a state-space model for the parameters.
> They use a Gaussian process for the spatial process parameterization.
> **Note**: they do a very methodological introduction and slowly add complexity for their modeling assumptions (EXCELLENT).
> Their application is wind-speed in Iran.


***

## Bayesian Hierarchical Modeling

[A Practical Intro to Bayesian Hierarchical Modeling - Omar Sosa](https://github.com/omarfsosa/tech-talk-hierarchical-models) 

> A great introduction using a running example along with accompanying code.
> It includes a [talk](https://www.youtube.com/watch?v=38yOWMMCeMk) with a great step-by-step introduction.
> The example is featured on the [numpyro ppl package](https://num.pyro.ai/en/stable/tutorials/bayesian_hierarchical_linear_regression.html)


***

[An Visual Introduction to Hierarchical Modeling](http://mfviz.com/hierarchical-models/)

> A great visual introduction.
> It takes you step by step with graphics.


***

## Time Series Modeling

[Time Series Modeling Playlist - Aric LaBarr](https://www.youtube.com/playlist?list=PLjwX9KFWtvNnOc4HtsvaDf1XYG3O5bv5s)

> An excellent introduction to time series modeling within 5 minute chunks for each video.
> Probably the best tutorial to go from 0 to 100 with some of the basic models available in the literature.
> There is a [similar talk](https://www.youtube.com/watch?v=P_RnURpkgdE) with more about the Bayesian

***

### Bayesian Dynamic Linear Models


[BDLM 4 TS Data Analysis - Shervin Khazaili](https://www.youtube.com/watch?v=-RCvVWxa9wg)

> A great intro video to time series modeling using Bayesian Dynamic Linear Models.
> A nice step-by-step approach showing the motivation as well as some simple applications.


***

[Time Series Analysis by State Space Methods - Durbin & Koopman (2012)](https://academic.oup.com/book/16563)

> A good reference book for introducing TS and how we can use state space models.


***

A Guide to State-Space Modeling of Ecological Time Series - [Auger-Méthé et al, 2021](https://doi.org/10.1002/ecm.1470)

> A paper which nicely outlines how one can introduce state-space models for modeling time series.
> I really like the step-by-step approach which slowly builds upon the model complexity by addressing some of the dataset assumptions 1-by-1.