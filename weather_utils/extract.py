import requests

def get_weather_data():
    API_KEY = 'd3c************************' #for security
    CITY = 'Casablanca'
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    response = requests.get(URL)
    data = response.json()
    
    with open('/tmp/weather_raw.json', 'w') as f:
        f.write(response.text)
