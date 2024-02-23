import autoroot
import cdsapi
from pathlib import Path
from loguru import logger
from bayesevt._src.data.era5.ops import parse_single_levels, parse_pressure_levels
from bayesevt._src.models.earth2mip import EARTH2MIP_MODEL_VARIABLES
import typer
from bayesevt._src.dtypes.time import Time
from bayesevt._src.dtypes.grid import RES025
from bayesevt._src.dtypes.region import GLOBE
from bayesevt._src.data.era5.download import (
    create_request_single_level_multi,
    create_request_pressure_level_multi
)
from concurrent.futures import ThreadPoolExecutor, as_completed


def download(
        date: str="2021-08-01",
        save_dir: str="/pool/proyectos/CLINT/sa4attrs/data/raw/",
        save_format: str="netcdf"
):
    """
    Downloads ERA5 data for a specific date and saves it to the specified directory.

    Args:
        date (str, optional): The date in "YYYY-MM-DD" format. Defaults to "2021-08-01".
        save_dir (str, optional): The directory where the downloaded data will be saved. Defaults to "/pool/proyectos/CLINT/sa4attrs/data/raw/".
        save_format (str, optional): The format in which the data will be saved. Defaults to "netcdf".
    """
    logger.info("Getting channels...")
    channels = list(set(EARTH2MIP_MODEL_VARIABLES["pangu"] + EARTH2MIP_MODEL_VARIABLES["fcnv2_sm"]))
    
    time = Time.from_datetime_str(date)

    logger.info("Parsing variables...")
    # parse single level variables
    sl_variables = parse_single_levels(channels)

    # parse pressure level variables
    pl_variables = parse_pressure_levels(channels)

    logger.info("Creating requests for single level...")
    dataset, request, save_name = create_request_single_level_multi(
        sl_variables, 
        time=time,
        region=GLOBE,
        grid=RES025,
        save_format=save_format
        
    )
    params = [(dataset, request, save_name)]

    logger.info("Creating requests for pressure level...")
    dataset, request, save_name = create_request_pressure_level_multi(
        codes=pl_variables, 
        time=time, 
        region=GLOBE,
        grid=RES025,
        save_format=save_format
    )
    params += [(dataset, request, save_name)]

    logger.info("Starting downloader...")
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = []

        c = cdsapi.Client()

        for iparams in params:
            # create save path
            save_path = Path(save_dir).joinpath(iparams[2])
            # do futures
            futures.append(
                executor.submit(c.retrieve, iparams[0], iparams[1], save_path)
            )


            # Wait for all downloads to finish
    logger.info("Waiting for all downloads to finish...")
    for future in as_completed(futures):
        try:
            future.result()
            logger.info("Finished script...Successful!")
        except Exception as e:
            print(f"Error during download: {e}")
            logger.info("Finished script...Failed!")
    
    

            

if __name__ == '__main__':
    typer.run(download)