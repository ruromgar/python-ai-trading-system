class YahooRepository:
    def __init__(self, logger, config, yahoo_client):
        self._config = config
        self._logger = logger

        self._yahoo_client = yahoo_client

    def get_finance_data(self):
        return self._yahoo_client.get_finance_data()