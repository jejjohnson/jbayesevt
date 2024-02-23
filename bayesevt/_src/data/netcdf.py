from typing import List, Union
from bayesevt._src.data.era5.variables import VARIABLE_CODES, VariableSingleLevel, VariablePressureLevel
import xarray as xr

def extract_codes_from_xarray(
        dataset: xr.Dataset, 
        codes: List[Union[VariableSingleLevel, VariablePressureLevel]],
        pressure_name: str="level",
        name_convention: str="era5_name"
        ) -> xr.Dataset:
    ds_new = []

    for ivar in codes:
        # select variable
        if isinstance(ivar, VariableSingleLevel) or isinstance(ivar, VariablePressureLevel):
            if name_convention == "era5_name":
                ids = dataset[ivar.era5_name]
            elif name_convention == "short_name":
                ids = dataset[ivar.short_name]
            else:
                raise ValueError(f"Unrecognized naming convention")
        if isinstance(ivar, VariablePressureLevel):
            ids = ids.sel({pressure_name: ivar.level}).drop_vars(pressure_name)
            
        ds_new.append(ids.transpose("latitude", "longitude"))    

    ds_new = xr.concat(ds_new, dim="channel")
    return ds_new
