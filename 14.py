length_in_feet = float(input("Enter length in feet: "))

options = [
    ("Inches", 12),
    ("Yards", 1/3),
    ("Miles", 1/5280),
    ("Millimetres", 304.8),
    ("Centimetres", 30.48),
    ("Meters", 0.3048),
    ("Kilometers", 0.0003048)
]

print("Choose a conversion option:")
for i, (name, _) in enumerate(options, start=1):
    print(f"{i}. {name}")

choice = int(input("Enter your choice (1-7): "))

if 1 <= choice <= len(options):
    unit_name, factor = options[choice - 1]
    converted_value = length_in_feet * factor
    print(f"{length_in_feet} feet = {converted_value} {unit_name}")
else:
    print("Invalid choice")
