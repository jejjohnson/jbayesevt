from typing import Tuple, Dict, List
from functools import partial
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
    format: str="netcdf"
    
):
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
        format=format
        
    )
    save_format = SAVE_FORMAT[format]
    save_name = f"{product}-{code.name}-{time.year}{time.month}{time.day}-{time.time}-sl{save_format}"
    return dataset, request, save_name


def create_request_single_level_multi(
    codes: List[SingleLevelCode],
    time: Time,
    region: Region = GLOBE,
    grid: Grid = RES025,
    format: str="netcdf"
    
) -> Tuple[str, Dict]:
    # checks
    # _check_consistent_ids(codes)
    f = partial(create_request_single_level, time=time, format=format, region=region, grid=grid)
    list_of_requests = list(map(f, codes))
    datasets, list_of_requests, _ = zip(*list_of_requests)
    product = codes[0].product

    request = joint_requests(list_of_requests)

    save_format = SAVE_FORMAT[format]
    save_name = f"{product}-{time.year}{time.month}{time.day}-{time.time}-sl{save_format}"
    return datasets[0], request, save_name


def create_request_pressure_level(
    code: PressureLevelCode,
    time: Time,
    region: Region = GLOBE,
    grid: Grid = RES025,
    format: str="netcdf"
    
) -> Tuple[str, Dict]:
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
        format=format
        
    )
    save_format = SAVE_FORMAT[format]
    save_name = f"{product}-{code.name}{pressure_level}-{time.year}{time.month}{time.day}-{time.time}-pl{save_format}"
    return dataset, request, save_name


def create_request_pressure_level_multi(
    codes: List[PressureLevelCode],
    time: Time,
    region: Region = GLOBE,
    grid: Grid = RES025,
    format: str="netcdf"
    
) -> Tuple[str, Dict]:
    # checks
    # _check_consistent_ids(codes)
    f = partial(create_request_pressure_level, time=time, format=format, region=region, grid=grid)
    list_of_requests = list(map(f, codes))
    datasets, list_of_requests, _ = zip(*list_of_requests)
    product = codes[0].product

    request = joint_requests(list_of_requests)

    save_format = SAVE_FORMAT[format]
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
) -> None:
    c = cdsapi.Client()
    param = '/'.join([str(x) for x in param])
    c.retrieve('reanalysis-era5-single-levels', {
            'date'    : date,
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
) -> None:
    c = cdsapi.Client()
    param = '/'.join([str(x) for x in param])
    levelist = '/'.join([str(x) for x in levels]),
    c.retrieve('reanalysis-era5-complete', {
        'date'    : date,
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