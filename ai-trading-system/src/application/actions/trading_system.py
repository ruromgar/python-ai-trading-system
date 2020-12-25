import asyncio

import pandas as pd
import numpy as np

from statsmodels.tsa.arima.model import ARIMA


class TradingSystem:
    def __init__(self, logger, config, yahoo_repository, ai_repository):
        self._config = config
        self._logger = logger

        self._yahoo_repository = yahoo_repository
        self._ai_repository = ai_repository

    async def monitoring(self, seconds, exec_on_start):
        if not exec_on_start:
            await asyncio.sleep(seconds)

        while True:
            finance_data = self._yahoo_repository.get_finance_data()

            if finance_data is None:
                self._logger.info(f'No new movements')
            else:
                last_real_data, forecast = self._ai_repository.get_forecast(finance_data)
                self._logger.info(f'Last data: {last_real_data} | Forecast: {forecast}')                    

            await asyncio.sleep(seconds)
