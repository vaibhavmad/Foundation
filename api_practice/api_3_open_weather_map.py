import requests
import os
from dotenv import load_dotenv

load_dotenv()

open_weather_api = os.getenv("open_weather_map_key")

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "lat": "28.61",
    "lon": "77.21",
    "appid": open_weather_api
}

response = requests.get(url = url, params = params, timeout=10)

print(response.json())