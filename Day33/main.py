# import requests 

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# print(response.json()["message"])

# Sunrise and Sunset

# parameters = {
#     "lat" : "20.593683",
#     "lng" : "78.962883",
#     "formatted" : "0"
# }

# response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# print(data)