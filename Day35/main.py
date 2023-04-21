import requests
from twilio.rest import Client

lat = 45.500940  # Your latitude
lon = -73.572700  # Your longitude
# my api key

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
#account
#auth

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

# print(response.status_code)
# print(weather_data)

# print(weather_data['hourly'][0]['weather'])
# print(weather_data['hourly'][0]['weather'][0]['main'])

counter = 0
will_rain = False
for data in weather_data:
    while counter < 12:
        counter += 1
        forecast = weather_data['hourly'][counter]['weather'][0]['id']
        if forecast < 700:
            will_rain = True
if will_rain:
    print("Bring an umbrella!")
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Bring an umbrella! It's going to rain today.",
        from_='+12766002655',
        to='+1'
    )
    print(message.sid)
