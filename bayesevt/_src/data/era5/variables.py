from dataclasses import dataclass
from typing import Union, Tuple

# codes database: https://codes.ecmwf.int/grib/param-db/?filter=grib2
SINGLE_LEVEL_TO_ERA5_CODE = {
    "z": 129, # z, geopotential
    "u": 131, # u, u component of wind
    "v": 132, # v, v component of wind
    "w": 135, # w = dp/dt, normally called omega
    "t": 130, # t, 2m temperature
    "q": 133,
    "r": 157, # relative humidity
    "t2m": 167,
    "u10m": 165, # 10u, 10m u component of wind
    "v10m": 166, # 10v, 10m v component of wind
    "u100m": 228246, # 100u, 100m u component of wind
    "v100m": 228247, # 100v, 100m v component of wind
    "tcwv": 137, # tcwv, total column vertically-integrated water vapour
    "sp": 134, # sp, surface pressure
    "msl": 151,
    "tp": 228, # total precip
    "tp06": 260267, # total precip accumlated over 6 hours
    "tisr": 212,
    "zs": 162051,
    "lsm": 172,
}

@dataclass(eq=True, order=True, frozen=True)
class PressureLevelCode:
    id: int
    level: int = 0
    name: str = ""
    @classmethod
    def from_name(cls, name: str):
        var_name, level = _parse_pressure_level_name(name)
        id_ = SINGLE_LEVEL_TO_ERA5_CODE[var_name]
        return PressureLevelCode(id=id_, level=level, name=var_name)

    @property
    def dataset(self):
        return "reanalysis-era5-pressure-levels"
    
    @property
    def product(self):
        return "reanalysis"

@dataclass(eq=True, order=True, frozen=True)
class SingleLevelCode:
    id: int
    name: str = ""
    @classmethod
    def from_name(cls, name: str):
        return SingleLevelCode(id=SINGLE_LEVEL_TO_ERA5_CODE[name], name=name)
    
    @property
    def dataset(self):
        return "reanalysis-era5-single-levels"
    
    @property
    def product(self):
        return "reanalysis"



def _parse_pressure_level_name(name: str) -> Tuple[str, int]:
    var_name: str = name[0]
    pressure_level: int = int(name[1:])
    return var_name, pressure_level

@dataclass
class UWind10m:
    name: "10u"
    full_name: "10m Component of Wind"
    era5_name: "10m_u_component_of_wind"
    ecmwf_code: 165
    cmip_name: "uas"