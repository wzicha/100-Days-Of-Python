import smtplib
import requests
from datetime import datetime, timezone
import time

MY_LAT = 45.500940  # Your latitude
MY_LONG = -73.572700  # Your longitude

# email / password

def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    return abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    # Convert UTC time to local time
    sunrise_utc = datetime.fromisoformat(data["results"]["sunrise"]).replace(tzinfo=timezone.utc)
    sunset_utc = datetime.fromisoformat(data["results"]["sunset"]).replace(tzinfo=timezone.utc)
    sunrise_local = sunrise_utc.astimezone()
    sunset_local = sunset_utc.astimezone()

    # Format time in PM format
    sunrise_pm = sunrise_local.strftime('%I:%M:%S %p')
    sunset_pm = sunset_local.strftime('%I:%M:%S %p')

    print(data)

    # Check if it is currently night time
    time_now = datetime.now().hour
    return time_now >= sunset_local.hour or time_now <= sunrise_local.hour


def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=email_password)
        connection.sendmail(from_addr=my_email, to_addrs="wzicha@gmail.com",
                            msg=f"Subject: Look up in the sky!\n\nThe ISS is above you")
        connection.close()

while True:
    if is_iss_close() and is_night():
        send_email()
    time.sleep(60)
