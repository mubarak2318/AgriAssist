from dataclasses import dataclass
from typing import Optional

@dataclass
class FarmerProfile:
    location: str
    land_size_acres: float
    soil_type: str
    water_availability: str
    season: str
    budget: float
    experience_years: Optional[int] = None