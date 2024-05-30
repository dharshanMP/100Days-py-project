import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

STOCK_NAME = os.getenv('STOCK_NAME')
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_key = os.getenv('STOCK_KEY')
news_api_key = os.getenv('NEWS_API_KEY')

acct_sid = os.getenv('ACC_SID')
auth_token = os.getenv('AUTH_TOKEN')


parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey": stock_api_key
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()["Time Series (Daily)"]

data_li = [value for (key, value) in data.items()]
yestrday_data = data_li[0]
yestrday_closing_data = yestrday_data["4. close"]
print(yestrday_closing_data)


day_before_yesterday_data = data_li[1]
day_before_closing = day_before_yesterday_data["4. close"]
print(day_before_closing)



difference = float(yestrday_closing_data) - float(day_before_closing)

up = None
if difference > 0:
    up = "🔺"
else:
    up = "🔻"    



difference_precentage = round((float(difference)/float(yestrday_closing_data)) *100)
print(difference_precentage)


if abs(difference_precentage) > 1:
    news_parameter = {
        "apiKey" : news_api_key,
        "qInTitle": COMPANY_NAME
    }

    response = requests.get(NEWS_ENDPOINT, params=news_parameter)
    response.raise_for_status()
    articles = response.json()["articles"]
    # print(articles)



    first_three_articles = articles[:3]
    # print(first_three_articles)

    seperated_articles = [f"{STOCK_NAME}: {up}{difference_precentage}\n Headline : {article['title']}. \nBrief:{article['description']}" for article in first_three_articles]

    client = Client(acct_sid, auth_token)

    for article in seperated_articles:
        message = client.messages.create( 
            body= article,
            from_= "+17372655676",
            to= "+916382336654")

                        

    



