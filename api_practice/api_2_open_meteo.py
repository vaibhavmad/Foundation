import requests

# new delhi lat: 28.61 N and long: 77.21 E
# The API endpoint /v1/forecast accepts a geographical coordinate, a list of weather variables and responds with a JSON hourly weather forecast for 7 days. Time always starts at 0:00 today and contains 168 hours. If &forecast_days=16 is set, up to 16 days of forecast can be returned. 
# example request: https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": "28.61",
    "longitude": "77.21",
    "current": "temperature_2m,is_day"
}

try: 
    response = requests.get(url, params = params, timeout=10)
    status_code = response.status_code

    if status_code != 200:
        pass
    else:
        weather_data = response.json()
        current_temperature = weather_data["current"]["temperature_2m"]

    print(f"Current temperature in the given area is: {current_temperature} degree celcius.")
        
except Exception as e:
    print(f"An error occurred: {e}")