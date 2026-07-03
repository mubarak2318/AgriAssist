# main.py
# ==============================================================
# AGRIASSIST — SMART FARMER ADVISORY SYSTEM
# Entry Point & Orchestrator
# ==============================================================
# PURPOSE:
#   This is the ONLY file the user runs.
#   It shows the main menu, calls each module in the right order,
#   and passes output from one module into the next.
#
#   EXECUTION ORDER:
#   1. Load all datasets once at startup
#   2. Show main menu
#   3. When user starts a session:
#      Module 1 → Module 2 → Module 5 → Module 6
#                          → Module 3 → Module 4 → Module 10 → Module 11
#                          → Module 7 → Module 8 → Module 9 → Module 12
# ==============================================================

# -------- Standard library imports --------
import sys    # For clean exit

# -------- Utility imports --------
from utils.data_loader import (
    load_crops, load_schemes, load_fertilizers,
    load_pesticides, load_loans, load_vendors, load_market_prices
)
from utils.console_formatter import print_header, print_section, print_info, print_warning
from utils.input_validator import get_choice_input

# -------- Member 1 module imports --------
from modules.member1_crop_intelligence.profile_analyzer import ProfileAnalyzer
from modules.member1_crop_intelligence.crop_engine import CropRecommendationEngine
from modules.member1_crop_intelligence.fertilizer_module import FertilizerModule
from modules.member1_crop_intelligence.pesticide_module import PesticideModule

# -------- Member 2 module imports --------
from modules.member2_finance_gov.scheme_advisor import SchemeAdvisor
from modules.member2_finance_gov.loan_module import LoanModule
from modules.member2_finance_gov.risk_assessment import RiskAssessment
from modules.member2_finance_gov.profit_prediction import ProfitPredictor

# -------- Member 3 module imports (skeleton) --------
from modules.member3_market_vendor.company_engine import CompanyEngine
from modules.member3_market_vendor.vendor_engine import VendorEngine
from modules.member3_market_vendor.market_intelligence import MarketIntelligence
from modules.member3_market_vendor.report_generator import ReportGenerator


# ==============================================================
# DATASET LOADING
# These are loaded once here and passed into each module class.
# This way, modules don't read files themselves — they just
# receive data they need through their __init__ method.
# ==============================================================
def load_all_datasets():
    """
    Loads all JSON datasets from the /data folder.
    Returns them as a single dictionary for easy passing.
    """
    print_info("Loading datasets...")
    datasets = {
        "crops":         load_crops(),
        "schemes":       load_schemes(),
        "fertilizers":   load_fertilizers(),
        "pesticides":    load_pesticides(),
        "loans":         load_loans(),
        "vendors":       load_vendors(),
        "market_prices": load_market_prices()
    }
    print_info(f"Loaded {len(datasets)} datasets successfully.")
    return datasets


# ==============================================================
# SESSION RUNNER
# This function runs one complete advisory session.
# It calls all 12 modules in the correct order,
# passing each module's output as input to the next.
# ==============================================================
def run_advisory_session(datasets):
    """
    Runs one full farmer advisory session from profile input to final report.

    :param datasets: dict of all loaded dataset lists
    """
    print_header("NEW FARMER ADVISORY SESSION")

    # ----------------------------------------------------------
    # MEMBER 1 — CROP INTELLIGENCE
    # ----------------------------------------------------------

    # MODULE 1: Collect farmer profile
    analyzer = ProfileAnalyzer()
    profile = analyzer.collect_profile()
    analyzer.display_profile(profile)

    # MODULE 2: Recommend the best crop
    crop_engine = CropRecommendationEngine(datasets["crops"])
    crop = crop_engine.recommend(profile)
    crop_engine.display_recommendation(crop)

    # MODULE 5: Recommend fertilizer based on crop + soil
    fertilizer_mod = FertilizerModule(datasets["fertilizers"])
    fertilizer_result = fertilizer_mod.recommend(
        crop.crop_name,
        profile.soil_type,
        profile.land_size_acres
    )
    fertilizer_mod.display_recommendation(fertilizer_result)

    # MODULE 6: Recommend pesticide based on crop
    pesticide_mod = PesticideModule(datasets["pesticides"])
    pesticide_result = pesticide_mod.recommend(
        crop.crop_name,
        profile.land_size_acres
    )
    pesticide_mod.display_recommendation(pesticide_result)

    # ----------------------------------------------------------
    # MEMBER 2 — FINANCE & GOVERNMENT
    # ----------------------------------------------------------

    # MODULE 3: Check government scheme eligibility
    scheme_advisor = SchemeAdvisor(datasets["schemes"])
    eligible_schemes = scheme_advisor.check_eligibility(profile)
    scheme_advisor.display_schemes(eligible_schemes)

    # MODULE 11: Calculate profit BEFORE loan so we know the total cost
    # (LoanModule needs total cost to check budget gap)
    profit_predictor = ProfitPredictor()
    profit_result = profit_predictor.calculate(
        profile,
        crop,
        fertilizer_result["total_cost"],
        pesticide_result["total_cost"]
    )
    profit_predictor.display_profit(profit_result)

    # MODULE 4: Loan assistance — uses total cost from profit predictor
    loan_mod = LoanModule(datasets["loans"])
    loan_result = loan_mod.assess(
        profile.budget,
        profit_result["cultivation_cost"],
        fertilizer_result["total_cost"],
        pesticide_result["total_cost"]
    )
    loan_mod.display_loans(loan_result)

    # MODULE 10: Risk assessment — uses crop score + water + budget
    risk_mod = RiskAssessment()
    risk_result = risk_mod.calculate(profile, crop, profit_result["total_cost"])
    risk_mod.display_risk(risk_result)

    # ----------------------------------------------------------
    # MEMBER 3 — MARKET, VENDOR & REPORT (SKELETON)
    # Modules below are skeleton — they return None for now.
    # When Member 3 completes their code, these will return real data.
    # ----------------------------------------------------------

    # MODULE 7: Company categorization
    company_engine = CompanyEngine(datasets["vendors"])
    company_result = company_engine.categorize(
        crop.crop_name,
        fertilizer_result["company"],
        pesticide_result["company"]
    )
    # Only display if Member 3 has implemented it (not None)
    if company_result:
        company_engine.display_companies(company_result)
    else:
        print_warning("Company recommendations: pending (Member 3 module)")

    # MODULE 8: Vendor recommendation
    vendor_engine = VendorEngine(datasets["vendors"])
    vendor_result = vendor_engine.recommend(profile.location, crop.crop_name)
    if vendor_result:
        vendor_engine.display_vendor(vendor_result)
    else:
        print_warning("Vendor recommendation: pending (Member 3 module)")

    # MODULE 9: Market intelligence
    market_mod = MarketIntelligence(datasets["market_prices"])
    market_result = market_mod.get_market_data(crop.crop_name, vendor_result)
    if market_result:
        market_mod.display_market_data(market_result)
    else:
        print_warning("Market intelligence: pending (Member 3 module)")

    # MODULE 12: Final report
    report_gen = ReportGenerator()
    report_gen.generate(
        profile, crop,
        fertilizer_result, pesticide_result,
        eligible_schemes, loan_result,
        risk_result, profit_result,
        company_result, vendor_result, market_result
    )

    # Ask if user wants to save the report
    save = input("\n  Save this report? (Y/N): ").strip().upper()
    if save == "Y":
        report_gen.save_report(profile, crop, profit_result)


# ==============================================================
# MAIN MENU
# Shown every time the program starts or after a session ends.
# ==============================================================
def show_main_menu():
    """
    Displays the main menu and returns the user's choice as a string.
    """
    print_header("AGRIASSIST — SMART FARMER ADVISORY")
    print("  1. Start New Farmer Advisory Session")
    print("  2. About AgriAssist")
    print("  0. Exit")
    print()
    return input("  Enter your choice: ").strip()


def show_about():
    """Prints a brief description of the project."""
    print_section("ABOUT AGRIASSIST")
    print("  AgriAssist is a console-based decision support system")
    print("  designed to help Indian farmers make informed decisions")
    print("  about crop selection, government schemes, fertilizers,")
    print("  pesticides, vendors, and profit estimation.")
    print()
    print("  Built by: Team AgriAssist (3 Members)")
    print("  Platform: Python Console Application")
    print("  Domain  : AgriTech / Decision Support System")


# ==============================================================
# PROGRAM ENTRY POINT
# Python runs this block when you execute: python main.py
# ==============================================================
if __name__ == "__main__":

    # Load all datasets once before the menu loop starts
    try:
        datasets = load_all_datasets()
    except FileNotFoundError as e:
        # If any dataset file is missing, show an error and stop
        print(f"\n[ERROR] Dataset file not found: {e}")
        print("Please make sure all files are present in the /data folder.")
        sys.exit(1)

    # Main menu loop — keeps running until user selects Exit (0)
    while True:
        choice = show_main_menu()

        if choice == "1":
            run_advisory_session(datasets)

        elif choice == "2":
            show_about()

        elif choice == "0":
            print("\n  Thank you for using AgriAssist.\n")
            sys.exit(0)    # Exit the program cleanly

        else:
            # Handle any invalid menu input
            print("\n  [!] Invalid choice. Please enter 1, 2, or 0.")