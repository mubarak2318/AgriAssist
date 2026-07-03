from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class AdvisoryReport:
    crop: object
    fertilizer_name: str = ""
    fertilizer_company: str = ""
    fertilizer_cost: float = 0.0
    pesticide_name: str = ""
    pesticide_company: str = ""
    pesticide_cost: float = 0.0
    eligible_schemes: List[str] = field(default_factory=list)
    scheme_details: List[Dict] = field(default_factory=list)
    loan_options: List[Dict] = field(default_factory=list)
    risk_score: float = 0.0
    risk_breakdown: Dict = field(default_factory=dict)
    cultivation_cost: float = 0.0
    expected_revenue: float = 0.0
    net_profit: float = 0.0
    best_vendor: Optional[Dict] = None
    market_summary: Optional[Dict] = None
    final_advisory_text: str = ""