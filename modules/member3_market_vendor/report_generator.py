# modules/member3_market_vendor/report_generator.py
# ==============================================================
# MODULE 12 — REPORT GENERATION MODULE
# Owner  : Member 3
# Status : COMPLETE
# --------------------------------------------------------------
# PURPOSE:
#   Pull together ALL module outputs and print the final
#   Farmer Advisory Report in one clean, readable format.
#   Optionally save as a .txt file.
# ==============================================================

import os
from datetime import datetime
from utils.console_formatter import print_header, print_section, print_field, print_rupees, print_separator


class ReportGenerator:
    """
    Assembles the Final Farmer Advisory Report from all module outputs.
    """

    def generate(self, profile, crop, fertilizer_result, pesticide_result,
                 schemes, loan_result, risk_result, profit_result,
                 company_result=None, vendor_result=None, market_result=None):
        """
        Prints the complete advisory report to the console.
        """
        print_header("FINAL FARMER ADVISORY REPORT")
        print(f"  Generated on: {datetime.now().strftime('%d-%m-%Y  %H:%M')}")

        # ----------------------------------------------------------
        # SECTION 1 — FARMER PROFILE
        # ----------------------------------------------------------
        print_section("FARMER PROFILE")
        print_field("Location",           profile.location)
        print_field("Land Size",          f"{profile.land_size_acres} acres")
        print_field("Soil Type",          profile.soil_type)
        print_field("Water Availability", profile.water_availability)
        print_field("Season",             profile.season)
        print_rupees("Budget",            profile.budget)

        # ----------------------------------------------------------
        # SECTION 2 — CROP RECOMMENDATION
        # ----------------------------------------------------------
        print_section("CROP RECOMMENDATION")
        print_field("Recommended Crop",   crop.crop_name)
        print_field("Suitability Score",  f"{crop.suitability_score}/100")
        print_field("Expected Yield",     f"{crop.expected_yield_kg:,.0f} kg")
        print_field("Market Price",       f"Rs. {crop.avg_market_price_per_kg}/kg")

        if crop.alternatives:
            print(f"\n  {'Alternative Crops':<22}:")
            for alt in crop.alternatives:
                print(f"    • {alt}")

        # ----------------------------------------------------------
        # SECTION 3 — GOVERNMENT SCHEMES
        # ----------------------------------------------------------
        print_section("ELIGIBLE GOVERNMENT SCHEMES")
        if not schemes:
            print("  No eligible schemes found.")
        else:
            for i, scheme in enumerate(schemes, start=1):
                print(f"  {i}. {scheme['scheme_name']}")
                print(f"     Benefit : {scheme['benefit']}")

        # ----------------------------------------------------------
        # SECTION 4 — RECOMMENDED INPUTS
        # ----------------------------------------------------------
        print_section("RECOMMENDED INPUTS")
        print_field("Fertilizer",         fertilizer_result["fertilizer_name"])
        print_field("Fertilizer Company", fertilizer_result["company"])
        print_rupees("Fertilizer Cost",   fertilizer_result["total_cost"])
        print()
        print_field("Pesticide",          pesticide_result["pesticide_name"])
        print_field("Pesticide Company",  pesticide_result["company"])
        print_rupees("Pesticide Cost",    pesticide_result["total_cost"])

        # ----------------------------------------------------------
        # SECTION 5 — COMPANY & VENDOR (Member 3)
        # ----------------------------------------------------------
        if company_result:
            print_section("COMPANY RECOMMENDATIONS")
            for category, company in company_result.items():
                print_field(category, company)

        if vendor_result:
            print_section("BEST VENDOR")
            print_field("Vendor Name",   vendor_result["vendor_name"])
            print_field("Location",      vendor_result["location"])
            print_field("Distance",      f"{vendor_result['distance_km']} km")
            print_field("Rating",        f"{vendor_result['rating']} / 5.0")
            print_field("Price Premium", f"+{vendor_result['price_premium_percent']}%")
            print_field("Contact",       vendor_result["contact"])

        # ----------------------------------------------------------
        # SECTION 6 — MARKET INTELLIGENCE (Member 3)
        # ----------------------------------------------------------
        if market_result:
            print_section("MARKET INTELLIGENCE")
            print_field("Market Demand",     market_result["demand"])
            print_field("Base Price",        f"Rs. {market_result['base_price_per_kg']}/kg")
            print_field("Best Time to Sell", market_result["best_selling_month"])
            if market_result["vendor_premium_percent"] > 0:
                print_field("Price With Vendor",
                            f"Rs. {market_result['premium_price_per_kg']}/kg")

        # ----------------------------------------------------------
        # SECTION 7 — FINANCIAL SUMMARY
        # ----------------------------------------------------------
        print_section("FINANCIAL SUMMARY")
        print("  COSTS:")
        print_rupees("  Cultivation Cost",  profit_result["cultivation_cost"])
        print_rupees("  Fertilizer Cost",   profit_result["fertilizer_cost"])
        print_rupees("  Pesticide Cost",    profit_result["pesticide_cost"])
        print_separator()
        print_rupees("  Total Cost",        profit_result["total_cost"])
        print()
        print("  RETURNS:")
        print_rupees("  Expected Revenue",  profit_result["expected_revenue"])
        print_rupees("  Net Profit",        profit_result["net_profit"])
        print_field("  ROI",               f"{profit_result['roi_percent']}%")

        # ----------------------------------------------------------
        # SECTION 8 — RISK ASSESSMENT
        # ----------------------------------------------------------
        print_section("RISK ASSESSMENT")
        print_field("Water Risk",         f"{risk_result['water_risk']}/30")
        print_field("Market Risk",        f"{risk_result['market_risk']:.1f}/40")
        print_field("Budget Risk",        f"{risk_result['budget_risk']}/30")
        print_field("Overall Risk Score", f"{risk_result['overall_risk']}%")
        print_field("Risk Level",         risk_result["risk_label"])

        # ----------------------------------------------------------
        # SECTION 9 — FINAL ADVISORY SENTENCE
        # ----------------------------------------------------------
        print_section("FINAL ADVISORY")
        verdict = "PROFITABLE" if profit_result["is_profitable"] else "NOT PROFITABLE"
        print(f"  Based on your {profile.land_size_acres}-acre {profile.soil_type}")
        print(f"  farm in {profile.location}, {crop.crop_name} is the recommended")
        print(f"  crop this {profile.season} season.")
        print()
        print(f"  Expected Net Profit : Rs. {profit_result['net_profit']:,.0f}")
        print(f"  Overall Verdict     : {verdict}")
        print()
        print("=" * 60)

    def save_report(self, profile, crop, profit_result):
        """
        Saves a summary of the report to storage/saved_reports/ folder.
        """
        # Build the path to the saved_reports folder
        BASE_DIR = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "..")
        )
        save_path = os.path.join(BASE_DIR, "storage", "saved_reports")

        # Create the folder if it doesn't exist
        os.makedirs(save_path, exist_ok=True)

        # Build a filename using location and current timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename  = f"report_{profile.location}_{timestamp}.txt"
        filepath  = os.path.join(save_path, filename)

        # Write a plain text summary to the file
        with open(filepath, "w") as f:
            f.write("=" * 60 + "\n")
            f.write("       AGRIASSIST — FARMER ADVISORY REPORT\n")
            f.write("=" * 60 + "\n")
            f.write(f"Generated   : {datetime.now().strftime('%d-%m-%Y %H:%M')}\n")
            f.write(f"Location    : {profile.location}\n")
            f.write(f"Land Size   : {profile.land_size_acres} acres\n")
            f.write(f"Soil Type   : {profile.soil_type}\n")
            f.write(f"Season      : {profile.season}\n")
            f.write(f"Budget      : Rs. {profile.budget:,.0f}\n")
            f.write("-" * 60 + "\n")
            f.write(f"Recommended Crop : {crop.crop_name}\n")
            f.write(f"Expected Yield   : {crop.expected_yield_kg:,.0f} kg\n")
            f.write(f"Net Profit       : Rs. {profit_result['net_profit']:,.0f}\n")
            f.write(f"ROI              : {profit_result['roi_percent']}%\n")
            f.write(f"Risk Level       : {profit_result['is_profitable'] and 'Profitable' or 'Loss'}\n")
            f.write("=" * 60 + "\n")
            f.write("Generated by AgriAssist\n")

        print(f"  [✓] Report saved to: saved_reports/{filename}")