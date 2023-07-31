import json

video_cards = [
    {
        "brand": "MSI",
        "name": "GeForce RTX 3060 Ventus 2X 12G",
        "price": 289.99,
        "video_chipset": "GeForce RTX 3060",
        "video_memory": 12,
        "vdeo_core_clock": 1320,
        "video_boost_clock": 1777,
    },
    {
        "brand": "Gigabyte",
        "name": "WINDFORCE OC",
        "price": 599.99,
        "video_chipset": "GeForce RTX 4070",
        "video_memory": 12,
        "vdeo_core_clock": 1920,
        "video_boost_clock": 2490,
    },
    {
        "brand": "Asus",
        "name": "ROG STRIX GAMING OC",
        "price": 1951.79,
        "video_chipset": "GeForce RTX 4090",
        "video_memory": 24,
        "vdeo_core_clock": 2235,
        "video_boost_clock": 2640,
    },
    {
        "brand": "XFX",
        "name": "Speedster MERC 319 CORE",
        "price": 529.99,
        "video_chipset": "Radeon RX 6800 XT",
        "video_memory": 16,
        "vdeo_core_clock": 1825,
        "video_boost_clock": 2250,
    },
    {
        "brand": "Sapphire",
        "name": "PULSE",
        "price": 394.76,
        "video_chipset": "Radeon RX 6700 XT",
        "video_memory": 12,
        "vdeo_core_clock": 2321,
        "video_boost_clock": 2581,
    },
]

file_path = "video_cards.json"

with open(file_path, "w") as file:
    json.dump(video_cards, file, indent=2)
