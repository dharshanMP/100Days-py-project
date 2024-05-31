import requests

API_KEY = "dAZXlcPsoMLUA3dI4DFEZO2GN6nkjtzZ"
API_SCERET = "Hw6cOayFlL9VP6b9"
API_TOKEN = "slrD6Yse1S7K2hj12yNO4Bg30oSD"
API_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

headers = {
    "Authorization":f"Bearer {API_TOKEN}",
    "Content-Type": "application/vnd.amadeus+json"

Parameters = {
    "originLocationCode": "CJB",
    "destinationLocationCode": "DEL",
    "departureDate":"2024-05-02",
    "adults": "1",
    
}

response = requests.get(url=API_ENDPOINT,headers=headers, params=Parameters)
response.raise_for_status()
print(response.json())
