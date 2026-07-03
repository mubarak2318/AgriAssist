from utils.console_formatter import print_section, print_field, print_rupees, print_success, print_separator

class ProfitPredictor:
    def calculate(self, profile, crop_recommendation, fertilizer_cost, pesticide_cost):
        cultivation_cost = crop_recommendation.cultivation_cost_per_acre * profile.land_size_acres
        total_cost       = cultivation_cost + fertilizer_cost + pesticide_cost
        expected_revenue = crop_recommendation.expected_yield_kg * crop_recommendation.avg_market_price_per_kg
        net_profit       = expected_revenue - total_cost
        roi_percent      = round((net_profit / total_cost) * 100, 1) if total_cost > 0 else 0
        return {"cultivation_cost": cultivation_cost, "fertilizer_cost": fertilizer_cost,
                "pesticide_cost": pesticide_cost, "total_cost": total_cost,
                "expected_revenue": expected_revenue, "net_profit": net_profit,
                "roi_percent": roi_percent, "is_profitable": net_profit > 0}

    def display_profit(self, result):
        print_section("PROFIT PREDICTION")
        print("  COSTS:")
        print_rupees("  Cultivation Cost", result["cultivation_cost"])
        print_rupees("  Fertilizer Cost",  result["fertilizer_cost"])
        print_rupees("  Pesticide Cost",   result["pesticide_cost"])
        print_separator()
        print_rupees("  Total Cost",       result["total_cost"])
        print()
        print("  RETURNS:")
        print_rupees("  Expected Revenue", result["expected_revenue"])
        print_rupees("  Net Profit",       result["net_profit"])
        print_field("  ROI",              f"{result['roi_percent']}%")
        print()
        if result["is_profitable"]:
            print("  [✓] VERDICT: This crop plan is PROFITABLE.")
        else:
            print("  [!] VERDICT: This plan may result in a LOSS.")
        print_success("Profit prediction complete.")