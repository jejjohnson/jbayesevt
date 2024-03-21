import numpy as np


# SECOND AXIS
def safe_reciprocal(x):
    """
    Vectorized 1/x, treating x==0 manually.

    Parameters:
    - x: Input array or scalar.

    Returns:
    - Array or scalar with reciprocal values of x. If x is 0, returns infinity.

    """
    x = np.array(x, float)
    near_zero = np.isclose(x, 0)
    x[near_zero] = np.inf
    x[~near_zero] = np.reciprocal(x[~near_zero])
    return x
