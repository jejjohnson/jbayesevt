from dataclasses import dataclass
import xarray as xr
import numpy as np


@dataclass
class CalculateRelativeHumidity:
    """Taken from WeatherBench2
    https://github.com/google-research/weatherbench2/blob/main/weatherbench2/derived_variables.py#L434
    """
    temperature_name: str = "temperature"
    specific_humidity_name: str = "specific_humidity"
    pressure_name: str = "level"

    def calculate(self, dataset: xr.Dataset) -> xr.DataArray:
        # We use the same formula as MetPy's
        # relative_humidity_from_specific_humidity.
        #
        # For saturation vapor pressure, we use the formula for Bolton 1980
        # (https://doi.org/10.1175/1520-0493(1980)108<1046:TCOEPT>2.0.CO;2) for T
        # in degrees Celsius:
        #   6.112 e^\frac{17.67T}{T + 243.5}
        # We assume pressure has units of hPa and temperature has units of Kelvin.
        temperature = dataset[self.temperature_name]
        specific_humidity = dataset[self.specific_humidity_name]
        pressure = dataset.coords[self.pressure_name]
        svp = 6.112 * np.exp(17.67 * (temperature - 273.15) / (temperature - 29.65))
        mixing_ratio = specific_humidity / (1 - specific_humidity)
        saturation_mixing_ratio = 0.622 * svp / (pressure - svp)
        return mixing_ratio / saturation_mixing_ratio
