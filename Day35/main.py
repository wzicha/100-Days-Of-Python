import requests

lat = 45.500940  # Your latitude
lon = -73.572700  # Your longitude
#API_KEY
weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": API_key,
    "exclude": "current,minutely,daily"
}
OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

print(response.status_code)
print(weather_data)

print(weather_data['hourly'][0]['weather'])
print(weather_data['hourly'][0]['weather'][0]['main'])

counter = 0
for data in weather_data:
    while counter < 12:
        counter += 1
        print(weather_data['hourly'][counter]['weather'][0]['main'])
