import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import seaborn as sns
sns.reset_defaults()
sns.set_context(context="talk", font_scale=0.7)


def plot_return_levels_deterministic(ds: xr.Dataset):

    
    fig, ax = plt.subplots(figsize=(6,6))

    model = ds.attrs["distribution"].upper()
    inference = ds.attrs["inference"].upper()
    units_levels = ds["return_level"] .attrs["units"]
    units_period = ds["return_period"] .attrs["units"]

    # drop nans
    return_level = ds["return_level"].dropna(dim="return_period")

    ax.plot(
        return_level.return_period, return_level.values, 
        linestyle="--", linewidth=3, color="tab:red",
        label=f"{model} ({inference})",
    )


    ax.set(
        xlabel=f"Return Period [{units_period}]",
        ylabel=f"Return Levels [{units_levels}]",
        xscale="log",
    )

    # SECOND AXIS
    def safe_reciprocal(x):
        """Vectorized 1/x, treating x==0 manually"""
        x = np.array(x, float)
        near_zero = np.isclose(x, 0)
        x[near_zero] = np.inf
        x[~near_zero] = np.reciprocal(x[~near_zero])
        return x

    secax = ax.secondary_xaxis("top", functions=(safe_reciprocal, safe_reciprocal))
    secax.set_xlabel("Probability")
    secax.set_xticks([0.1, 0.01])

    # format log scale labels
    formatter = ScalarFormatter()
    formatter.set_scientific(False)
    ax.xaxis.set_major_formatter(formatter)
    secax.xaxis.set_major_formatter(formatter)

    plt.grid(which="both", visible=True)
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    return fig, ax