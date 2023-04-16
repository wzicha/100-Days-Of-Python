import requests
import datetime

lat = 45.500940  # Your latitude
lon = -73.572700  # Your longitude
#api key
weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": API_key,
}
OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"

response = requests.get(OWM_Endpoint, params=weather_params)
# response.raise_for_status()
data = response.json()

print(response.status_code)
print(data)


