from dataclasses import dataclass

@dataclass
class UWind10m:
    name: "10u"
    full_name: "10m Component of Wind"
    era5_name: "10m_u_component_of_wind"
    ecmwf_code: 165
    cmip_name: "uas"