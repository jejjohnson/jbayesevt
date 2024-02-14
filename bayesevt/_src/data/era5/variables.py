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

ERA5_CODE_TO_NAME = {
    129: "z" , # z, geopotential
    131: "u" , # u, u component of wind
    132: "v" , # v, v component of wind
    135: "w" , # w = dp/dt, normally called omega
    130: "t" , # t, 2m temperature
    133: "q" ,
    157: "r" , # relative humidity
    167: "t2m" ,
    165: "u10m" , # 10u, 10m u component of wind
    166: "v10m" , # 10v, 10m v component of wind
    228246: "u100m" , # 100u, 100m u component of wind
    228247: "v100m" , # 100v, 100m v component of wind
    137: "tcwv" , # tcwv, total column vertically-integrated water vapour
    134: "sp" , # sp, surface pressure
    151: "msl" ,
    228: "tp" , # total precip
    260267: "tp06" , # total precip accumlated over 6 hours
    212: "tisr" ,
    162051: "zs" ,
    172: "lsm" ,
}

@dataclass(eq=True, order=True, frozen=True)
class PressureLevelCode:
    id: int
    level: int = 0
    name: str = ""
    var_name: str = ""

    @classmethod
    def from_name(cls, name: str):
        var_name, level = _parse_pressure_level_name(name)
        id_ = SINGLE_LEVEL_TO_ERA5_CODE[var_name]
        return PressureLevelCode(id=id_, level=level, name=var_name, var_name=name)
    
    @classmethod
    def from_id_and_level(cls, id: int, level: int=0):
        name = ERA5_CODE_TO_NAME[id]
        var_name = f"{name}{level}"
        return PressureLevelCode(id=id, level=level, name=name, var_name=var_name)

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
    
    @classmethod
    def from_id(cls, id: str):
        name = ERA5_CODE_TO_NAME[id]
        return SingleLevelCode(id=id, name=name)
    
    @property
    def var_name(self):
        return self.name
    
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