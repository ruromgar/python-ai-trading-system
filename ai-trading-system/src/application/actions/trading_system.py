import asyncio

import pandas as pd
import numpy as np

from statsmodels.tsa.arima.model import ARIMA


class TradingSystem:
    def __init__(self, logger, config, yahoo_repository, ai_repository, alpaca_repository):
        self._config = config
        self._logger = logger

        self._yahoo_repository = yahoo_repository
        self._ai_repository = ai_repository
        self._alpaca_repository = alpaca_repository

    async def monitoring(self, seconds, exec_on_start):
        if not exec_on_start:
            await asyncio.sleep(seconds)

        while True:
            self._alpaca_repository.is_market_open()
            await asyncio.sleep(seconds)
