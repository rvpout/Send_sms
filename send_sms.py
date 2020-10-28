# 1. Configure sms
# 2. Sends sms every morning (twilio)
# 3. Looks up weather
# 4. Adds the waether uppdate to sms

import requests, json
from twilio.rest import Client


# Configures SMS, where to send

account_sid = ['ACbc7f3e3e1959d94ae8f85077d5ced437']
auth_token = ['3f26ec142b5bc4a7223634d9989f425d']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="helou there",
                     from_='twilio number',
                     to='My number'
                 )

print(message.sid)



#Looks up weather  requests, json,

api_key = "7159346aea3d43e2f5e93c740d810b82"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Turku"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"] - 273.15
    current_feels = y["feels_like"] - 273.15

    b = x["wind"]
    current_wind = b["speed"]

    z = x["weather"]
    weather_description = z[0]["description"]
    
    
    print(" Temperature = " + 
                str(current_temperature) + " Astetta " +
        "\n Currently feels like = " +
                str(current_feels) + " Astetta " +
        "\n wind speed = "  +
                str(current_wind) + " m/s " +
        "\n description = " +
                str(weather_description))

else:
    print("Error")
