from dataclasses import dataclass, field
from typing import Union, Tuple


# codes database: https://codes.ecmwf.int/grib/param-db/?filter=grib2

@dataclass(eq=True, order=True, frozen=True)
class VariableSingleLevel:

    @property
    def dataset(self):
        """
        Gets the dataset name.

        Returns:
            str: The dataset name.
        """
        return "reanalysis-era5-single-levels"
    
    @property
    def product(self):
        """
        Gets the product name.

        Returns:
            str: The product name.
        """
        return "reanalysis"
    

@dataclass(eq=True, order=True, frozen=True)
class VariablePressureLevel:

    @property
    def name(self):
        return f"{self.short_name}{self.level}"

    @property
    def dataset(self):
        """
        Gets the dataset name.

        Returns:
            str: The dataset name.
        """
        return "reanalysis-era5-pressure-levels"
    
    @property
    def product(self):
        """
        Gets the product name.

        Returns:
            str: The product name.
        """
        return "reanalysis"


@dataclass(eq=True, order=True, frozen=True)
class Temperature2m(VariableSingleLevel):
    name: str = "t2m"
    short_name: str = "t2m"
    long_name: str = "2m Temperature"
    era5_name: str = "2m_temperature"
    ecmwf_gid: int = 167
    cmip_name: str = ""
    units: str = "K"


@dataclass(eq=True, order=True, frozen=True)
class UWind10m(VariableSingleLevel):
    name: str = "u10m"
    short_name: str = "u10"
    long_name: str = "10m U Component of Wind"
    era5_name: str = "10m_u_component_of_wind"
    ecmwf_gid: int = 165
    cmip_name: str = "uas"
    units: str = "meters / second"


@dataclass(eq=True, order=True, frozen=True)
class UWind100m(VariableSingleLevel):
    name: str = "u100m"
    short_name: str = "u100"
    long_name: str = "100m Component of Wind"
    era5_name: str = "100m_u_component_of_wind"
    ecmwf_gid: int = 228246
    cmip_name: str = ""
    units: str = "meters / second"


@dataclass(eq=True, order=True, frozen=True)
class VWind10m(VariableSingleLevel):
    name: str = "v10m"
    short_name: str = "v10"
    long_name: str = "10 metre V wind component"
    era5_name: str = "10m_v_component_of_wind"
    ecmwf_gid: int = 166
    units: str = "meters / second"


@dataclass(eq=True, order=True, frozen=True)
class VWind100m(VariableSingleLevel):
    name: str = "v100m"
    short_name: str = "v100"
    long_name: str = "100m V Component of Wind"
    era5_name: str = "100m_v_component_of_wind"
    ecmwf_gid: int = 228247
    cmip_name: str = ""
    units: str = "meters / second"


@dataclass(eq=True, order=True, frozen=True)
class SurfacePressure(VariableSingleLevel):
    name: str = "sp"
    short_name: str = "sp"
    long_name: str = "Surface Pressure"
    era5_name: str = "surface_pressure"
    standard_name: str = "surface_air_pressure"
    ecmwf_gid: int = 134
    cmip_name: str = ""
    units: str = "Pa"


@dataclass(eq=True, order=True, frozen=True)
class TotalColumnWaterVapour(VariableSingleLevel):
    name: str = "tcwv"
    short_name: str = "tcwv"
    long_name: str = "Total column vertically-integrated water vapour"
    era5_name: str = "total_column_water_vapour"
    ecmwf_gid: int = 137
    cmip_name: str = ""
    units: str = "kg / m**2"


@dataclass(eq=True, order=True, frozen=True)
class MeanSeaLevelPressure(VariableSingleLevel):
    name: str = "msl"
    short_name: str = "msl"
    long_name: str = "Mean Sea Level Pressure"
    era5_name: str = "mean_sea_level_pressure"
    standard_name: str = "air_pressure_at_mean_sea_level"
    ecmwf_gid: int = 151
    cmip_name: str = ""
    units: str = "Pa"


@dataclass(eq=True, order=True, frozen=True)
class TotalPrecipitation(VariableSingleLevel):
    name: str = "tp"
    short_name: str = "tp"
    long_name: str = "Total Precipitation"
    era5_name: str = "total_precipitation"
    standard_name: str = "total_precipitation"
    ecmwf_gid: int = 228
    cmip_name: str = ""
    units: str = "m"


@dataclass(eq=True, order=True, frozen=True)
class TotalPrecipitation06(VariableSingleLevel):
    name: str = "tp06"
    short_name: str = "tp06"
    long_name: str = "Total Precipitation 6Hr"
    era5_name: str = "total_precipitation"
    standard_name: str = "total_precipitation"
    ecmwf_gid: int = 260267
    cmip_name: str = ""
    units: str = "m"


@dataclass(eq=True, order=True, frozen=True)
class WindU(VariablePressureLevel):
    short_name: str = "u"
    long_name: str = "U Component of Wind"
    era5_name: str = "u_component_of_wind"
    standard_name: str = "eastward_wind"
    ecmwf_gid: int = 131
    cmip_name: str = ""
    level: int = 500
    units: str = "meters / second"


@dataclass(eq=True, order=True, frozen=True)
class WindV(VariablePressureLevel):
    short_name: str = "v"
    long_name: str = "V Component of Wind"
    era5_name: str = "v_component_of_wind"
    standard_name: str = "northward_wind"
    ecmwf_gid: int = 132
    cmip_name: str = ""
    level: int = 500
    units: str = "meters / second"




@dataclass(eq=True, order=True, frozen=True)
class Temperature(VariablePressureLevel):
    short_name: str = "t"
    long_name: str = "Temperature"
    era5_name: str = "temperature"
    standard_name: str = "air_temperature"
    ecmwf_gid: int = 130
    cmip_name: str = ""
    level: int = 500
    units: str = "K"


@dataclass(eq=True, order=True, frozen=True)
class Geopotential(VariablePressureLevel):
    short_name: str = "z"
    long_name: str = "Geopotential"
    era5_name: str = "geopotential"
    standard_name: str = "geopotential"
    ecmwf_gid: int = 129
    cmip_name: str = ""
    level: int = 500
    units: str = "meters ** 2 / second ** 2"


@dataclass(eq=True, order=True, frozen=True)
class RelativeHumidty(VariablePressureLevel):
    short_name: str = "r"
    long_name: str = "Relative Humidity"
    era5_name: str = "relative_humidity"
    standard_name: str = "relative_humidity"
    ecmwf_gid: int = 157
    cmip_name: str = ""
    level: int = 500
    units: str = ""


@dataclass(eq=True, order=True, frozen=True)
class SpecificHumidty(VariablePressureLevel):
    short_name: str = "q"
    long_name: str = "Specific Humidity"
    era5_name: str = "specific_humidity"
    standard_name: str = "specific_humidity"
    ecmwf_gid: int = 133
    cmip_name: str = ""
    level: int = 500
    units: str = "kg / kg ** 1"



SINGLE_LEVEL_NAMES = {
    "z": Geopotential, # z, geopotential
    "u": WindU, # u, u component of wind
    "v": WindV, # v, v component of wind
    # "w": 135, # w = dp/dt, normally called omega
    "t": Temperature, # t,  temperature
    "q": SpecificHumidty,
    "r": RelativeHumidty, # relative humidity
    
    ###############
    # SURFACE
    ###############
    "t2m": Temperature2m,
    "u10m": UWind10m, # 10u, 10m u component of wind
    "v10m": VWind10m, # 10v, 10m v component of wind
    "u100m": UWind100m, # 100u, 100m u component of wind
    "v100m": VWind100m, # 100v, 100m v component of wind
    "tcwv": TotalColumnWaterVapour, # tcwv, total column vertically-integrated water vapour
    "sp": SurfacePressure, # sp, surface pressure
    "msl": MeanSeaLevelPressure,
    "tp": TotalPrecipitation, # total precip
    "tp06": TotalPrecipitation06, # total precip accumlated over 6 hours
    # "tisr": 212,
    # "zs": 162051,
    # "lsm": 172,
}


VARIABLE_NAMES = {
    "z": Geopotential, # z, geopotential
    "u": WindU, # u, u component of wind
    "v": WindV, # v, v component of wind
    # "w": 135, # w = dp/dt, normally called omega
    "t": Temperature, # t,  temperature
    "q": SpecificHumidty,
    "r": RelativeHumidty, # relative humidity
    ###############
    # SURFACE
    ###############
    "t2m": Temperature2m,
    "u10m": UWind10m, # 10u, 10m u component of wind
    "v10m": VWind10m, # 10v, 10m v component of wind
    "u100m": UWind100m, # 100u, 100m u component of wind
    "v100m": VWind100m, # 100v, 100m v component of wind
    "tcwv": TotalColumnWaterVapour, # tcwv, total column vertically-integrated water vapour
    "sp": SurfacePressure, # sp, surface pressure
    "msl": MeanSeaLevelPressure,
    "tp": TotalPrecipitation, # total precip
    "tp06": TotalPrecipitation06, # total precip accumlated over 6 hours
    # "tisr": 212,
    # "zs": 162051,
    # "lsm": 172,
}

VARIABLES_SURFACE = [
    "t2m",
    "u10m", # 10u, 10m u component of wind
    "v10m", # 10v, 10m v component of wind
    "u100m", # 100u, 100m u component of wind
    "v100m", # 100v, 100m v component of wind
    "tcwv", # tcwv, total column vertically-integrated water vapour
    "sp", # sp, surface pressure
    "msl",
    "tp", # total precip
    "tp06", # total precip accumlated over 6 hours
    # "tisr": 212,
    # "zs": 162051,
    # "lsm": 172,
]


VARIABLE_CODES = {
    129: Geopotential, # z, geopotential
    131: WindU, # u, u component of wind
    132: WindV, # v, v component of wind
    # 135: "w" , # w = dp/dt, normally called omega
    130: Temperature, # t, 2m temperature
    133: SpecificHumidty,
    157: RelativeHumidty, # relative humidity
    167: Temperature2m,
    165: UWind10m, # 10u, 10m u component of wind
    166: VWind10m, # 10v, 10m v component of wind
    228246: UWind100m, # 100u, 100m u component of wind
    228247: VWind100m, # 100v, 100m v component of wind
    137: TotalColumnWaterVapour, # tcwv, total column vertically-integrated water vapour
    134: SurfacePressure, # sp, surface pressure
    151: MeanSeaLevelPressure,
    228: TotalPrecipitation, # total precip
    260267: TotalPrecipitation06, # total precip accumlated over 6 hours
    # 212: "tisr" ,
    # 162051: "zs" ,
    # 172: "lsm" ,
}










