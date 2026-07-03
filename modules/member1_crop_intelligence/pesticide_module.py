from utils.console_formatter import print_section, print_field, print_rupees, print_success

class PesticideModule:
    def __init__(self, pesticide_dataset):
        self.pesticide_dataset = pesticide_dataset

    def recommend(self, crop_name, land_size_acres):
        candidates = [p for p in self.pesticide_dataset if crop_name in p["suitable_crops"]]
        if not candidates:
            return self._default_pesticide(land_size_acres)
        chemical_matches = [p for p in candidates if p["type"] != "Organic"]
        if chemical_matches:
            best = chemical_matches[0]
        else:
            best = candidates[0]

        if "dosage_per_acre_ml" in best:
            total_units = best["dosage_per_acre_ml"] * land_size_acres
            unit_label  = "ml"
            total_cost  = (total_units / 1000) * best["cost_per_litre"]
        else:
            total_units = best["dosage_per_acre_gm"] * land_size_acres
            unit_label  = "gm"
            total_cost  = (total_units / 1000) * best["cost_per_kg"]

        return {"pesticide_name": best["pesticide_name"], "type": best["type"],
                "company": best["company"], "target_pests": best["target_pests"],
                "description": best["description"], "total_quantity": total_units,
                "unit": unit_label, "total_cost": total_cost}

    def _default_pesticide(self, land_size_acres):
        total = 500 * land_size_acres
        return {"pesticide_name": "Neem-Based Bio Pesticide", "type": "Organic",
                "company": "T-Stanes", "target_pests": ["General Pests"],
                "description": "General purpose eco-friendly biopesticide",
                "total_quantity": total, "unit": "ml", "total_cost": (total / 1000) * 250}

    def display_recommendation(self, result):
        print_section("PESTICIDE RECOMMENDATION")
        print_field("Pesticide",        result["pesticide_name"])
        print_field("Type",             result["type"])
        print_field("Supplier Company", result["company"])
        print_field("Targets",          ", ".join(result["target_pests"]))
        print_field("Description",      result["description"])
        print_field("Total Quantity",   f"{result['total_quantity']:,.0f}", result["unit"])
        print_rupees("Total Pesticide Cost", result["total_cost"])
        print_success("Pesticide recommendation generated.")