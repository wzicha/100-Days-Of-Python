import requests
import datetime

lat = 45.500940  # Your latitude
lon = -73.572700  # Your longitude
# API_KEY
time = datetime.datetime.now()

response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={API_key}")
# response.raise_for_status()
data = response.json()

print(response.status_code)


