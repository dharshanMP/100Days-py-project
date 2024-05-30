import requests
from datetime import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv('MY_NAME')
TOKEN = os.getenv('MY_TOKEN')
GRAPH_ID = os.getenv('MY_GRAPH_ID')

pixela_end_point =  "https://pixe.la/v1/users"

user_params = {
    "token": USERNAME,
    "username":TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=pixela_end_point, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_end_point}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name" : "Book reading graph",
    "unit":"Hrs",
    "type":"float",
    "color":"sora"

}

header = {
    "X-USER-TOKEN":TOKEN
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)


pixel_endpoint = f"{pixela_end_point}/{USERNAME}/graphs/{GRAPH_ID}"

today = dt.now()
# print(today.strftime("%Y%m%d"))

pixel_update = {
    "date": today.strftime("%Y%m%d"),
    "quantity":input("How many hrs you read book : "),
}

response = requests.post(url=pixel_endpoint, json=pixel_update, headers=header)
print(response.text)


update_endpoint = f"{pixela_end_point}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel = {
    "quantity":"1.3"
}

# response = requests.put(url=update_endpoint, json=new_pixel, headers=header)
# print(response.text)


delete_endpoint = f"{pixela_end_point}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint,headers=header)
# print(response.text)
