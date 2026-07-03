WIDTH = 60

def print_header(title):
    print("\n" + "=" * WIDTH)
    print(title.center(WIDTH))
    print("=" * WIDTH)

def print_section(title):
    print("\n" + "-" * WIDTH)
    print(f" {title}")
    print("-" * WIDTH)

def print_field(label, value, unit=""):
    label_padded = f"  {label:<22}"
    unit_str = f" {unit}" if unit else ""
    print(f"{label_padded}: {value}{unit_str}")

def print_list_items(items, indent=4):
    for item in items:
        print(" " * indent + f"• {item}")

def print_success(message):
    print(f"  [✓] {message}")

def print_warning(message):
    print(f"  [!] {message}")

def print_info(message):
    print(f"  [i] {message}")

def print_separator():
    print("  " + "." * (WIDTH - 2))

def print_rupees(label, amount):
    formatted = f"Rs. {amount:,.0f}"
    print_field(label, formatted)