---
title: Introduction
subject: AI 4 Attribution
short_title: Intro
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
    EO: Earth Observation
---

> A set of notes to catalogue my progress in applying AI for climate attributions.


### **Introduction**

In this section, you'll find:
* Problem Definition (**TODO**) you'll find a brief overview of the problem of climate attribution.
* literature review (**TODO**) for all papers related to the problem with a particular focus on the problem definition side and statistical modeling side.
* [project proposals](./project.md) - outlines some (everchanging) proposed ideas with a set of goals that I want to accomplish within the project.

***

### **Conceptual**

In this section, you'll find a brief outline of some ideas I deem conceptual important to understand from on an abstract level.
* [extreme value theory](./conceptual/evt.md) - I go over some of the important theorems and concepts.
* [evaluating the extreme value family distribution](./conceptual/eval.md) - I go over some of the staple methods for analysis and evaluation for these types of distributions and parameter estimation.
* [Bayesian modeling](./conceptual/bayes.md) - I outline some important concepts of Bayes rule. 
I also include hierarchical Bayesian models which will be an important for this work.
* [Bayesian inference](./conceptual/bayes_inf.md) - I do an overview of some of the staple methods for finding the best parameters.


***

### **Data**

In this section, you'll find a some sections related to the type of data we will be using for this study and some of the properties.
In general, we will be working with global or regional spatiotemporal EO data.
However, there are some nuances to the type.
* [Datasets](./data/datasets.md) - outlines some of the staple datasets to be used within this study. It includes the CMIPX and ERA5 datasets. I also distinguish some defining characteristics for example the idea of simulation versus reanalysis.
* [Data Access](./data/data_access.md) - outlines how one can quickly access the datasets using python. This will be particularly useful for individuals who don't have a lot of resources and quickly want to prototype different methods without having to download the entire dataset.

***

### **Modeling**

In this section, you'll find some sections related to the modeling aspects detailing how we actually implement some of the conceptual aspects in practice.
* [Features (Manually)](./modeling/features_manual.md) - outlines how we can manually extract features from our spatiotemporal dataset. These are typically "classical methods" done historically and are coupled with simple models.
* [Features (Learned)](./modeling/features_ai.md) - outlines how we can learn the features directly from data. It offers some alternatives to manually extracting features. Many of these methods are very common within the machine learning community.
* [Software](./modeling/software.md) - outlines some software that we can use to accomplish some of the data processing, feature extraction, modeling, and evaluation.


***

### **Cookbook**

In this section, you'll find some sections with recipes with a bit more detail on how we can accomplish specific tasks. These will be used as reference for things outlined in other sections.
* [Filtering EO Data](./cookbook/filtering.md) - outlines how we can manually filter spatiotemporal data to remove high variations.
* [EO Data Anomalies](./cookbook/anomalies.md) - outlines how we can manually extract anomalies from spatiotemporal data.
* [Spatial Averaging](./cookbook/spatial_mean.md) - outlines how we can aggregate the spatial dimension of spatiotemporal data to extract a single time series or patches of time series.
