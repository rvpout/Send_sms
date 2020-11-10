# Configure telebot
# Sends sms every morning to telegram
# Looks up weather
# Adds the waether uppdate to sms

import requests
import json
import schedule
import time


# Configures telegrambot

import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '1499612660:AAF4wbH-ztZ17l9pZ8G4ytdAv61aHmvUSng'
    bot_chatID = '790865520'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()    

#Looks up weather from openweather

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


# Send weather info to telegram

def report():
        telegram_bot_sendtext(" Temperature: " + 
                str(current_temperature) + " Degrees " +
        "\nCurrently feels like: " +
                str(current_feels) + " Degrees" +
        "\nwind speed: "  +
                str(current_wind) + " m/s " +
        "\ndescription: " +
                str(weather_description))

schedule.every().day.at("15:50").do(report)

while True:
        schedule.run_pending()
        time.sleep(1)

