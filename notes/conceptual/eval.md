---
title: Evaluation
subject: AI 4 Attribution
short_title: Evaluation EVT
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


## Analysis

### Variogram

```{figure} https://miro.medium.com/v2/resize:fit:912/format:webp/0*VLG9IkCdXpanUhdT.png
:name: earth-sys-decomp
:width: 490px
:alt: Random image of the beach or ocean!
:align: center

Example of Variogram. [[Source: Medium](https://ai.plainenglish.io/what-is-stationarity-in-spatial-data-f541b04b5811)]
```

This can be used to assess the strength of a the spatial dependencies given a kernel function.

***

### Correlogram


This figure is used to give us an idea of some of the patterns we can expect to see in multivariate data.


```{figure} https://www.data-to-viz.com/graph/IMG/correlogram1.png
:width: 490px
:alt: Random image of the beach or ocean!
:align: center

Example of a Correlogram. [[Source](https://www.data-to-viz.com/graph/correlogram.html)]
```

We have some additional variations we can use to try and describe the data better.
For example, we can try to fit linear relationships between each of the variables ([see example](https://www.data-to-viz.com/graph/correlogram.html)).
We could also color-code some of the data points if they belong to a specific category ([see example](https://www.data-to-viz.com/graph/correlogram.html)).
Lastly, we could customize the assumed distribution in the diagonals (instead of histograms) ([see example](https://python-graph-gallery.com/111-custom-correlogram/)).

***

### Autocorrelation

We can look at the autocorrelation between the time periods.




```{figure} https://www.statsmodels.org/stable/_images/graphics_tsa_plot_acf.png
:width: 490px
:alt: Random image of the beach or ocean!
:align: center

Example of a Correlogram. [[Source](https://www.data-to-viz.com/graph/correlogram.html) | [statsmodels](https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_acf.html)]
```

We can extend this to the partial autocorrelation function ([see example](https://www.statsmodels.org/devel/generated/statsmodels.graphics.tsaplots.plot_pacf.html)).

***


### Cross Correlation

We can look at the cross correlation between two time series of different variables.


```{figure} https://static.wixstatic.com/media/9b2dd8_aee40fe153ed499b994e18033e316bdc~mv2.png/v1/fill/w_848,h_714,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/9b2dd8_aee40fe153ed499b994e18033e316bdc~mv2.png
:width: 490px
:alt: Random image of the beach or ocean!
:align: center

Example of a Correlogram. [[Source](https://www.datainsightonline.com/post/cross-correlation-with-two-time-series-in-python) | [matplotlib](https://matplotlib.org/stable/gallery/lines_bars_and_markers/xcorr_acorr_demo.html#sphx-glr-gallery-lines-bars-and-markers-xcorr-acorr-demo-py)]
```

https://matplotlib.org/stable/gallery/lines_bars_and_markers/xcorr_acorr_demo.html#sphx-glr-gallery-lines-bars-and-markers-xcorr-acorr-demo-py


***

### Seasonal Decomposition



```{figure} https://sthalles.github.io/assets/time-series-decomposition/cover.png
:width: 490px
:alt: Random image of the beach or ocean!
:align: center

Example of a Seasonal Decomposition. [[Source](https://sthalles.github.io/a-visual-guide-to-time-series-decomposition/) | [statsmodels](https://duchesnay.github.io/pystatsml/statistics/time_series.html)]
```





https://duchesnay.github.io/pystatsml/statistics/time_series.html



***

## Empirical Fit

### P-P Plot



```{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Probability-Probability_plot%2C_quality_characteristic_data.png/600px-Probability-Probability_plot%2C_quality_characteristic_data.png
:name: earth-sys-decomp
:width: 490px
:alt: Random image of the beach or ocean!
:align: center

Example of p-p plot from wikipedia. [[Source: Wikipedia](https://en.wikipedia.org/wiki/P–P_plot)]
```

This is also known as the *probability-probability plot*, the *percent-percent plot*, or the *p-value* plot.
It is used for assessing how closely two datasets agree and/or the residuals. See [wiki](https://en.wikipedia.org/wiki/P–P_plot) for more details.

**Note**: this plot only works when we have the theoretical cumulative distribution.


***


### Q-Q Plot

```{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Normal_normal_qq.svg/600px-Normal_normal_qq.svg.png
:name: earth-sys-decomp
:width: 490px
:alt: Random image of the beach or ocean!
:align: center

Example of Q-Q plot from wikipedia. [[Source: Wikipedia](https://en.wikipedia.org/wiki/Q–Q_plot)]
```

This is the quantile-quantile plot.
This is a graphical tool to compare two probability distributions by comparing their quantiles versus one another.
See [wiki](https://en.wikipedia.org/wiki/Q–Q_plot) for more details.

***

## Predictions

### Return Period

We can extrapolate an distribution by computing the $p$-return level.
This represents the high quantile for which the probability that the maximym exceeds this quantile is $1/p$.
This concept is known as the **return period**.
The **return period** of a particular event is the inverse probability that the event will be exceeded in any given year.
For example, the $p$-year return level is associated with a return period of $p$ years.
The $1/p$ return level is the $1-p$ quantile of an arbitrary quantile function for a distribution.([Mahmoudian & Mahammadzadeh, 2014](https://doi.org/10.1007/s10687-014-0180-2)).



To compute the return level of $y_p$ s.t. the distribution, $\text{Quantile}(p)=1-p$.
We can solve for $p$ which results in the following formula.
$$
\begin{aligned}
\text{Distribution}(y_p) &= 1 - p\\
y_p &= \text{Distribution}^{-1}(1-p)=\text{Quantile}(1-p)
\end{aligned}
$$




```{figure} https://www.metoffice.gov.uk/binaries/content/gallery/metofficegovuk/images/industry/diagrameva_article.png
:name: earth-sys-decomp
:width: 490px
:alt: Random image of the beach or ocean!
:align: center

Example of return period for temperature. [[Source: MetOffice](https://www.metoffice.gov.uk/services/research-consulting/weather-climate-consultancy/extreme-value-analysis)]
```

This is also known as the *recurrence interval* or *repeat interval* which is an average time or an estimated average time between events.
In the case of extreme events, these can include floods, heatwaves, or droughts.
See [wiki](https://en.wikipedia.org/wiki/Return_period) for more details.

:::{note} Example: GEVD
:class: dropdown
The return period is a nifty tool for making predictions of along the tails of the distribution.
We simply need the [quantile function](https://en.wikipedia.org/wiki/Quantile_function) for the arbitrary distribution.
The quantile function maps some input, $u$, to a threshold value $y$ so that the probability of $y$ being less than or equal than $y$ is $p$.
$$
\text{Q}:[0,1] \rightarrow \mathbb{R}
$$
We can an example for the **GEVD**.
For the GEVD, we have the quantile function defined as
$$
\text{Q}_{GEVD}(p;\mu,\sigma,\xi) = 
\begin{cases}
\mu - \frac{\sigma}{\xi}
\left[ 1 - \left( - \log p\right)^{-\xi} \right], && \xi \neq 0 \\
\mu - \sigma\log\left( - \log p\right), && \xi = 0
\end{cases}
$$
One can easily find this function (along with many others) in a [wiki](https://en.wikipedia.org/wiki/Generalized_extreme_value_distribution) or any similar resource.
Now, we simply plug in the return level, i.e., $1-p$, into the quantile function
$$
\text{Q}_{GEVD}(1-p;\mu,\sigma,\xi) 
\begin{cases}
\mu - \frac{\sigma}{\xi}
\left\{ 1 - \left[ - \log(1-p)\right]^{-\xi} \right\}, && \xi \neq 0 \\
\mu - \sigma\log\left\{ - \log(1 - p)\right\}, && \xi = 0
\end{cases}
$$

:::


***

### Expected Shortfall

Ultimately, the goal of EVT is to compute the value at risk.
We can derive the expected shortfall (conditional rv).
$$
y_p = \mu - \frac{\sigma}{\xi}\left[ 1 - \left(\frac{N}{N_\mu} (1 - p) \right)^{-\xi} \right]
$$

where:

* $y_p$ - the random variable
* $\mu$ - the threshold (in percentage terms)
* $N$ - number of observations
* $N_\mu$ - # of observations that exceed the threshold

We can define the expected shortfall (ES) as:
$$
\text{ES} = \frac{y_p}{1 -\xi} + \frac{\sigma - \xi\mu}{1 - \xi}
$$