import alpaca_trade_api as alpaca


class AlpacaClient:
    def __init__(self, logger, config):
        self._config = config
        self._logger = logger

        self._key_id = self._config.ALPACA_CONFIG['key_id']
        self._secret_key = self._config.ALPACA_CONFIG['secret_key']
        self._base_url = self._config.ALPACA_CONFIG['base_url']

        self._api = alpaca.REST(self._key_id, self._secret_key, base_url=self._base_url)

    def get_account_info(self):
        account = self._api.get_account()
        print(
            f'The buying power is {acc.buying_power} {acc.currency} '
            f'and the equity is {acc.equity} {acc.currency}\n'
            f'The account status is {account.status}'
        )

    def is_market_open(self):
        clock = self._api.get_clock()
        return clock.is_open

    def get_prices(self, asset_symbol):
        # Get daily price data for GOOG over the last 5 trading days.
        barset = self._api.get_barset('GOOG', 'day', limit=5)
        bars = barset['GOOG']

        # See how much GOOG moved in that timeframe.
        week_open = bars[0].o
        week_close = bars[-1].c
        percent_change = (week_close - week_open) / week_open * 100
        print(f'GOOG moved {percent_change}% over the last 5 days')

    def get_portfolio(self):
        # Get a list of all of our positions.
        portfolio = self._api.list_positions()

        # Get our position in GOOG.
        position = self._api.get_position('GOOG')

    def trade_alpaca(self, last_real_data, forecast):
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
