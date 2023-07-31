import json

memory_ram = [
    {
        "brand": "Corsair",
        "name": "Vengeance LPX 16GB",
        "price": 37.99,
        "ram_type": "DDR4",
        "ram_speed": 3200,
        "ram_modules": "2 x 8GB",
    },
    {
        "brand": "Corsair",
        "name": "Vengeance RGB PRO 32GB",
        "price": 104.98,
        "ram_type": "DDR4",
        "ram_speed": 3600,
        "ram_modules": "2 x 16GB",
    },
    {
        "brand": "Corsair",
        "name": "Vengeance LPX 32GB",
        "price": 67.99,
        "ram_type": "DDR4",
        "ram_speed": 3600,
        "ram_modules": "2 x 16GB",
    },
    {
        "brand": "G.Skill",
        "name": "Trident Z5 RGB 32GB",
        "price": 104.99,
        "ram_type": "DDR5",
        "ram_speed": 6000,
        "ram_modules": "2 x 32GB",
    },
    {
        "brand": "Silicon Power",
        "name": "Gaming 16GB",
        "price": 29.97,
        "ram_type": "DDR4",
        "ram_speed": 3200,
        "ram_modules": "2 x 8GB",
    },
]

file_path = "memory_ram.json"

with open(file_path, "w") as file:
    json.dump(memory_ram, file, indent=2)
