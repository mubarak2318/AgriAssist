def get_text_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  [!] This field cannot be empty. Please enter a value.")

def get_float_input(prompt, min_val=0.01, max_val=9999999):
    while True:
        try:
            value = float(input(prompt).strip())
            if min_val <= value <= max_val:
                return value
            else:
                print(f"  [!] Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("  [!] Invalid input. Please enter a number (e.g., 5 or 50000).")

def get_int_input(prompt, min_val=0, max_val=100):
    while True:
        try:
            value = int(input(prompt).strip())
            if min_val <= value <= max_val:
                return value
            else:
                print(f"  [!] Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("  [!] Invalid input. Please enter a whole number.")

def get_choice_input(prompt, valid_choices):
    print(prompt)
    for i, choice in enumerate(valid_choices, start=1):
        print(f"  {i}. {choice}")
    while True:
        try:
            index = int(input("  Enter your choice number: ").strip())
            if 1 <= index <= len(valid_choices):
                return valid_choices[index - 1]
            else:
                print(f"  [!] Please enter a number between 1 and {len(valid_choices)}.")
        except ValueError:
            print("  [!] Invalid input. Please enter a number.")

def get_optional_int(prompt):
    value = input(prompt).strip()
    if value == "":
        return None
    try:
        return int(value)
    except ValueError:
        return None