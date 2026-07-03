from models.farmer_profile import FarmerProfile
from models.crop_recommendation import CropRecommendation
from utils.console_formatter import print_section, print_field, print_success

class CropRecommendationEngine:
    def __init__(self, crop_dataset):
        self.crop_dataset = crop_dataset

    def recommend(self, profile):
        scored_crops = []
        for crop in self.crop_dataset:
            score = self._calculate_score(crop, profile)
            scored_crops.append((score, crop))
        scored_crops.sort(key=lambda x: x[0], reverse=True)

        best_score, best_crop = scored_crops[0]
        alternatives = [scored_crops[i][1]["crop_name"] for i in range(1, min(3, len(scored_crops)))]
        expected_yield = best_crop["avg_yield_per_acre"] * profile.land_size_acres

        return CropRecommendation(
            crop_name=best_crop["crop_name"],
            expected_yield_kg=expected_yield,
            suitability_score=best_score,
            avg_market_price_per_kg=best_crop["avg_market_price_per_kg"],
            cultivation_cost_per_acre=best_crop["cultivation_cost_per_acre"],
            alternatives=alternatives
        )

    def _calculate_score(self, crop, profile):
        score = 0
        if profile.soil_type in crop["suitable_soil"]:
            score += 40
        if profile.water_availability == crop["water_need"]:
            score += 35
        elif profile.water_availability == "High" and crop["water_need"] == "Medium":
            score += 20
        elif profile.water_availability == "Medium" and crop["water_need"] == "Low":
            score += 20
        if profile.season == crop["season"]:
            score += 25
        return score

    def display_recommendation(self, recommendation):
        print_section("CROP RECOMMENDATION")
        print_field("Recommended Crop", recommendation.crop_name)
        print_field("Suitability Score", f"{recommendation.suitability_score}/100")
        print_field("Expected Yield", f"{recommendation.expected_yield_kg:,.0f}", "kg")
        print_field("Market Price", f"Rs. {recommendation.avg_market_price_per_kg}/kg")
        if recommendation.alternatives:
            print(f"\n  {'Alternative Crops':<22}:")
            for alt in recommendation.alternatives:
                print(f"    • {alt}")
        print_success("Crop recommendation generated.")