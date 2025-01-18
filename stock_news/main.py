import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_api_key = ""
news_api_key = ""
account_sid = ""
auth_token =""
stock_params={

    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":stock_api_key,



}
response = requests.get(STOCK_ENDPOINT,params=stock_params)
data = response.json()["Time Series (Daily)"]

data_list = [value for (key,value) in data.items()]
yesterday_list = data_list[0]
yesterday_closing_price = yesterday_list["4. close"]
print(yesterday_closing_price)

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]
print(day_before_yesterday_closing_price)

positive_difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if positive_difference >0:
    up_down ="🔺"
else:
    up_down = "🔻"

diff_percent = round((positive_difference/float(yesterday_closing_price))*100)
print(diff_percent)

if abs(diff_percent) > 2:
    news_params={
        "apiKey":news_api_key,
        "qInTitle":COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    articles = news_response.json()["articles"]
    # print(article)
three_articles = articles[:3]
print(three_articles)


formatted_article = [f"{STOCK_NAME}:{up_down}{diff_percent}%\nHeadline:{article['title']}.\nBrief:{article['description']}" for article in three_articles]


for article in formatted_article:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=article,
        from_="",
        to="",
    )
    print(message.status)


