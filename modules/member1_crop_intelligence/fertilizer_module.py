from abc import ABC, abstractmethod
from utils.console_formatter import print_section, print_field, print_rupees, print_success


class FertilizerBase(ABC):
    @abstractmethod
    def recommend(self, crop_name, soil_type, land_size_acres):
        pass

    @abstractmethod
    def display_recommendation(self, result):
        pass


class FertilizerModule(FertilizerBase):
    def __init__(self, fertilizer_dataset):
        self.fertilizer_dataset = fertilizer_dataset

    def recommend(self, crop_name, soil_type, land_size_acres):
        best_match = None
        best_score = 0

        for fertilizer in self.fertilizer_dataset:
            score = self._score_fertilizer(fertilizer, crop_name, soil_type)

            if score > best_score:
                best_score = score
                best_match = fertilizer

        if best_match is None:
            return self._default_fertilizer(land_size_acres)

        total_dosage = best_match["dosage_per_acre_kg"] * land_size_acres
        total_cost = total_dosage * best_match["cost_per_kg"]

        return {
            "fertilizer_name": best_match["fertilizer_name"],
            "company": best_match["company"],
            "description": best_match["description"],
            "dosage_per_acre_kg": best_match["dosage_per_acre_kg"],
            "total_dosage_kg": total_dosage,
            "cost_per_kg": best_match["cost_per_kg"],
            "total_cost": total_cost
        }

    def _score_fertilizer(self, fertilizer, crop_name, soil_type):
        score = 0

        if crop_name in fertilizer["suitable_crops"]:
            score += 1

        if soil_type in fertilizer["suitable_soil"]:
            score += 1

        return score

    def _default_fertilizer(self, land_size_acres):
        total = 50 * land_size_acres

        return {
            "fertilizer_name": "NPK 10:26:26",
            "company": "IFFCO",
            "description": "General purpose balanced NPK",
            "dosage_per_acre_kg": 50,
            "total_dosage_kg": total,
            "cost_per_kg": 25,
            "total_cost": total * 25
        }

    def display_recommendation(self, result):
        print_section("FERTILIZER RECOMMENDATION")
        print_field("Fertilizer", result["fertilizer_name"])
        print_field("Supplier Company", result["company"])
        print_field("Description", result["description"])
        print_field("Dosage per Acre", f"{result['dosage_per_acre_kg']}", "kg")
        print_field("Total Quantity", f"{result['total_dosage_kg']:,.0f}", "kg")
        print_rupees("Total Fertilizer Cost", result["total_cost"])
        print_success("Fertilizer recommendation generated.")