import json

cpus = [
    {
        "brand": "AMD",
        "name": "Ryzen 5 5600X",
        "price": 162.66,
        "core_count": 6,
        "performance_core_clock": 3.7,
        "performance_boost_clock": 4.6,
        "integrated_graphics": None,
    },
    {
        "brand": "AMD",
        "name": "Ryzen 7 5800X",
        "price": 217.99,
        "core_count": 8,
        "performance_core_clock": 3.8,
        "performance_boost_clock": 4.7,
        "integrated_graphics": None,
    },
    {
        "brand": "AMD",
        "name": "Ryzen 7 7800X3D",
        "price": 439.00,
        "core_count": 8,
        "performance_core_clock": 4.2,
        "performance_boost_clock": 5.0,
        "integrated_graphics": "Radeon",
    },
    {
        "brand": "Intel",
        "name": "Core i7 13700K",
        "price": 409.00,
        "core_count": 16,
        "performance_core_clock": 3.4,
        "performance_boost_clock": 5.4,
        "integrated_graphics": "Intel UHD Graphics 770",
    },
    {
        "brand": "Intel",
        "name": "Core i9 13900K",
        "price": 569.99,
        "core_count": 24,
        "performance_core_clock": 3.0,
        "performance_boost_clock": 5.8,
        "integrated_graphics": "Intel UHD Graphics 770",
    },
    {
        "brand": "Intel",
        "name": "Core i9 13900K",
        "price": 569.99,
        "core_count": 24,
        "performance_core_clock": 3.0,
        "performance_boost_clock": 5.8,
        "integrated_graphics": "Intel UHD Graphics 770",
    },
]

file_path = "cpus.json"

with open(file_path, "w") as file:
    json.dump(cpus, file, indent=2)
