from config import *

import alpaca_trade_api as tradeapi

alpaca_endpoint = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(API_KEY, SECRET_KEY, alpaca_endpoint)

account = api.get_account()


print(account.status)
