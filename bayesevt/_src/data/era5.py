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