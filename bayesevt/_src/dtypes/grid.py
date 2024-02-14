from dataclasses import dataclass


@dataclass
class Grid:
    dlon: float = 0.25
    dlat: float = 0.25

    @property
    def bbox_cdsapi(self):
        return (self.dlon, self.dlat)


RES025 = Grid(0.25, 0.25)