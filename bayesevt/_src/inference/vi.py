from typing import Callable, Optional
import jax.random as jrandom
import numpyro
from numpyro.infer import Predictive, SVI, Trace_ELBO



def run_inference_svi(
        model: Callable, 
        guide: Callable,
        optimizer,
        num_samples: int=1,
        num_steps: int=10_000,
        loss = Trace_ELBO(),
        rng_key= jrandom.PRNGKey(123),
        *args, **kwargs
    ):

    # initialize svi inference
    svi = SVI(model=model, guide=guide, optim=optimizer, loss=loss)

    svi_result = svi.run(rng_key=rng_key, num_steps=num_steps, *args, **kwargs)
    
    return svi_result