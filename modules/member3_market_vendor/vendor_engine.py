# modules/member3_market_vendor/vendor_engine.py
# ==============================================================
# MODULE 8 — VENDOR RECOMMENDATION ENGINE
# Owner  : Member 3
# Status : COMPLETE
# --------------------------------------------------------------
# PURPOSE:
#   Score and rank all Crop Buyer vendors.
#   Best vendor is chosen based on:
#     Location match  → 40 points
#     Rating          → up to 40 points
#     Price premium   → up to 20 points
# ==============================================================

from utils.console_formatter import (
    print_section, print_field, print_success, print_warning
)


class VendorEngine:
    """
    Scores and ranks vendors/buyers for the farmer's location and crop.
    """

    def __init__(self, vendor_dataset):
        # Store full vendor dataset
        self.vendor_dataset = vendor_dataset

    def recommend(self, location, crop_name):
        """
        Filters Crop Buyers, scores each one, returns the best match.
        """
        # Step 1: Filter — keep only Crop Buyers
        buyers = [
            v for v in self.vendor_dataset
            if v["category"] == "Crop Buyer"
        ]

        # If no buyers found in dataset, return None
        if not buyers:
            return None

        # Step 2: Score each buyer
        scored = []
        for buyer in buyers:
            score = self._score_vendor(buyer, location)
            scored.append((score, buyer))

        # Step 3: Sort by score — highest first
        scored.sort(key=lambda x: x[0], reverse=True)

        # Step 4: Return the top-scoring vendor dict
        return scored[0][1]

    def _score_vendor(self, vendor, farmer_location):
        """
        Calculates a score for one vendor out of 100.
        """
        score = 0

        # Location match gives 40 points
        # .lower() makes comparison case-insensitive
        if vendor["location"].lower() == farmer_location.lower():
            score += 40

        # Rating score: rating is out of 5, scale to 40 points
        # e.g. rating 4.5 → (4.5/5) × 40 = 36 points
        rating_points = (vendor["rating"] / 5) * 40
        score += rating_points

        # Price premium score: higher premium = farmer earns more
        # Find the maximum premium across all vendors to normalise
        all_premiums = [
            v["price_premium_percent"]
            for v in self.vendor_dataset
            if v["category"] == "Crop Buyer"
        ]
        max_premium = max(all_premiums) if all_premiums else 1
        if max_premium == 0:
            max_premium = 1    # avoid division by zero

        premium_points = (vendor["price_premium_percent"] / max_premium) * 20
        score += premium_points

        return score

    def display_vendor(self, vendor):
        """
        Prints the recommended vendor details.
        """
        print_section("BEST VENDOR RECOMMENDATION")

        if vendor is None:
            print_warning("No vendor found for your location.")
            return

        print_field("Vendor Name",    vendor["vendor_name"])
        print_field("Location",       vendor["location"])
        print_field("Distance",       vendor["distance_km"], "km")
        print_field("Rating",         f"{vendor['rating']} / 5.0")
        print_field("Price Premium",  f"+{vendor['price_premium_percent']}%", "above base price")
        print_field("Contact",        vendor["contact"])
        print_success("Vendor recommendation generated.")