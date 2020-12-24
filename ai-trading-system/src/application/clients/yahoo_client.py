import yfinance as yf
import pandas as pd


class YahooClient:
    def __init__(self, logger, config):
        self._config = config
        self._logger = logger

    def get_finance_data():
        logger.info('Getting data from Yahoo Finance...')

        google = yf.Ticker("GOOG")        
        df = google.history(period='5d', interval="1m")[['Low']]
        df['date'] = pd.to_datetime(df.index).time
        df.set_index('date', inplace=True)
        return df.shape
