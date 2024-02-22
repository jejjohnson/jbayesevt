from typing import List, Union
from bayesevt._src.data.era5.variables import VARIABLE_CODES, VariableSingleLevel, VariablePressureLevel
import xarray as xr

def load_netcdf_dataset(dataset: xr.Dataset, codes: List[Union[VariableSingleLevel, VariablePressureLevel]]) -> xr.Dataset:
    ds_new = []
    for ivar in codes:
        # select variable
        if isinstance(ivar, VariableSingleLevel):
            ids = dataset[ivar.era5_name]
        elif isinstance(ivar, VariablePressureLevel):
            ids = dataset[ivar.era5_name].sel(level=ivar.level).drop_vars('level')
            
        ds_new.append(ids.transpose("latitude", "longitude"))    

    ds_new = xr.concat(ds_new, dim="channel")
    return ds_new
