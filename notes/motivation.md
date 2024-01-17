---
title: Motivation
subject: AI 4 Attribution
short_title: Motivation
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

### What Do We Know?

- The climate is changing --> we have observations and climate projections
- why the climate is changing --> anthropogenic activity
- one affect of climate change --> more frequent extreme events.

***

### Why Do We Care?

**TLDR**: We care because extreme events on Earth impact humans directly.

**Weather & Climate Variables**:

> Mainly understanding how individual

- Temperature
- Climate
- Wind


**Phenomena**

> Quantifying changes in phenomena in the natural world.
> Many of them are convective extremes, i.e., High Winds, Flash Flooding, Lightning, Tornados, Giant Hail and Land Slides.

- Quantifying monsoons
- El Niño and other modes of variability
- Quantify poleward/equatorward extremes in jet positioning
- 

**Impacts on the Natural Physical Environment**

> The adverse affects on the human population

- Quantifying daily maximum concentrations of a harmful chemical species
- Extreme precipitation can lead flooding either directly or via streamflows.
- Extreme windstorms and/or tropical cyclone intensity can lead to infrastructure damage
- Extreme heat waves or cold snaps can lead to high prices or harm done to infrastructure. 
- Drought can cause damage to the agriculture industry which is very vulnerable to prolonged periods of extreme temperatures.

***


```{figure} https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fsrep05884/MediaObjects/41598_2014_Article_BFsrep05884_Fig1_HTML.jpg?as=webp
:name: extremes
:width: 490px
:alt: Random image of the beach or ocean!
:align: center

A figure showcasing how the location, scale and shape correspond to different distribution shapes. For example, 1) the location parameter can represent the location shifts in maxima, 2) the scale parameter can demonstrate the scale shift in maxima which represents the change in variability, and 3) the shape parameter can demonstrate the distribution shape change which represents a change in symmetry. [[Kodra & Ganguly (2014)](https://doi.org/10.1038/srep05884)]
```
***

### What We Want to Know?

However, we want to know:
- What...? When...? How...?
- Can we predict (anticipate the frequency) of extreme events?
- Human Risk assessment --> hobsow?

**How ongoing climate change affects the frequency and intensity of the extreme events**.

--> Can we attribute specific covariates to extreme events.

***

#### Common Objectives

**Estimation**.
Can we estimate the value that occurs, on average, once every 1,000 years, i.e., the 1,000 return level.

**Process Identification**.
Cn we identify environmental covariates that drive extremes.

**Hypothesis Testing**.
Can we confirm that the likelihood of an extreme event is changing over time?

**Comparisons**.
Can we determine if two locations are asymptotically dependent?

**Projections**.
Can we project the change in the $99.9^{th}$ percentile in the year 2050?


***

### How Can We Understand?

**Physical Understanding**. 
Our knowledge of the physics and causal relationships between variables will be the greatest tool when it comes to understanding extremes.
For example, we have a lot of knowledge about climate change and the Greenhouse Gas Effect which could be causes to many different types of extreme events.

**Simulations**.
We encode this physical knowledge into computer code which reflect our understanding. From this, we can run simulations under different conditions to see *what would happen if...?*
For example, we can run simulations with and without different forcing scenarios.
See [my datasets guide](./data/datasets) for more details where I outline some available climate simulations.


***

### Why is it Challenging?

Most of our intuition and methodology is built around the mean and standard deviation from the mean.
However, extremes are rare events and the mean and variance are poor indicators of rare events.
This is because they don't give us information about the tail of the distribution where rare events live.
Similarly, measures like correlation are also poor indicators because they are still based around the first 2 moments.
Thus, we need new and better ways to describe distributions and the dependencies between random variables.