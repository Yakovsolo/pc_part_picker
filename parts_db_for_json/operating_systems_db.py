import json

operating_systems = [
    {
        "brand": "Microsoft",
        "name": "Windows 11 Home",
        "price": 117.98,
        "mode": "64-bit",
        "max_supported_memory": 128,
    },
    {
        "brand": "Microsoft",
        "name": "Windows 11 Pro",
        "price": 144.99,
        "mode": "64-bit",
        "max_supported_memory": 2048,
    },
    {
        "brand": "Microsoft",
        "name": "Windows 10 Pro",
        "price": 129.55,
        "mode": "64-bit",
        "max_supported_memory": 2048,
    },
    {
        "brand": "Microsoft",
        "name": "Windows 10 Pro",
        "price": 199.99,
        "mode": "32/64-bit",
        "max_supported_memory": 2048,
    },
    {
        "brand": "Microsoft",
        "name": "Windows 8.1 Pro DE",
        "price": 188.07,
        "mode": "64-bit",
        "max_supported_memory": 512,
    },
]


file_path = "operating_systems.json"

with open(file_path, "w") as file:
    json.dump(operating_systems, file, indent=2)
