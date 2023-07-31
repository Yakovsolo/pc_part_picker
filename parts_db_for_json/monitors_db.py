import json

monitors = [
    {
        "brand": "Asus",
        "name": "TUF Gaming VG27AQ",
        "price": 300.00,
        "screen_size": '27.0"',
        "resolution": "2560x1440",
        "refresh_rate": 165,
        "response_time": 1.0,
        "panel_type": "IPS",
        "aspect_ratio": "16:9",
    },
    {
        "brand": "Asus",
        "name": "VG248QG",
        "price": 188.99,
        "screen_size": '24.0"',
        "resolution": "1920x1080",
        "refresh_rate": 165,
        "response_time": 0.5,
        "panel_type": "TN",
        "aspect_ratio": "16:9",
    },
    {
        "brand": "Dell",
        "name": "UP3218K",
        "price": 3999.00,
        "screen_size": '32.0"',
        "resolution": "7680x4320",
        "refresh_rate": 60,
        "response_time": 6.0,
        "panel_type": "IPS",
        "aspect_ratio": "16:9",
    },
    {
        "brand": "Samsung",
        "name": "Odyssey G9 Neo 549AG952N",
        "price": 1504.28,
        "screen_size": '49.0"',
        "resolution": "5120x1440",
        "refresh_rate": 240,
        "response_time": 1.0,
        "panel_type": "VA",
        "aspect_ratio": "32:9",
    },
    {
        "brand": "Alienware",
        "name": "AW3423DWF",
        "price": 999.99,
        "screen_size": '34.2"',
        "resolution": "3440x1440",
        "refresh_rate": 165,
        "response_time": 0.1,
        "panel_type": "QD-OLED",
        "aspect_ratio": "21:9",
    },
]

file_path = "monitors.json"

with open(file_path, "w") as file:
    json.dump(monitors, file, indent=2)


