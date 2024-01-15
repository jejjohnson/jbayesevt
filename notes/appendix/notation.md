---
title: Notation
subject: AI 4 Attribution
short_title: Notation
authors:
  - name: J. Emmanuel Johnson
    affiliations:
      - CSIC
      - UCM
      - IGEO
    orcid: 0000-0002-6739-0053
    email: juanjohn@ucm.es
license: CC-BY-4.0
keywords: notation
---

## Spatial Coordinates

$$
\mathbf{s} \in \Omega \subseteq \mathbb{R}^{D_s}
$$

For example, we can have:

$$
\begin{aligned}
\text{Cartesian}: && && \mathbf{s} &= [x,y,z]\\
\text{Spherical}: && && \mathbf{s} &= [\lambda,\phi, r]
\end{aligned}
$$

## Temporal Coordinates

$$
t \in \mathcal{T} \subseteq \mathbb{R}^+
$$

For example, we can have:

$$
\begin{aligned}
t &= [\text{seconds}] \\
t &= [\text{hours}]
\end{aligned}
$$


## Observations

> Measurements we can actually observe.

$$
\begin{aligned}
\boldsymbol{y} &= \boldsymbol{y}(\mathbf{s},t), && &&
\boldsymbol{y}: \mathbb{R}^{D_s}\times\mathbb{R}^+\rightarrow\mathbb{R}^{D_y} 
&& &&
\mathbf{s}\in\Omega_y\subseteq\mathbb{R}^{D_s} && &&
t \in \mathcal{T}_y \subseteq \mathbb{R}^+
\end{aligned}
$$


## Covariate

> Data which we believe is conditionally important for our model.

$$
\begin{aligned}
\boldsymbol{x} &= \boldsymbol{x}(\mathbf{s},t), && &&
\boldsymbol{x}: \mathbb{R}^{D_s}\times\mathbb{R}^+\rightarrow\mathbb{R}^{D_x} 
&& &&
\mathbf{s}\in\Omega_x\subseteq\mathbb{R}^{D_s} && &&
t \in \mathcal{T}_x \subseteq \mathbb{R}^+
\end{aligned}
$$

## Quantity of Interest (QoI)

> The true quantity we are interested in estimating.

$$
\begin{aligned}
\boldsymbol{u} &= \boldsymbol{u}(\mathbf{s},t), && &&
\boldsymbol{u}: \mathbb{R}^{D_s}\times\mathbb{R}^+\rightarrow\mathbb{R}^{D_x} 
&& &&
\mathbf{s}\in\Omega_u\subseteq\mathbb{R}^{D_s} && &&
t \in \mathcal{T}_u \subseteq \mathbb{R}^+
\end{aligned}
$$

## Latent Variables

> Unknown, unobserved variables

$$
\begin{aligned}
\boldsymbol{z} &= \boldsymbol{z}(\mathbf{s},t), && &&
\boldsymbol{z}: \mathbb{R}^{D_s}\times\mathbb{R}^+\rightarrow\mathbb{R}^{D_x} 
&& &&
\mathbf{s}\in\Omega_z\subseteq\mathbb{R}^{D_s} && &&
t \in \mathcal{T}_z \subseteq \mathbb{R}^+
\end{aligned}
$$

