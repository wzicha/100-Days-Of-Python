from datetime import datetime
import requests
import json
import smtplib

# username for opensky
# password
# email
# password

# ICAO24 identifier of the aircraft to track
# icao24 = "c05ea6"
icao24 = "3c6516"

# Time to retrieve track data for
date_string = "Fri Mar 31 13:00:00 2023 -0500"
dt = datetime.strptime(date_string, "%a %b %d %H:%M:%S %Y %z")

# URL for retrieving track data for the specified aircraft at the given time
url = f"https://opensky-network.org/api/tracks/?icao24={icao24}&time={int(dt.timestamp())}"

# Make an authenticated request to the OpenSky Network API
response = requests.get(url, auth=(username, password))

try:
    data = response.json()
    print(json.dumps({"path": data["path"][:10]}, indent=4))
    print(response.text)

    if data['path'][0][5] == False:
        print(data['path'][0][5])
        print("Fight has not landed")
except json.decoder.JSONDecodeError:
        print("Error: Response is not in JSON format")
        print("Flight has landed")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=email_password)
            connection.sendmail(from_addr=my_email, to_addrs="wzicha@gmail.com", msg=f"Subject: Flight has landed\n\nAircraft {icao24} has landed")
            connection.close()


