# Bayesian Extreme Values Modeling for Climate (WIP)

> This repo will showcase how we can use some modern PPLs to model extreme values for climate data.
> We will also investigate how we can extend the standard models for EVTs which include spatial and/or temporal considerations.

***
## Installation (TODO)


**Clone Repo**

```bash
git clone https://github.com/jejjohnson/jbayesevt.git
cd jbayesevt
```

**Create Environment**
```bash
conda env create -f environments/environment_ai_gpu.yaml -y
conda activate bayesevt_ai
```

**Install Additional Packages**
There are a few libraries that do not install correctly via the conda environment.

```bash
pip install git+https://github.com/NVIDIA/apex.git -v --disable-pip-version-check --no-cache-dir --no-build-isolation --global-option="--cpp_ext" --global-option="--cuda_ext"
```

***
## Documentation (TODO)




