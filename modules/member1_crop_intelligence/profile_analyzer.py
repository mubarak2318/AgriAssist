from utils.input_validator import get_text_input, get_float_input, get_choice_input, get_optional_int
from models.farmer_profile import FarmerProfile
from utils.console_formatter import print_header, print_section, print_success

class ProfileAnalyzer:
    SOIL_TYPES = [
    "Red Soil      (Well-drained, iron-rich, good for Groundnut & Maize)",
    "Black Soil    (Moisture-retaining, ideal for Cotton & Wheat)",
    "Alluvial Soil (Fertile river soil, best for Rice & Sugarcane)",
    "Sandy Loam    (Light & porous, suits Groundnut & Chickpea)",
    "Loamy Soil    (Balanced texture, versatile for most crops)",
    "Clay Soil     (Heavy & wet, ideal for Rice)"
]
    WATER_LEVELS = [
    "Low    (Borewell / Rainwater only)",
    "Medium (Canal or limited irrigation)",
    "High   (Full irrigation available)"
]
    SEASONS = [
    "Kharif  (June-Oct  | Monsoon crops: Rice, Cotton, Groundnut)",
    "Rabi    (Nov-Mar   | Winter crops : Wheat, Chickpea, Sunflower)",
    "Zaid    (Mar-June  | Summer crops : Tomato, Sugarcane)"
]

    def collect_profile(self):
        print_header("STEP 1 — FARMER PROFILE SETUP")
        print("  Please answer each question. Press Enter to confirm.\n")

        location   = get_text_input("  Enter your Location (city/district): ")
        land_size  = get_float_input("  Enter Land Size (in acres): ", min_val=0.1, max_val=500)
        soil_type  = get_choice_input("\n  Select your Soil Type:", self.SOIL_TYPES)
        soil_type = soil_type.split("(")[0].strip()
        water      = get_choice_input("\n  Select Water Availability:", self.WATER_LEVELS)
        water     = water.split("(")[0].strip()
        season     = get_choice_input("\n  Select Farming Season:", self.SEASONS)
        season = season.split("(")[0].strip().split()[0]
        budget     = get_float_input("\n  Enter your Budget (in Rs.): ", min_val=1000, max_val=9999999)

        print("\n  Farming experience is optional. Press Enter to skip.")
        experience = get_optional_int("  Years of farming experience: ")

        profile = FarmerProfile(
            location=location,
            land_size_acres=land_size,
            soil_type=soil_type,
            water_availability=water,
            season=season,
            budget=budget,
            experience_years=experience
        )
        print_success("Farmer profile recorded successfully.")
        # Sanity check — warn if budget is very low for the land size
        estimated_minimum = land_size * 5000   # rough Rs.5000/acre minimum
        if budget < estimated_minimum:
            print()
            print(f"  [!] NOTE: Rs.{budget:,.0f} seems low for {land_size} acres.")
            print(f"  [i] Typical minimum for this farm size: Rs.{estimated_minimum:,.0f}")
            print(f"  [i] The system will still generate a full advisory with loan recommendations.")
        return profile

    def display_profile(self, profile):
        print_section("YOUR FARM PROFILE SUMMARY")
        print(f"  {'Location':<22}: {profile.location}")
        print(f"  {'Land Size':<22}: {profile.land_size_acres} acres")
        print(f"  {'Soil Type':<22}: {profile.soil_type}")
        print(f"  {'Water Availability':<22}: {profile.water_availability}")
        print(f"  {'Season':<22}: {profile.season}")
        print(f"  {'Budget':<22}: Rs. {profile.budget:,.0f}")
        if profile.experience_years is not None:
            print(f"  {'Experience':<22}: {profile.experience_years} years")
        else:
            print(f"  {'Experience':<22}: Not provided")