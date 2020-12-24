import pandas as pd
import numpy as np

from statsmodels.tsa.arima.model import ARIMA


class TradingSystem:
    def __init__(self, logger, config, yahoo_repository):
        self._config = config
        self._logger = logger

        self._yahoo_repository = yahoo_repository

    async def monitoring(self, seconds, exec_on_start):
        if not exec_on_start:
            await asyncio.sleep(seconds)

        while True:
            last_movements = self._yahoo_repository.get_finance_data()

            if last_movements is None:
                self._logger.info(f'No new movements')
            else:
                self._logger.info(last_movements)                    

            await asyncio.sleep(seconds)

    def get_forecast():
        df = get_finance_data()

        # Assuming that we've properly trained the model before and that the 
        # hyperparameters are correctly tweaked, we use the full dataset to fit
        y = df['Low'].values
        model = ARIMA(y, order=(5,0,1)).fit()
        forecast = model.forecast(steps=1)[0]

        # Returning the last real data and the forecast for the next minute
        return (y[len(y)-1], forecast)
