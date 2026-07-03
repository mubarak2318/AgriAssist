from utils.console_formatter import print_section, print_success, print_warning

class SchemeAdvisor:
    def __init__(self, scheme_dataset):
        self.scheme_dataset = scheme_dataset

    def check_eligibility(self, profile):
        return [s for s in self.scheme_dataset if self._is_eligible(s, profile)]

    def _is_eligible(self, scheme, profile):
        rules = scheme["eligibility"]
        if "max_land_acres" in rules and profile.land_size_acres > rules["max_land_acres"]:
            return False
        if "min_land_acres" in rules and profile.land_size_acres < rules["min_land_acres"]:
            return False
        if "water_availability" in rules and profile.water_availability not in rules["water_availability"]:
            return False
        if "seasons" in rules and profile.season not in rules["seasons"]:
            return False
        return True

    def display_schemes(self, eligible_schemes):
        print_section("GOVERNMENT SCHEMES — ELIGIBILITY")
        if not eligible_schemes:
            print_warning("No eligible schemes found for your profile.")
            return
        print(f"  You are eligible for {len(eligible_schemes)} scheme(s):\n")
        for i, scheme in enumerate(eligible_schemes, start=1):
            print(f"  {i}. {scheme['scheme_name']}")
            print(f"     Benefit : {scheme['benefit']}")
            print(f"     About   : {scheme['description']}")
            print()
        print_success(f"{len(eligible_schemes)} eligible scheme(s) identified.")