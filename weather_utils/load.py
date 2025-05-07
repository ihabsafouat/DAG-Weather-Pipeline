import json
import sqlite3

def save_weather_data():
    with open('/tmp/weather_cleaned.json') as f:
        data = json.load(f)

    conn = sqlite3.connect('/tmp/weather.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT,
            temperature REAL,
            humidity REAL,
            weather TEXT,
            timestamp INTEGER
        )
    ''')

    cursor.execute('''
        INSERT INTO weather (city, temperature, humidity, weather, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (data['city'], data['temperature'], data['humidity'], data['weather'], data['timestamp']))

    conn.commit()
    conn.close()
