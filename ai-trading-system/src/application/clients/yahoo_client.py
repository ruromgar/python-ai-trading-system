import yfinance as yf
import pandas as pd


class YahooClient:
    def __init__(self, logger, config):
        self._config = config
        self._logger = logger

    def get_finance_data(self):
        self._logger.info('Getting data from Yahoo Finance...')

        google = yf.Ticker("GOOG")        
        df = google.history(period='5d', interval="1m")[['Low']]
        self._logger.info(f'Data found. Last value dated on {df.index[-1]}')
        df['date'] = pd.to_datetime(df.index).time
        df.set_index('date', inplace=True)

        return df
