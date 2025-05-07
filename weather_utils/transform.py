import json

def clean_weather_data():
    with open('/tmp/weather_raw.json') as f:
        data = json.load(f)

    cleaned = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"],
        "timestamp": data["dt"]
    }

    with open('/tmp/weather_cleaned.json', 'w') as f:
        json.dump(cleaned, f)
