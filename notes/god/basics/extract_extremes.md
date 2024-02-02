---
title: Calculating Extremes for Spatiotemporal Data
subject: AI 4 Attribution
short_title: Calculating Extremes
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


> In this section, we will look at the 3 most basic methods for calculate extreme values: the block maxima (BM), peak-over-threshold (POT), and point process (PP) methods. We will do detailed demonstrations showcasing how we can extract these extreme values through the lens of discretization via histograms. With histograms, we will show how we can extract extreme values through for each of these methods as a combination of thresholding, selecting maximum values, and counting.

* Make some simple Spatial Correlation Analysis
* Make some temporal correlation analysis
- Regular Discretized - Use a histogram transform with predefined
- Irregular Discretized - Use a search for values above a threshold

To cover all cases, we will need tools for the following operations:
- defining a spatiotemporal block
- Selecting a threshold
- Selecting maximum/minimum values
- Counting the number occurrences of the values above a threshold within a spatiotemporal block
- Summary statistic of occurrences, eg mean, median, etc

**Appendix**
- Applied Discretization Strategies - Cartesian, Rectilinear, Curvilinear, Irregular | `boost-histogram`

**References**
- spatial correlation analysis
* Temporal correlation analysis
* Post analysis of thresholds and discretization schemes

***
#### **Block Maxima**

We define a spatiotemporal block and we take the maximum count within a spatiotemporal block. 

**Algorithm**
1. Define spatiotemporal block
2. Select maximum/minimum values

```python
Clon_coords: Array[“”] = …
Clat_coords: Array[“”] = …
```

***
#### **Peak-Over-Threshold**

We select the values that are over a predefined threshold and discard the rest. We also have the option to discretize this further by taking the maximum within a pre-defined spatiotemporal block. The POT method is a discretized version of the block maxima method, i.e., it is the infinite limit as the size of spatiotemporal block goes to zero whereby each individual point is a maximum. This will result in an irregular grid because there is no guarantee that only one maximum occurrence above a pre-defined threshold within a pre-defined spatiotemporal block. In addition, one could have irregular blocks/shapes but this makes processing much harder. One could further discretize this to count exceedences (and intensity).

***
**Algorithm**
1. Define maximum/minimum threshold values
2. Select values above/below threshold
3. Define spatiotemporal block (Optional)
4. Summary statistic of values within spatiotemporal block (Optional)


***
#### **Point Processes**

This method is similar to the POT method with the spatiotemporal blocks. However, we also count the number of exceedences and take a summary statistic of the values within the block.
- [Point Process Analysis](https://geographicdata.science/book/notebooks/08_point_pattern_analysis.html) | [Point Process NBs](https://github.com/MatthewDaws/PointProcesses) | [PP w/ PyTorch](https://github.com/HongtengXu/PoPPy) | [Marked Spatiotemporal Point Process Simulator](https://github.com/meowoodie/Spatio-Temporal-Point-Process-Simulator)
- [neural spatial temporal point process](https://arxiv.org/abs/2011.04583) | [point process and models](https://arxiv.org/abs/1910.00282)
- [spatial point process w Paula](https://www.paulamoraga.com/tutorial-point-patterns/)
