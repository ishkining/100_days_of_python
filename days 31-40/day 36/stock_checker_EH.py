import os
from datetime import datetime

import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

parameters_aplhavantage = {
    'function': 'TIME_SERIES_INTRADAY',
    'symbol': STOCK,
    'interval': '60min',
    'apikey': os.environ.get('API_ALPHAVANTAGE')
}

today_date = datetime.now()
yesterday_date = f"{today_date.year}-{f'0{today_date.month}' if today_date.month < 10 else today_date.month}-" \
                 f"{int((today_date.day - 1) % 31)}"


stock_response = requests.get(url='https://www.alphavantage.co/query', params=parameters_aplhavantage)
stock_response.raise_for_status()

# STEP 1: Use https://newsapi.org
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

yesterday_stock_difference = float(stock_response.json()['Time Series (60min)'][yesterday_date+' 20:00:00']['4. close']) \
                             - \
                             float(stock_response.json()['Time Series (60min)'][yesterday_date+' 05:00:00']['1. open'])

percent_of_difference = (yesterday_stock_difference / \
                        float(stock_response.json()['Time Series (60min)'][yesterday_date+' 05:00:00']['1. open'])) \
                        * 100
print(yesterday_stock_difference)
print(f'{percent_of_difference}%')

# STEP 2: Use https://www.alphavantage.co
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if -5 > percent_of_difference > 5:
    parameters_newsapi = {
        'q': COMPANY_NAME,
        'apikey': os.environ.get('API_NEWSAPI')
    }

    news_response = requests.get(url='https://newsapi.org/v2/everything', params=parameters_newsapi)
    news_response.raise_for_status()
    news_dict = [(news['source']['name'], news['title']) for news in news_response.json()['articles'][:3]]
    for item in news_dict:
        print(item[0])

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

