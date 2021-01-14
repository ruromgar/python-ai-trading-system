class AlpacaRepository:
    def __init__(self, logger, config, alpaca_client):
        self._config = config
        self._logger = logger

        self._alpaca_client = alpaca_client

    def test(self):
        return self._alpaca_client.test()