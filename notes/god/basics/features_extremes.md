---
title: Feature Extraction for Spatiotemporal Dependencies
subject: AI 4 Attribution
short_title: Feature Extraction
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

> In this section, we will do a deeper dive into how one can further preprocess the data to remove extreme values


* Spatially Aggregate Data (Optional)
* Temporally Aggregate Data (Optional)
* Stitching, SuperImposing, Aggregating, Batch Sampling - [PoPPY](https://arxiv.org/pdf/1810.10122.pdf)

**Examples**
- 1D Data Recorded in a sequence of distance or time
- 2D sampling for spatial interpolation
- 3D sampling for spatial interpolation
- Spatiotemporal

**Spatial Scale**
- Changes —> Mean, Variance, Tails, Range, Distribution Shape
- Tools —> Variogram, Predict the scale
- Recale:
	- DownScale/SuperResolution/UpSample
	- Upscaling/Coarsen/DownSample —> Average Arithmetic, Power Law Average, Harmonic, Geometric
- Aggregations
- Creating location weights - https://youtu.be/k9VbyqafnPk?si=biWcgcqwuXVe8RfG 

```python
# filtering - remove high/low frequency signals
# spatiotemporal peaks - spatial,temporal dependencies
# remove climatology - temporal dependencies
# spatial aggregation - spatial dependencies
# rolling mean - spatial, temporal dependencies
```
**Cookbook**
- Spatial Statistics with Declustering Weights —> Grid Cell Size vs Declustered Mean
- Lat-Lon Spatial Averages using weights at poles

## Example PsuedoCode

First, we need some spatiotemporal data.
This data could be any spatiotemporal field, $y=y(\mathbf{s},t)$, representing the extreme values we wish to extract.

```python
y: Array["Dt Dy"] = ...
```

Now, we need to do some preprocessing steps to ensure that we get an iid dataset.
We will remove some of the excess effects.

```python
# filter high frequency signals
y: Array["Dt Dy"] = low_pass_filter(y, params)
# remove climatology
climatology["Dclim"] = calculate_climatology(y, reference_period, params)
y: Array["Dt Dy"] = remove_climatology(y, climatology, params)
# spatial aggregation
y: Array["Dt"] = spatial_aggregator(y, params)
```

Now, we need to select some extreme values.

```python
y_max: Array["Dt"] = block_maximum(y, params)
```