import json

power_suplyes = [
    {
        "brand": "Corsair",
        "name": "RM750e (2023)",
        "price": 99.99,
        "power_suply_type": "ATX",
        "wattage": 750,
        "modular": "Full",
    },
    {
        "brand": "Corsair",
        "name": "RM850e (2021)",
        "price": 129.99,
        "power_suply_type": "ATX",
        "wattage": 850,
        "modular": "Full",
    },
    {
        "brand": "Thermaltake",
        "name": "Toughpower GX2",
        "price": 67.98,
        "power_suply_type": "ATX",
        "wattage": 600,
        "modular": "No",
    },
    {
        "brand": "Gigabyte",
        "name": "UD750GM",
        "price": 84.99,
        "power_suply_type": "ATX",
        "wattage": 750,
        "modular": "Full",
    },
    {
        "brand": "Cooler Master",
        "name": "V850 SFX GOLD",
        "price": 135.99,
        "power_suply_type": "ATX",
        "wattage": 850,
        "modular": "Full",
    },
]

file_path = "power_suplyes.json"

with open(file_path, "w") as file:
    json.dump(power_suplyes, file, indent=2)
