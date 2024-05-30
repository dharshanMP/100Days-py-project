import requests
from datetime import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()

user_input = input("Enter your exercise: ")

USER_NAME = os.getenv('NAME')
API_ID = os.getenv('API_ID')
API_KEY = os.getenv('API_KEY')

NUTRITION_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

data = {
    "query": user_input,
    "gender": "male",  
    "weight_kg": 70,  
    "height_cm": 175,  
    "age": 30  
}

response = requests.post(NUTRITION_API_ENDPOINT, headers=headers, json=data)
exercise_result = response.json()

# if response.status_code == 200:
#     print(response.json())
# else:
#     print(response.json())


today = dt.now().strftime("%d%m%y")
timing = dt.now().strftime("%x")

sheety_endpoint = f"https://api.sheety.co/{USER_NAME}/dharshanExercise/dharshanExercise"
for exercise in exercise_result["exercises"]:
    inputs_sheety = {
        "dharshanexercise":{
            "date": today,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"], 
        }
    }

# print(inputs_sheety)

sheety_response = requests.post(sheety_endpoint,json=inputs_sheety)
print(sheety_response.text)