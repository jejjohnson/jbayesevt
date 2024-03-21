from jaxtyping import Array
from tensorflow_probability.substrates.jax import distributions as tfd


def calculate_returns_gevd(return_period: Array, loc, scale, concentration) -> Array:
    """
    Calculate the return levels using the Generalized Extreme Value (GEV) distribution.

    Args:
        return_period (Array): An array of return periods.
        loc: The location parameter of the GEV distribution.
        scale: The scale parameter of the GEV distribution.
        concentration: The concentration parameter of the GEV distribution.

    Returns:
        Array: An array of return levels corresponding to the given return periods.
    """
    # initialize gevd model
    model = tfd.GeneralizedExtremeValue(loc=loc, scale=scale, concentration=concentration)

    # calculate return levels
    return_level = model.quantile(1-1/return_period)

    return return_level


def calculate_returns_gpd(return_period: Array, loc, scale, concentration) -> Array:
    """
    Calculate the return levels using the Generalized Pareto Distribution (GPD) model.

    Parameters:
    - return_period (Array): An array of return periods.
    - loc (float): The location parameter of the GPD model.
    - scale (float): The scale parameter of the GPD model.
    - concentration (float): The concentration parameter of the GPD model.

    Returns:
    - return_level (float): The calculated return level.

    """
    # initialize gpd model
    model = tfd.GeneralizedPareto(loc=loc, scale=scale, concentration=concentration)

    # calculate return levels
    return_level = model.quantile(1-1/return_period)

    return return_level

