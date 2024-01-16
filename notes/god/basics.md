---
title: Basics
subject: AI 4 Attribution
short_title: Basics
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
> We will explore some staple data likelihoods for modeling extreme values. 
> We can include some standard distributions like the Normal and LogNormal, more long-tail distributions like the T-Student and Stable Distribution, and also more extreme value specific distributions like GEVD and GPD. 
> We will directly find the best parameters of these distributions given observations of extreme values . 
> We will explore various methods for extracting extreme values from spatiotemporal data like block maxima method or the peak-over-threshold (POT) method. 
> We will look at advanced inference methods using the `numpyro` library to estimate the parameters. 
> We will explore different analysis techniques like the quality of data fit (p-p plot, q-q plot, PDFs, CDFs) and return periods to make predictions about unseen extremes. We will also do an exploratory analysis to characterize the autocorrelations in space and time. In addition, we will explore different standardized ad-hoc feature extraction techniques to extract IID data, i.e., the residuals. 
> Some examples include removing trends like the climatology, appropriate time scale aggregation, appropriate spatial scale aggregation, filtering and differencing.

## Data Structure Assumptions

Recall, we are dealing with a spatiotemporal field given by

$$
\begin{aligned}
\boldsymbol{y} = \boldsymbol{y}(\mathbf{x},t)
&& &&
\boldsymbol{y}:\mathbb{R}^{D_s}\times\mathbb{R}^+\rightarrow\mathbb{R}^{D_y}
&& &&
\mathbf{x}\in\Omega_y\subseteq\mathbb{R}^{D_s}
&& &&
t\in\mathcal{T}\subseteq\mathbb{R}^+
\end{aligned}
$$

where $\mathbf{x}$ are the spatial coordinates and $t$ is the temporal coordinate.

***

### I.I.D. Samples

This is the simplest form where we assume each datapoint is independent, i.e., no spatial or temporal dependencies. 
When given a:
* Time Series: this means that we assume there are no temporal correlations.
* Spatial Field - this means that we assume that there are no spatial correlations.
* SpatioTemporal Field - we assume there are no spatial AND temporal correlations.

So the dataset will be:

$$
\mathcal{D} = \{ \boldsymbol{y}_n \}_{n=1}^{N}
\hspace{10mm}
\boldsymbol{y}_n\in\mathbb{R}^{D_y}
$$

where $N=N_s N_t$ are the total number of points in the spatiotemporal datacube.
When given a spatiotemporal datacube, this can be achieved through spatiotemporal aggregations, e.g., 
The reasoning is be

***

### Parametric Model



We assume we have a data likelihood given by:

$$
\boldsymbol{y} \sim p(\boldsymbol{y}|\boldsymbol{\theta})
$$

This distribution could be a Gaussian,a GEVD or a Pareto distribution.
We are interested in finding the best parameters, $\boldsymbol{\theta}$ given the observations, $\boldsymbol{y}$, i.e., the posterior.
The full Bayesian posterior can be written as

$$
p(\boldsymbol{\theta}|\boldsymbol{y}) = \frac{1}{Z}p(\boldsymbol{y}|\boldsymbol{\theta})p(\boldsymbol{\theta})
$$

where $Z$ is a normalization constant.
We can use any inference technique including approximate inference methods or sampling methods.
