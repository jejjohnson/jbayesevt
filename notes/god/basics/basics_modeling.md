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

We have the **joint distribution** which shows how we believe the data and the parameters factorize.

$$
\begin{aligned}
p(\mathcal{D},\boldsymbol{\theta}) = p(\mathcal{D}|\boldsymbol{\theta})p(\boldsymbol{\theta})
\end{aligned}
$$

In this case, we believe that the data can be explained by the parameters.
Now, this is our belief but we need use Bayes rule to find a pragmatic way of finding the parameters.
We can look at the **posterior distribution** which

$$
p(\boldsymbol{\theta}|\mathcal{D}) = \frac{1}{Z}p(\mathcal{D}|\boldsymbol{\theta})p(\boldsymbol{\theta})
$$

where $Z$ is the marginal likelihood given by

$$
Z := p(\mathcal{D})=\int p(\mathcal{D}|\boldsymbol{\theta})p(\boldsymbol{\theta})d\boldsymbol{\theta}
$$

We assume that there is one set of global, shared hidden variables, $\boldsymbol{\theta}$.

$$
p(\mathcal{D}|\boldsymbol{\theta})p(\boldsymbol{\theta}) = p(\boldsymbol{\theta})\prod_{n=1}^Np(\mathcal{D}_n|\boldsymbol{\theta})
$$