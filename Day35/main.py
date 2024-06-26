import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

MY_LAT = 11.016844
MY_LON = 76.955833

endpoint_weather = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv('MY_API_KEY')
account_sid = os.getenv('MY_AUTH_SID')
auth_token = os.getenv('MY_AUTH_TOKEN')

#print(api_key)

parameter = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "cnt": 4,
    "appid": api_key
}


response = requests.get(endpoint_weather,params=parameter)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

for hour_data in weather_data["list"]:
    condition = hour_data["weather"][0]["id"]
    #print(hour_data)
    if int(condition) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body= "It's going to rain ⛈️ stay safe...(py)",
    from_=os.getenv('TWILIO_NUM'),
    to=os.getenv('MY_NUM')
    )
    print(message.status)