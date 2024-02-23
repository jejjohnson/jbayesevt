import autoroot
from pathlib import Path
import typer
from bayesevt._src.models.earth2mip import EARTH2MIP_MODEL_VARIABLES
from bayesevt._src.data.era5.ops import parse_all_variables
from dask.diagnostics import ProgressBar
from bayesevt._src.geoprocessing.physics import CalculateRelativeHumidity
from bayesevt._src.data.era5.variables import VARIABLES_SURFACE
import xarray as xr
from loguru import logger
import time


def download_era5_gcfs(
    save_dir: str="./",
    t0: str="2018-07-20",
    t1: str="2018-08-10",
    ):
    logger.info("Starting script...")
    start_time = time.time()
    # get channels
    logger.info("Loading Variables for Earth2mip Models")
    channels = list(set(EARTH2MIP_MODEL_VARIABLES["pangu"] + EARTH2MIP_MODEL_VARIABLES["fcnv2_sm"]))

    # parse all channel names
    logger.info("Parsing variable names...")
    all_variables = parse_all_variables(channels)
    assert list(map(lambda x: x.name, all_variables)) == channels

    # get surface variables
    vars_surface = set(filter(lambda x: x.name in VARIABLES_SURFACE, all_variables))
    vars_surface = set(map(lambda x: x.era5_name, vars_surface))

    # get pressure variables
    vars_pressure = set(filter(lambda x: x.name not in VARIABLES_SURFACE, all_variables))
    unique_levels = set(map(lambda x: x.level, vars_pressure))
    vars_pressure = set(map(lambda x: x.era5_name, vars_pressure))

    # concatenate all variables
    vars_all = list(vars_surface) + list(vars_pressure)

    # LOADING CLOUD DATA
    logger.info("Load GCFS Data...")
    cloud_dir = "gs://gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3"
    ds = xr.open_zarr(cloud_dir)

    # Remove Relative Humidty (it's not there)
    ivars = list(filter(lambda x: x != "relative_humidity", vars_all))

    logger.info("Starting Preprocessing...")
    with ProgressBar():
        # subset variables
        logger.info("I - Subset Variables...")
        ds = ds[ivars]
        # select event
        logger.info("II - Selecting Events...")
        ds = ds.sel(time=slice(t0, t1))
        # select levels
        logger.info("III - Selecting Levels...")
        ds = ds.sel(level=list(unique_levels)).compute()
        # resample to 1D
        logger.info("IV - Resampling...")
        ds = ds.resample(time="1D").mean()
        # run parallel computation
        logger.info("Running Parallel Computation...")
        ds = ds.compute()

    logger.info("Calculating Relative Humidity...")
    ds["relative_humidity"] = CalculateRelativeHumidity().calculate(ds)

    logger.info("Saving...")
    time_name = str(t0).replace("-", "") + "_" + str(t1).replace("-", "")
    save_name = Path(save_dir).joinpath(f"reanalysis_gcfs_{time_name}.nc")
    ds.to_netcdf(save_name)
    logger.info("Finished script!")
    end_time = time.time() - start_time
    logger.info(f"Time Taken: {end_time:.5f} [secs]")
            

if __name__ == '__main__':
    typer.run(download_era5_gcfs)