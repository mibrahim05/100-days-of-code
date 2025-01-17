import requests
from twilio.rest import Client
OWM_Endpoints  = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""

account_sid = ""
auth_token =""



weather_params = {

    "lat":-5.397140,
    "lon":105.266792,
    "appid":api_key,
    "cnt":4
}


response= requests.get(OWM_Endpoints,params=weather_params)
response.raise_for_status()
data = response.json()
will_rain = False
# print(data["list"][0]["weather"])
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    # print("bring an umbrella")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's Going to rain today,Remember to take Umbrella☔",
        from_="",
        to="",
    )
    print(message.status)





