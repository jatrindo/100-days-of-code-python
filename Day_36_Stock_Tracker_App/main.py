import os
import requests
import datetime as dt
import textwrap
import twilio.rest

STOCK = "TSLA"

AA_KEY = os.environ.get('AA_KEY')
AA_URL = "https://www.alphavantage.co/query"
SIG_PRICE_DIFF_PERC = 1.5

NEWSAPI_KEY = os.environ.get("NEWSAPI_KEY")
NEWSAPI_URL = "https://newsapi.org/v2/everything"

FROM_PHONE = os.environ.get("FROM_PHONE")
TO_PHONE = os.environ.get("TO_PHONE")

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACC_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


def get_price_change(stock_symbol):
    params = {
        'function': "TIME_SERIES_DAILY_ADJUSTED",
        'symbol': stock_symbol,
        'outputsize': "compact",
        'datatype': "json",
        'apikey': AA_KEY,
    }

    response = requests.get(url=AA_URL, params=params)
    response.raise_for_status()

    data = response.json()

    # Get the daily price data
    daily_price_data = data.get('Time Series (Daily)')

    # Dates in YYYY-MM-DD
    yesterday = dt.datetime.now() - dt.timedelta(days=1)
    yesterday_date = yesterday.strftime('%Y-%m-%d')
    day_before_yesterday = dt.datetime.now() - dt.timedelta(days=2)
    day_before_yesterday_date = day_before_yesterday.strftime('%Y-%m-%d')

    # Compare the yesterday's closing price with the day before yesterday's
    # closing price
    yesterday_price = float(
        daily_price_data.get(yesterday_date).get('4. close')
    )
    day_before_yesterday_price = float(
        daily_price_data.get(day_before_yesterday_date).get('4. close')
    )

    return ((yesterday_price - day_before_yesterday_price) / day_before_yesterday_price) * 100


def get_news_for_stock(stock_symbol):
    params = {
        'apiKey': NEWSAPI_KEY,
        'qInTitle': f"\"{stock_symbol}\"",
        'sortBy': 'publishedAt'
    }
    response = requests.get(NEWSAPI_URL, params=params)
    response.raise_for_status()

    data = response.json()

    return data.get('articles')


def create_message_string(stock_symbol, price_change_perc, articles):
    # Optional: Format the SMS message like this:
    emoji = "🔻" if (price_change_perc < 0) else "🔺"
    message = f"{stock_symbol}: {emoji}{abs(price_change_perc):.3f}%\n"

    for a in articles:
        message += textwrap.dedent(f"""
        Headline: {a.get('title')}
        Brief: {a.get('description')}
        Source: {a.get('source').get('name')}
        """)

    return message.strip()


def send_sms_message(message, account_sid, auth_token, from_phone, to_phone):
    client = twilio.rest.Client(account_sid, auth_token)
    client.messages.create(
        body=message,
        from_=from_phone,
        to=to_phone
    )


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
price_change_perc = get_price_change(STOCK)
print(f"Price Change for {STOCK}: {price_change_perc:.3f}%")

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if price_change_perc >= SIG_PRICE_DIFF_PERC:
    articles = get_news_for_stock(STOCK)[:3]

    msg = create_message_string(stock_symbol=STOCK, price_change_perc=price_change_perc, articles=articles)
    print(msg)

    # STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    send_sms_message(account_sid=TWILIO_ACCOUNT_SID, auth_token=TWILIO_AUTH_TOKEN,
                     from_phone=FROM_PHONE, to_phone=TO_PHONE, message=msg)
