import requests
from datetime import datetime

GENDER ="Male"
AGE = 21
WEIGHT = 50
HEIGHT = 170
APP_ID= ""
APP_KEY = ""
sheet_endpoint = ""
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercise you did:")

TOKEN = ""
headers = {
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,
}

exercise_params = {
    "query":exercise_text,
    "gender":GENDER,
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE
}

response = requests.post(url=exercise_endpoint,json=exercise_params,headers=headers)
data = response.json()
# print(data)

today_date = datetime.now().strftime("%d/%m/%Y")
# print(today_date)
now_time = datetime.now().strftime("%X")
# print(now_time)
bearer_headers = {
"Authorization": f"Bearer {TOKEN}"
}

for exercise in data["exercises"]:
    sheet_input ={
        "workout":{
            "date":today_date,
            "time":now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_input,
        headers=bearer_headers
    )
    print(sheet_response.text)
