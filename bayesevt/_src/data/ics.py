from dataclasses import dataclass
import datetime
from typing import List
from earth2mip.grid import LatLonGrid, equiangular_lat_lon_grid
from bayesevt._src.data.grib import load_grib_dataset
from bayesevt._src.data.era5.ops import parse_all_variables
import xarray as xr


@dataclass
class LocalDataSource:
    channel_names: List[str]
    file_paths: List[str]

    @property
    def time_means(self):
        raise NotImplementedError()

    @property
    def grid(self) -> LatLonGrid:
        return equiangular_lat_lon_grid(721, 1440)

    def __getitem__(self, time: datetime.datetime) -> xr.Dataset:
        # 1) create codes
        channel_codes = parse_all_variables(self.channel_names)
        # 2) load data based on codes
        ds: xr.Dataset = load_grib_dataset(files=self.file_paths, codes=channel_codes)
        ds = ds.assign_coords(channel=self.channel_names)
        # 3) do post processing
        # - assign time as initial condition
        ds = ds.assign_coords(time=time)
        # - create consistent datastructure
        ds = ds.transpose("channel", "lat", "lon")
        # - correct lon coordinate between 0 and 360
        ds = ds.assign_coords(lon=ds["lon"] + 180.0)
        ds = ds.roll(lon=1440//2)
        return ds