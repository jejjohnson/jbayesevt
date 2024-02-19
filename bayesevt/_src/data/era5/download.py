from typing import Tuple, Dict, List
from functools import partial
import cdsapi
from bayesevt._src.dtypes.grid import Grid, RES025
from bayesevt._src.dtypes.region import Region, GLOBE
from bayesevt._src.dtypes.time import Time
from bayesevt._src.data.era5.variables import SingleLevelCode, PressureLevelCode
from bayesevt._src.data.era5.ops import joint_requests

ERA5_PARAM_CODES_SURFACE_FOURCASTNET = [
    165, # 10u, 10m u component of wind
    166, # 10v, 10m v component of wind
    167, # 2t, temperature
    134, # sp, surface pressure
    151, # msl, mean sea level pressure
    137, # tcwv, total column vertically-integrated water vapour
    228246, # 100u, 100m u component of wind
    228247, # 100v, 100m v component of wind
]

ERA5_PARAM_CODES_PRESSURE_LEVELS_FOURCASTNET = [
    130, # t, 2m temperature
    131, # u, u component of wind
    132, # v, v component of wind
    129, # z, geopotential
    157, # relative humidity
]


ERA5_LEVELS_FOURCASTNET = [
    1000, 
    925, 
    850, 
    700, 
    600, 
    500, 
    400, 
    300, 
    250, 
    200, 
    150, 
    100, 
    50 
]

SAVE_FORMAT = {
    "grib": ".grib",
    "netcdf": ".nc"
}


def create_request_single_level(
    code: SingleLevelCode, 
    time: Time,
    region: Region = GLOBE,
    grid: Grid = RES025,
    save_format: str="netcdf"
    
):
    """Create a request for downloading ERA5 data for a single level.

    Args:
        code (SingleLevelCode): The code representing the dataset and product.
        time (Time): The time for which the data is requested.
        region (Region, optional): The region for which the data is requested. Defaults to GLOBE.
        grid (Grid, optional): The grid for which the data is requested. Defaults to RES025.
        save_format (str, optional): The format in which the data will be saved. Defaults to "netcdf".

    Returns:
        tuple: A tuple containing the dataset, request, and save name.
    """
    # extract code specifics
    dataset = code.dataset
    product = code.product

    # create request
    request = dict(
        product_type=product,
        year=[str(time.year)],
        month=[str(time.month)],
        day=[str(time.day)],
        param=[str(code.id)],
        time=[str(time.time)],
        area=region.bbox_cdsapi,
        grid=grid.bbox_cdsapi,
        format=save_format
        
    )
    save_format = SAVE_FORMAT[save_format]
    save_name = f"{product}-{code.name}-{time.year}{time.month}{time.day}-{time.time}-sl{save_format}"
    return dataset, request, save_name


from typing import List, Tuple, Dict

def create_request_single_level_multi(
    codes: List[SingleLevelCode],
    time: Time,
    region: Region = GLOBE,
    grid: Grid = RES025,
    save_format: str="netcdf"
) -> Tuple[str, Dict]:
    """
    Creates a request for downloading multiple single-level codes from ERA5 dataset.

    Args:
        codes (List[SingleLevelCode]): List of single-level codes to download.
        time (Time): Time specification for the data.
        region (Region, optional): Region specification for the data. Defaults to GLOBE.
        grid (Grid, optional): Grid specification for the data. Defaults to RES025.
        save_format (str, optional): Save format for the downloaded data. Defaults to "netcdf".

    Returns:
        Tuple[str, Dict]: A tuple containing the dataset name, request dictionary, and save name.
    """
    # checks
    # _check_consistent_ids(codes)
    f = partial(create_request_single_level, time=time, save_format=save_format, region=region, grid=grid)
    list_of_requests = list(map(f, codes))
    datasets, list_of_requests, _ = zip(*list_of_requests)
    product = codes[0].product

    request = joint_requests(list_of_requests)

    save_format = SAVE_FORMAT[save_format]
    save_name = f"{product}-{time.year}{time.month}{time.day}-{time.time}-sl{save_format}"
    return datasets[0], request, save_name


def create_request_pressure_level(
    code: PressureLevelCode,
    time: Time,
    region: Region = GLOBE,
    grid: Grid = RES025,
    save_format: str="netcdf"
    
) -> Tuple[str, Dict]:
    """
    Create a request for downloading ERA5 data for a specific pressure level.

    Args:
        code (PressureLevelCode): The code representing the pressure level.
        time (Time): The time for which the data is requested.
        region (Region, optional): The region for which the data is requested. Defaults to GLOBE.
        grid (Grid, optional): The grid resolution for the data. Defaults to RES025.
        save_format (str, optional): The format in which the data will be saved. Defaults to "netcdf".

    Returns:
        Tuple[str, Dict]: A tuple containing the dataset, request, and save name.

    """
    # # checks
    # _check_consistent_ids(codes)
    
    # extract code specifics
    dataset = code.dataset
    product = code.product
    param = str(code.id)
    pressure_level = code.level
    # extract levels
    # pressure_level = sorted(list(map(lambda x: x.level, codes)))

    # create request
    request = dict(
        product_type=product,
        year=[str(time.year)],
        month=[str(time.month)],
        day=[str(time.day)],
        param=[str(param)],
        pressure_level=[int(pressure_level)],
        time=[str(time.time)],
        area=region.bbox_cdsapi,
        grid=grid.bbox_cdsapi,
        format=save_format
        
    )
    save_format = SAVE_FORMAT[save_format]
    save_name = f"{product}-{code.name}{pressure_level}-{time.year}{time.month}{time.day}-{time.time}-pl{save_format}"
    return dataset, request, save_name


from typing import List, Tuple, Dict

def create_request_pressure_level_multi(
    codes: List[PressureLevelCode],
    time: Time,
    region: Region = GLOBE,
    grid: Grid = RES025,
    save_format: str="netcdf"
) -> Tuple[str, Dict]:
    """
    Creates a request for multiple pressure levels.

    Args:
        codes (List[PressureLevelCode]): List of pressure level codes.
        time (Time): Time for the request.
        region (Region, optional): Region for the request. Defaults to GLOBE.
        grid (Grid, optional): Grid for the request. Defaults to RES025.
        save_format (str, optional): Save format for the request. Defaults to "netcdf".

    Returns:
        Tuple[str, Dict]: A tuple containing the dataset, request, and save name.
    """
    # checks
    # _check_consistent_ids(codes)
    f = partial(create_request_pressure_level, time=time, save_format=save_format, region=region, grid=grid)
    list_of_requests = list(map(f, codes))
    datasets, list_of_requests, _ = zip(*list_of_requests)
    product = codes[0].product

    request = joint_requests(list_of_requests)
    save_format = SAVE_FORMAT[save_format]
    save_name = f"{product}-{time.year}{time.month}{time.day}-{time.time}-pl{save_format}"
    return datasets[0], request, save_name

def _check_consistent_ids(pl_codes: list) -> None:
    ids = set(list(map(lambda x: x.id, pl_codes)))
    assert len(ids) == 1
    


def download_era5_surface_cdsapi(
    param: list[int],
    date_str: str="2021-08-01",
    time: str="00:00",
    grid: str="0.25/0.25",
    model: str="model",
    save_dir: str="./"
) -> None:
    """
    Downloads ERA5 surface data using the CDS API.

    Args:
        param (list[int]): List of parameter codes to download.
        date_str (str, optional): Date in the format 'YYYY-MM-DD'. Defaults to "2021-08-01".
        time (str, optional): Time in the format 'HH:MM'. Defaults to "00:00".
        grid (str, optional): Grid resolution in the format 'lat/lon'. Defaults to "0.25/0.25".
        model (str, optional): Model name. Defaults to "model".
        save_dir (str, optional): Directory to save the downloaded file. Defaults to "./".

    Returns:
        None
    """
    c = cdsapi.Client()
    param = '/'.join([str(x) for x in param])
    c.retrieve('reanalysis-era5-single-levels', {
            'date'    : date_str,
            'product_type': 'reanalysis',
            'param'   : param,
            'time'    : time, 
            'grid'    : grid,               
            'format'  : 'netcdf',                
        }, f'{save_dir}/surface_{model}.netcdf') 
    return None


def download_era5_pressure_levels_cdsapi(
    param: list[int],
    levels: list[int],
    date_str: str="2021-08-01",
    time: str="00:00",
    grid: str="0.25/0.25",
    model: str="model",
    save_dir: str="./"
) -> None:
    """
    Downloads ERA5 pressure level data using the CDS API.

    Args:
        param (list[int]): List of parameter codes.
        levels (list[int]): List of pressure levels.
        date_str (str, optional): Date string in the format "YYYY-MM-DD". Defaults to "2021-08-01".
        time (str, optional): Time string in the format "HH:MM". Defaults to "00:00".
        grid (str, optional): Grid resolution string in the format "lat/lon". Defaults to "0.25/0.25".
        model (str, optional): Model name. Defaults to "model".
        save_dir (str, optional): Directory to save the downloaded file. Defaults to "./".

    Returns:
        None
    """
    c = cdsapi.Client()
    param = '/'.join([str(x) for x in param])
    levelist = '/'.join([str(x) for x in levels]),
    c.retrieve('reanalysis-era5-complete', {
        'date'    : date_str,
        'levelist': levelist,
        'levtype' : 'pl',
        'param'   : param,
        'stream'  : 'oper',
        'time'    : time, 
        'type'    : 'an',
        'grid'    : grid,               
        'format'  : 'netcdf',                 
        }, f'{save_dir}/surface_{model}.netcdf') 
    return None