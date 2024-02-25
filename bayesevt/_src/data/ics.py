from dataclasses import dataclass
import datetime
from typing import List
from earth2mip.grid import LatLonGrid, equiangular_lat_lon_grid
from bayesevt._src.data.grib import load_grib_dataset
from bayesevt._src.data.netcdf import extract_codes_from_xarray
from bayesevt._src.data.era5.ops import parse_all_variables
import xarray as xr


@dataclass
class InMemoryDataSourceXArray:
    """
    A class representing a local data source using xarray for accessing and manipulating data.

    Attributes:
        channel_names (List[str]): List of channel names.
        file_paths (List[str]): List of file paths.
        pressure_name (str): Name of the pressure variable.
        name_convention (str): Name convention for the data.
        engine (str): Engine used for opening the files.

    Methods:
        time_means: Property representing the time means.
        grid: Property representing the grid.
        __getitem__: Method for accessing data based on a specific time.

    """

    channel_names: List[str]
    ds: xr.Dataset
    pressure_name: str = "level"
    name_convention: str = "era5_name"

    @property
    def time_means(self):
        raise NotImplementedError()

    @property
    def grid(self) -> LatLonGrid:
        return equiangular_lat_lon_grid(721, 1440)

    def __getitem__(self, time: datetime.datetime) -> xr.Dataset:
        """
        Get the dataset for a specific time.

        Args:
            time (datetime.datetime): The time for which to retrieve the dataset.

        Returns:
            xr.Dataset: The dataset for the specified time.

        """
        # 1) create codes
        channel_codes = parse_all_variables(self.channel_names)

        # 3) select time coordinate
        try:
            ds = self.ds.sel(time=time, method="nearest")
        except KeyError:
            # no time coordinate
            ds = self.ds

        # 4) extract the codes from xarray
        ds = extract_codes_from_xarray(ds, channel_codes, pressure_name=self.pressure_name, name_convention=self.name_convention)

        # 5) do coordinate validation
        ds = ds.assign_coords(channel=self.channel_names)
        ds = ds.assign_coords(time=time)
        ds = ds.rename(latitude="lat", longitude="lon")

        # 6) do dimension validation
        ds = ds.transpose("channel", "lat", "lon")
        
        # 7) correct lon coordinate between 0 and 360
        ds = ds.assign_coords(lon=ds["lon"] % 360)

        # 8) Sort Coordinates
        ds = ds.sortby("lon")
        ds = ds.sortby("lat", ascending=False)

        return ds


    

@dataclass
class LocalDataSourceXArray:
    """
    A class representing a local data source using xarray for accessing and manipulating data.

    Attributes:
        channel_names (List[str]): List of channel names.
        file_paths (List[str]): List of file paths.
        pressure_name (str): Name of the pressure variable.
        name_convention (str): Name convention for the data.
        engine (str): Engine used for opening the files.

    Methods:
        time_means: Property representing the time means.
        grid: Property representing the grid.
        __getitem__: Method for accessing data based on a specific time.

    """

    channel_names: List[str]
    file_paths: List[str]
    pressure_name: str = "level"
    name_convention: str = "era5_name"
    engine: str = "netcdf"

    @property
    def time_means(self):
        raise NotImplementedError()

    @property
    def grid(self) -> LatLonGrid:
        return equiangular_lat_lon_grid(721, 1440)

    def __getitem__(self, time: datetime.datetime) -> xr.Dataset:
        """
        Get the dataset for a specific time.

        Args:
            time (datetime.datetime): The time for which to retrieve the dataset.

        Returns:
            xr.Dataset: The dataset for the specified time.

        """
        # 1) create codes
        channel_codes = parse_all_variables(self.channel_names)

        # 2) load data based on codes
        ds: xr.Dataset = xr.open_mfdataset(paths=self.file_paths, engine=self.engine, combine="by_coords")

        # 3) select time coordinate
        try:
            ds = ds.sel(time=time, method="nearest")
        except KeyError:
            # no time coordinate
            pass

        # 4) extract the codes from xarray
        ds = extract_codes_from_xarray(ds, channel_codes, pressure_name=self.pressure_name, name_convention=self.name_convention)

        # 5) do coordinate validation
        ds = ds.assign_coords(channel=self.channel_names)
        ds = ds.assign_coords(time=time)
        ds = ds.rename(latitude="lat", longitude="lon")

        # 6) do dimension validation
        ds = ds.transpose("channel", "lat", "lon")
        
        # 7) correct lon coordinate between 0 and 360
        ds = ds.assign_coords(lon=ds["lon"] % 360)

        # 8) Sort Coordinates
        ds = ds.sortby("lon")
        ds = ds.sortby("lat", ascending=False)

        return ds
