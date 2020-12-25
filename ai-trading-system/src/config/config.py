import logging
import os
import sys


LOG_CONFIG = {
    'name': 'ai-trading-bridge',
    'level': logging.DEBUG,
    'stream_handler': logging.StreamHandler(sys.stdout),
    'format': '%(asctime)s: %(module)s: %(levelname)s: %(message)s'
}

POLLING_CONFIG = {
    'yahoo_interval': 30,
}

ROBINHOOD_CONFIG = {
    'mail': os.environ['RH_USER_EMAIL'],
    'password': os.environ['RH_PASSWORD'],
    'mfa': os.environ['RH_MFA_CODE']
}

ALPACA_CONFIG = {
    'key_id': os.environ['ALPACA_KEY_ID'],
    'secret_key': os.environ['ALPACA_SECRET_KEY'],
    # Change to https://api.alpaca.markets for live
    'base_url': 'https://paper-api.alpaca.markets'
}
