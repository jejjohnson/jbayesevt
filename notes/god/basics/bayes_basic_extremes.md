---
title: Bayesian Modeling for Extreme Values
subject: AI 4 Attribution
short_title: Bayesian Modeling
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

> In this section, we will do some basic modeling using standard Bayesian methods. We will use the standard distributions for extreme values to model the data directly. We will put priors on the parameters for each distribution. We will use `numpyro` (a PPL) so that we don't have to worry about the manually implementing the inference algorithms and then we can experiment with different methods.

$$
\begin{aligned}
\text{Data Likelihood}: && &&
y_n &\sim p(y_n|\boldsymbol{\theta}) \\
\text{Prior}: && &&
\boldsymbol{\theta} &\sim p(\boldsymbol{\theta})
\end{aligned}
$$

**Distributions**
- Generalized Extreme Value Distribution (GEVD)
- Generalized Pareto Distribution (GPD)
- (Marked) Point Process (MPP) - [Example](https://mark-kramer.github.io/Case-Studies-Python/09.html) 
