---
title: Spatiotemporal Effects
subject: AI 4 Attribution
short_title: Spatiotemporal
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
> We will incorporate spatiotemporal effects into our model assumptions. 
> We will use nonparametric Gaussian process models  to account for the spatial and temporal autocorrelations present within the data. 
> We assume that each of the parameters of the distribution are a random field given which is the result of an underlying latent spatial process. 
> Then, we can say that the extreme values are conditionally independent of the parameters of the data likelihood. 
> These latent models will be used to parameterize the data likelihood parameters. We can include the covariates within the kernel function (Deep Kernel Learning) or we can include them within the mean function. 
> The heterogeneity can be accounted for by having a separate GP for the scale parameter for the data likelihood. We can use approximations like inducing points or spectral approximations to deal with the large number of spatial samples present.