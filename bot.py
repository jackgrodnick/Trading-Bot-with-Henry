#import requests
#from config import *

#BASE_URL = 'https://paper-api.alpaca.markets'

#ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)

#r = requests.get(ACCOUNT_URL, headers={'APCA_API_KEY_ID': 'PK2M9NVUQKL2D0ELISAG', 'APCA-API-SECRET-KEY': 'iJ8458XwS1sHo0IpFk6EOLJJjv93FiiLPqZ9jtAT'})

#print(r.content)

print("test")

import alpaca_trade_api as tradeapi

alpaca_endpoint = 'https://paper-api.alpaca.markets'

api = tradeapi.REST('PK2M9NVUQKL2D0ELISAG', 'iJ8458XwS1sHo0IpFk6EOLJJjv93FiiLPqZ9jtAT', alpaca_endpoint)

account = api.get_account()


print(account.status)
