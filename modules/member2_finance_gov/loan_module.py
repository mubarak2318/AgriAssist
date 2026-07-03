from utils.console_formatter import print_section, print_rupees, print_success, print_info

class LoanModule:
    def __init__(self, loan_dataset):
        self.loan_dataset = loan_dataset

    def assess(self, budget, cultivation_cost, fertilizer_cost, pesticide_cost):
        total_cost  = cultivation_cost + fertilizer_cost + pesticide_cost
        budget_gap  = total_cost - budget
        if budget_gap > 0:
            suitable = [l for l in self.loan_dataset if l["max_amount"] >= budget_gap]
            suitable.sort(key=lambda x: x["interest_rate_percent"])
        else:
            suitable = self.loan_dataset[:]
        return {"total_cost": total_cost, "farmer_budget": budget,
                "budget_gap": budget_gap, "needs_loan": budget_gap > 0,
                "suggested_loans": suitable}

    def display_loans(self, result):
        print_section("LOAN ASSISTANCE")
        print_rupees("Total Estimated Cost", result["total_cost"])
        print_rupees("Your Budget",          result["farmer_budget"])
        if result["needs_loan"]:
            print_rupees("Budget Shortfall", result["budget_gap"])
            print(f"\n  Recommended loan options (cheapest interest first):\n")
            for i, loan in enumerate(result["suggested_loans"], start=1):
                print(f"  {i}. {loan['loan_name']}")
                print(f"     Provider     : {loan['provider']}")
                print(f"     Max Amount   : Rs. {loan['max_amount']:,}")
                print(f"     Interest Rate: {loan['interest_rate_percent']}% per year")
                print(f"     Tenure       : {loan['tenure_months']} months")
                print(f"     Purpose      : {loan['purpose']}")
                print()
        else:
            print_rupees("Budget Surplus", abs(result["budget_gap"]))
            print_info("Your budget is sufficient. No loan needed.")
        print_success("Loan assessment complete.")


        