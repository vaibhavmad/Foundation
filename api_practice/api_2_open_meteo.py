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
    response = requests.get(url, params=params, timeout=10)
    status_code = response.status_code

    # --- LOGIC FIX: treat non-200 as error and stop; only parse/print when we have success ---
    # BEFORE (bug): if status_code != 200 we did "pass", then execution fell through to the print below.
    # But current_temperature was only set inside the else block, so on non-200 we'd get NameError.
    #
    # BEFORE code (removed, kept here for reference):
    #   if status_code != 200:
    #       pass
    #   else:
    #       weather_data = response.json()
    #       current_temperature = weather_data["current"]["temperature_2m"]
    #   print(f"Current temperature...")   <-- this ran for BOTH 200 and non-200; current_temperature undefined when non-200!
    #
    # AFTER: if non-200, we print and exit. Success path (parse + print) lives only inside the else.

    if status_code != 200:
        # Non-200 = API did not return OK. Print why and stop; do not try to parse or use current_temperature.
        print(f"Bad response: status {status_code}, reason: {response.reason}. Response body: {response.text[:200]}")
        exit(1)
    else:
        # Only when status is 200: parse JSON, get temperature, then print. Success print runs only here.
        weather_data = response.json()
        current_temperature = weather_data["current"]["temperature_2m"]
        print(f"Current temperature in the given area is: {current_temperature} degree Celsius.")

except Exception as e:
    print(f"An error occurred: {e}")