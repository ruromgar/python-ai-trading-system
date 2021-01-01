import robin_stocks as robinhood
import pyotp


class RobinHoodClient:
    def __init__(self, logger, config):
        self._config = config
        self._logger = logger

        self._rh_mfa_code = self._config.ROBINHOOD_CONFIG['mfa']
        self._rh_user_email = self._config.ROBINHOOD_CONFIG['mail']
        self._rh_password = self._config.ROBINHOOD_CONFIG['password']

    def trade_robinhood(self, last_real_data, forecast):
        timed_otp = pyotp.TOTP(self._rh_mfa_code).now()
        login = rh.login(self._rh_user_email, self._rh_password, mfa_code=totp)

        last_real_data, forecast = get_forecast()

        # Your code to decide if you want to buy or sell 
        # (and the number of shares) goes here
        action = 'BUY' # or 'SELL', or 'HOLD', or...
        shares = 1

        if action == 'BUY':
            rh.order_buy_market('GOOG', shares)
            return f'Bought {shares} shares.'
        elif action == 'SELL':
            rh.order_sell_market('GOOG', shares)
            return f'Sold {shares} shares.'
        else:
            return f'No shares were bought nor sold.'
