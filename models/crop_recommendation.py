from dataclasses import dataclass, field
from typing import List

@dataclass
class CropRecommendation:
    crop_name: str
    expected_yield_kg: float
    suitability_score: float
    avg_market_price_per_kg: float
    cultivation_cost_per_acre: float
    alternatives: List[str] = field(default_factory=list)