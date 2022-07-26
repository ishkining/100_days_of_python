from datetime import datetime
import time

import requests

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

TEST_LAT = -43.6764
TEST_LONG = 37.9182

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
do_u_found = False

while not do_u_found:
    time.sleep(60)
    if iss_latitude - 5 < TEST_LONG < iss_longitude + 5 and iss_latitude - 5 < TEST_LAT < iss_latitude + 5:
        print("I'm here")
        if time_now.hour < sunrise or time_now.hour > sunset:
            do_u_found = True
            print("Look up")

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



