import requests

parameters = {
    "amount":10,
    "type": "boolean",
    "category": 20,
}

reponse = requests.get("https://opentdb.com/api.php", params=parameters)
reponse.raise_for_status()
data = reponse.json()
question_data = (data["results"])

