class AIRepository:
    def __init__(self, logger, config, ai_client):
        self._config = config
        self._logger = logger

        self._ai_client = ai_client

    def get_forecast(self, finance_data):
        return self._ai_client.get_forecast(finance_data)