# modules/member3_market_vendor/company_engine.py
# ==============================================================
# MODULE 7 — COMPANY CATEGORIZATION ENGINE
# Owner  : Member 3
# Status : COMPLETE
# --------------------------------------------------------------
# PURPOSE:
#   Map the recommended crop and required inputs (fertilizer,
#   pesticide) to specific company categories.
# ==============================================================

from utils.console_formatter import print_section, print_field, print_success


class CompanyEngine:
    """
    Categorizes companies by type and maps them to the farmer's needs.
    """

    def __init__(self, vendor_dataset):
        # Store the full vendor/company dataset
        self.vendor_dataset = vendor_dataset

    def categorize(self, crop_name, fertilizer_company, pesticide_company):
        """
        Groups relevant companies by category.
        Returns a dict with category → company name mapping.
        """
        result = {}

        # Fertilizer and Pesticide companies come directly
        # from Module 5 and Module 6 outputs
        result["Fertilizer Company"] = fertilizer_company
        result["Pesticide Company"]  = pesticide_company

        # Find Seed Supplier from vendor dataset
        seed_company = "Not Available"
        for vendor in self.vendor_dataset:
            if vendor["category"] == "Seed Supplier":
                seed_company = vendor["vendor_name"]
                break    # take the first match
        result["Seed Company"] = seed_company

        # Find Crop Buyer from vendor dataset
        buyer = "Not Available"
        for vendor in self.vendor_dataset:
            if vendor["category"] == "Crop Buyer":
                buyer = vendor["vendor_name"]
                break
        result["Crop Buyer"] = buyer

        return result

    def display_companies(self, companies):
        """
        Prints the categorized company recommendations.
        """
        print_section("COMPANY RECOMMENDATIONS")

        # Loop through the dict and print each category
        for category, company in companies.items():
            print_field(category, company)

        print_success("Company recommendations generated.")