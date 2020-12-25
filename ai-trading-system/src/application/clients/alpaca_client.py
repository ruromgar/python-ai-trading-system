import alpaca_trade_api as alpaca


class AlpacaClient:
    def __init__(self, logger, config):
        self._config = config
        self._logger = logger

        self._key_id = self._config.ALPACA_CONFIG['key_id']
        self._secret_key = self._config.ALPACA_CONFIG['secret_key']
        self._base_url = self._config.ALPACA_CONFIG['base_url']

    def trade_alpaca(last_real_data, forecast):
        api = alpaca.REST(self._key_id, self._secret_key, base_url=self._base_url)

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
