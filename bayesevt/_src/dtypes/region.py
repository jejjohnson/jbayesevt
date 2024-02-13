from dataclasses import dataclass


@dataclass
class Region:
    lon_min: float
    lon_max: float
    lat_min: float
    lat_max: float

    @property
    def bbox_cdsapi(self):
        return (self.lat_max, self.lon_min, self.lat_min, self.lon_max)


GLOBE = Region(lon_min=-180, lon_max=180, lat_min=-90, lat_max=90)
# TODO - Spain Region
# TODO - Europe Region
# TODO - USA Region