# modules/member3_market_vendor/market_intelligence.py
# ==============================================================
# MODULE 9 — MARKET INTELLIGENCE MODULE
# Owner  : Member 3
# Status : COMPLETE
# --------------------------------------------------------------
# PURPOSE:
#   Find market data for the recommended crop.
#   Calculate the price the farmer will actually receive
#   after applying the vendor's price premium.
# ==============================================================

from utils.console_formatter import (
    print_section, print_field, print_success, print_warning
)


class MarketIntelligence:
    """
    Fetches and displays market data for the recommended crop.
    """

    def __init__(self, market_dataset):
        # Store the full market prices dataset
        self.market_dataset = market_dataset

    def get_market_data(self, crop_name, best_vendor=None):
        """
        Finds market data for the crop.
        If a vendor is provided, calculates the premium price too.
        Returns a dict or None if crop not found.
        """
        # Search the dataset for a matching crop name
        market_entry = None
        for entry in self.market_dataset:
            if entry["crop_name"] == crop_name:
                market_entry = entry
                break    # found it, stop searching

        # If crop not found in dataset, return None
        if market_entry is None:
            return None

        # Get base price from the market dataset
        base_price = market_entry["price_per_kg"]

        # Build result dictionary
        result = {
            "crop_name":          crop_name,
            "base_price_per_kg":  base_price,
            "demand":             market_entry["demand"],
            "best_selling_month": market_entry["best_selling_month"],
            "region":             market_entry["region"],
        }

        # If a vendor was found, calculate the premium price
        # Premium means farmer earns MORE than the base market price
        if best_vendor is not None:
            premium = best_vendor["price_premium_percent"]
            # Formula: base_price × (1 + premium/100)
            # e.g. Rs.65 with 10% premium → Rs.65 × 1.10 = Rs.71.5
            premium_price = base_price * (1 + premium / 100)
            result["vendor_premium_percent"]  = premium
            result["premium_price_per_kg"]    = round(premium_price, 2)
        else:
            # No vendor — premium price equals base price
            result["vendor_premium_percent"]  = 0
            result["premium_price_per_kg"]    = base_price

        return result

    def display_market_data(self, market_data):
        """
        Prints the market intelligence summary.
        """
        print_section("MARKET INTELLIGENCE")

        if market_data is None:
            print_warning("Market data not available for this crop.")
            return

        print_field("Crop",             market_data["crop_name"])
        print_field("Region",           market_data["region"])
        print_field("Base Market Price",f"Rs. {market_data['base_price_per_kg']}/kg")
        print_field("Market Demand",    market_data["demand"])
        print_field("Best Time to Sell",market_data["best_selling_month"])

        # Show vendor premium only if it is greater than 0
        if market_data["vendor_premium_percent"] > 0:
            print_field(
                "Vendor Premium",
                f"+{market_data['vendor_premium_percent']}% above market"
            )
            print_field(
                "Price With Vendor",
                f"Rs. {market_data['premium_price_per_kg']}/kg"
            )

        print_success("Market intelligence generated.")