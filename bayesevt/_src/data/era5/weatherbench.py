from dataclasses import dataclass


@dataclass
class WeatherBenchERA5:
    base_path: str = "gs://weatherbench2/datasets/era5/"
    era5_1h_025: str = "1959-2023_01_10-full_37-1h-0p25deg-chunk-1.zarr"
    era5_6h_025_derived: str = "1959-2023_01_10-wb13-6h-1440x721_with_derived_variables.zarr"
    era5_6h_150: str = "1959-2023_01_10-6h-240x121_equiangular_with_poles_conservative.zarr"
    era5_6h_526: str = "1959-2023_01_10-6h-64x32_equiangular_conservative.zarr"


@dataclass
class WeatherBenchClimatology:
    base_path: str = "gs://weatherbench2/datasets/era5/"
    clim_6h_025: str = "era5-hourly-climatology/1990-2017_6h_1440x721.zarr"