from utils.console_formatter import print_section, print_field, print_success

class RiskAssessment:
    def calculate(self, profile, crop_recommendation, total_cost):
        if profile.water_availability == "Low":
            water_risk = 30
        elif profile.water_availability == "Medium":
            water_risk = 15
        else:
            water_risk = 0

        mismatch    = 100 - crop_recommendation.suitability_score
        market_risk = (mismatch / 100) * 40

        budget_coverage = (profile.budget / total_cost * 100) if total_cost > 0 else 100
        if budget_coverage < 50:
            budget_risk = 30
        elif budget_coverage < 100:
            budget_risk = 15
        else:
            budget_risk = 0

        overall = min(round(water_risk + market_risk + budget_risk, 1), 100)
        return {"water_risk": round(water_risk, 1), "market_risk": round(market_risk, 1),
                "budget_risk": round(budget_risk, 1), "overall_risk": overall,
                "risk_label": self._risk_label(overall)}

    def _risk_label(self, score):
        if score <= 30:   return "Low Risk"
        elif score <= 60: return "Moderate Risk"
        else:             return "High Risk"

    def display_risk(self, risk_result):
        print_section("RISK ASSESSMENT")
        print_field("Water Risk",        f"{risk_result['water_risk']}/30 points")
        print_field("Market Risk",       f"{risk_result['market_risk']:.1f}/40 points")
        print_field("Budget Risk",       f"{risk_result['budget_risk']}/30 points")
        print()
        print_field("Overall Risk Score", f"{risk_result['overall_risk']}%")
        print_field("Risk Level",         risk_result["risk_label"])
        print_success("Risk assessment complete.")
    def display_risk(self, risk_result):
        print_section("RISK ASSESSMENT")
        print_field("Water Risk",        f"{risk_result['water_risk']}/30 points")
        print_field("Market Risk",       f"{risk_result['market_risk']:.1f}/40 points")
        print_field("Budget Risk",       f"{risk_result['budget_risk']}/30 points")
        print()
        print_field("Overall Risk Score", f"{risk_result['overall_risk']}%")
        print_field("Risk Level",         risk_result["risk_label"])

    # NEW — Budget warning if farmer's budget covers less than 10% of cost
        if risk_result["budget_risk"] >= 30:
            print()
            print("  [!] WARNING: Your budget covers less than 50% of total cost.")
            print("  [i] Apply for a loan BEFORE committing to this crop plan.")

        print_success("Risk assessment complete.")