from typing import Tuple, List, Union
import eccodes
import numpy as np
from bayesevt._src.data.era5.variables import VARIABLE_CODES, VariableSingleLevel, VariablePressureLevel
import xarray as xr


def extract_grib_vals_and_coords(gid: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    # extract lon/lat coordinates
    nlon = eccodes.codes_get(gid, "Ni")
    nlat = eccodes.codes_get(gid, "Nj")
    lat = eccodes.codes_get_array(gid, "latitudes").reshape(nlat, nlon)
    lon = eccodes.codes_get_array(gid, "longitudes").reshape(nlat, nlon)
    values = eccodes.codes_get_values(gid).reshape(nlat, nlon)
    return lat, lon, values


def extract_grib_params(gid: int) -> Tuple[int, int, str]:
    id_ = eccodes.codes_get(gid, "paramId")
    level = eccodes.codes_get(gid, "level")
    level_type = eccodes.codes_get(gid, "typeOfLevel")
    return id_, level, level_type


def load_grib_dataset(files: List[str], codes: List[Union[VariableSingleLevel, VariablePressureLevel]]) -> xr.Dataset:

    # empty arrays
    arrays = [None] * len(codes)
    for ipath in files:
        with open(ipath) as f:
            while True:
                gid = eccodes.codes_grib_new_from_file(f)
                # logger.debug(f"GID: {gid}")
                
                if gid is None:
                    break
                # extract codes
                id, level, level_type = extract_grib_params(gid)
                # logger.debug(f"ID: {id} | LEVEL: {level} | Type: {level_type}")

                # Create Unique Code to Match List of Variables
                if level_type == "surface":
                    code = VARIABLE_CODES[id]()
                elif level_type == "isobaricInhPa":
                    code = VARIABLE_CODES[id](level=level)

                # check if Unique Code Exists
                try:
                    i = codes.index(code)
                except ValueError:
                    continue
                # extract coordinates and values
                lat, lon, values = extract_grib_vals_and_coords(gid)
                # logger.debug(f"Array SIZE: {values.shape}")
                
                # release codes
                eccodes.codes_release(gid)

                # aggregrate arrays
                arrays[i] = values

    # check all IDs are the same
    msg = f"Number of Variables is not the same as arrays..."
    msg += f"\nNumber of Variables: {len(codes)}"
    msg += f"\nNumber of Arrays: {len(arrays)}"
    assert len(arrays) == len(codes), msg


    # create xarray dataset
    arrays = np.stack(arrays)
    coords = {}
    coords["lon"] = lon[0, :]
    coords["lat"] = lat[:, 0]
    ds = xr.DataArray(arrays, dims=["channel", "lat", "lon"], coords=coords)
    return ds