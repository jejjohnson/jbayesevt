---
title: Game of Dependence
subject: AI 4 Attribution
short_title: Game of Dependence
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

## Whirlwind Tour

**Extreme Value Data Likelihoods**. 
We will explore some staple data likelihoods for modeling extreme values. We can include some standard distributions like the Normal and LogNormal, more long-tail distributions like the T-Student and Stable Distribution, and also more extreme value specific distributions like GEVD and GPD. We will directly find the best parameters of these distributions given observations of extreme values . We will explore various methods for extracting extreme values from spatiotemporal data like block maxima method or the peak-over-threshold (POT) method. We will look at advanced inference methods using the `numpyro` library to estimate the parameters. We will explore different analysis techniques like the quality of data fit (p-p plot, q-q plot, PDFs, CDFs) and return periods to make predictions about unseen extremes. We will also do an exploratory analysis to characterize the autocorrelations in space and time. In addition, we will explore different standardized ad-hoc feature extraction techniques to extract IID data, i.e., the residuals. Some examples include removing trends like the climatology, appropriate time scale aggregation, appropriate spatial scale aggregation, filtering and differencing.

**Covariate Effects**.
We will incorporate covariates to try and make the data more IID. We will look at covariates such as the spatial coordinates, the temporal coordinates and any related variables of interest. Some variables include temperature and precipitation. We can also explore local and global covariates like “warming”. We will explore simple statistical models like linear functions and then more complex functions like basis functions or perhaps nonlinear functions. We will use Bayesian Hierarchical Models (BHMs) to separate the parameter uncertainty of the process with the hyper-parameters of the process Parameterization. To select the best parameterization, we can use some traditional model selection techniques like AIC or BIC.

**Spatiotemporal Effects**.
We will incorporate spatiotemporal effects into our model assumptions. We will use nonparametric Gaussian process models  to account for the spatial and temporal autocorrelations present within the data. We assume that each of the parameters of the distribution are a random field given which is the result of an underlying latent spatial process. Then, we can say that the extreme values are conditionally independent of the parameters of the data likelihood. These latent models will be used to parameterize the data likelihood parameters. We can include the covariates within the kernel function (Deep Kernel Learning) or we can include them within the mean function. The heterogeneity can be accounted for by having a separate GP for the scale parameter for the data likelihood. We can use approximations like inducing points or spectral approximations to deal with the large number of spatial samples present.

**Dynamical Effects**.
We will make the transition from coordinate-based models to field-based models by way of state space models (SSM). To start, we can examine some simple structural time series methods (STS) where we can manually fit the periodicity and covariates. We can also use an entire family of Bayesian filtering methods like KF, EKF, UKF and ADF. These methods will have more advanced inference methods like approximate Gaussian assumptions and Variational methods. We’re also free to include other sampling methods like MCMC, ensemble methods and particle filters for inference. To deal with scalability issues, we can use convolutions for the spatial Parameterizations and simple time steppers like Euler. We can also include ODEs/PDEs to include more physics within the spatial operators. In addition, we can include more traditional numerical time steppers for more stable rollouts (Autoregressive applications).

**Latent Variable Effects**.
We can include more flexibility by considering latent variables. We can use flexible flow transformations (bijective, Surjective, stochastic) to encode the covariates or other observations. These could provide more expressive representations and possibly more scalability by reducing the dimension drastically. We could use a library of pre-trained relevant covariate Embeddings for more expressive representations. These transformations are fully compatible with state space models.

**Large-Scale Multivariate Effects**.
It is very evident that large scale DL methods have had great success in predicting weather. However, very little attention has been paid to predicting climate and even less has been explored for extremes. Nevertheless, there is a wealth of information present within these models as they input large amounts of Multivariate, spatiotemporal data. We will look at using these pretrained models as dynamical models which can be included as relevant covariates to our extremes models. We can use standard nonlinear SSM to apply them, e.g., EKF, UKF, or ADF. We can also include methods like ensemble Kalman filters or particle filters. Lastly, we can explore retraining these models to predict the appropriate scales necessary for climate projections and extremes.