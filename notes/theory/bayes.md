---
title: Bayesian Modeling
subject: Finding the Parameters
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


## Bayes Rule

$$
p(\boldsymbol{\theta}|\mathcal{D}) = \frac{1}{Z}p(\mathcal{D}|\boldsymbol{\theta})p(\boldsymbol{\theta})
$$

where $Z$ is the normalizing coefficient given by the equation:

$$
Z = \int_\mathcal{D} p(\mathcal{D}|\boldsymbol{\theta})p(\boldsymbol{\theta})d\mathcal{D}
$$

***

### Hierarchical Bayesian Modeling

$$
\begin{aligned}
\text{Data Model}: && &&
p(\mathcal{D}|\boldsymbol{\theta},\boldsymbol{\alpha}) \\
\text{Process Model}: && &&
p(\boldsymbol{\theta}|\boldsymbol{\alpha}) \\
\text{Parameter Model}: && &&
p(\boldsymbol{\alpha}) \\
\end{aligned}
$$

***

## Inference

*Inference* refers to how we find the posterior distribution.