import yfinance as yf
import pandas as pd
import numpy as np

from statsmodels.tsa.arima.model import ARIMA

import pyotp
import robin_stocks as robinhood
import alpaca_trade_api as alpaca

import telegram
import sys
import os

import matplotlib.pyplot as plt 
plt.style.use('fivethirtyeight')


RH_USER_EMAIL = os.environ['RH_USER_EMAIL']
RH_PASSWORD = os.environ['RH_PASSWORD']
RH_MFA_CODE = os.environ['RH_MFA_CODE']

ALPACA_KEY_ID = os.environ['ALPACA_KEY_ID']
ALPACA_SECRET_KEY = os.environ['ALPACA_SECRET_KEY']
# Change to https://api.alpaca.markets for live
BASE_URL = 'https://paper-api.alpaca.markets'

CHAT_ID = 'XXXXXXXX'
TOKEN = os.environ['TELEGRAM_TOKEN']


def get_finance_data():
    google = yf.Ticker("GOOG")
    
    df = google.history(period='1d', interval="1m")[['Low']]
    df['date'] = pd.to_datetime(df.index).time
    df.set_index('date', inplace=True)

    return df


def get_forecast():
    df = get_finance_data()

    # Assuming that we've properly trained the model before and that the 
    # hyperparameters are correctly tweaked, we use the full dataset to fit
    y = df['Low'].values
    model = ARIMA(y, order=(5,0,1)).fit()
    forecast = model.forecast(steps=1)[0]

    # Returning the last real data and the forecast for the next minute
    return (y[len(y)-1], forecast)


def trade_robinhood():
    timed_otp = pyotp.TOTP(RH_MFA_CODE).now()
    login = rh.login(RH_USER_EMAIL, RH_PASSWORD, mfa_code=totp)

    last_real_data, forecast = get_forecast()

    # Your code to decide if you want to buy or sell 
    # (and the number of shares) goes here
    action = 'BUY' # or 'SELL', or 'HOLD', or...
    shares = 1

    if action == 'BUY':
        rh.order_buy_market('GOOG', shares)
        return f'Bought {shares} shares.'
    elif action == 'SELL':
        rh.order_sell_market('GOOG', shares)
        return f'Sold {shares} shares.'
    else:
        return f'No shares were bought nor sold.'


def trade_alpaca():
    api = alpaca.REST(ALPACA_KEY_ID, ALPACA_SECRET_KEY, base_url=BASE_URL)

    last_real_data, forecast = get_forecast()

    # Your code to decide if you want to buy or sell 
    # (and the number of shares) goes here
    action = 'BUY' # or 'SELL', or 'HOLD', or...
    shares = 1

    if action == 'BUY':
        api.submit_order(symbol='GOOG', qty=shares, side='buy', type='market', time_in_force='day')
        return f'Bought {shares} shares.'
    elif action == 'SELL':
        api.submit_order(symbol='GOOG', qty=shares, side='sell', type='market', time_in_force='day')
        return f'Sold {shares} shares.'
    else:
        return f'No shares were bought nor sold.'


def send_message(event, context):
    action_performed = trade_alpaca() # or trade_robinhood()

    bot = telegram.Bot(token=TOKEN)
    bot.sendMessage(chat_id=CHAT_ID, text=action_performed)
