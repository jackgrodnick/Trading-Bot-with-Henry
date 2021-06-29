from config import *
import json
import time
import alpaca_trade_api as tradeapi
from tradingview_ta import TA_Handler, Interval, Exchange

while 1 == 1:

    alpaca_endpoint = 'https://paper-api.alpaca.markets'


    api = tradeapi.REST(API_KEY, SECRET_KEY, alpaca_endpoint, api_version='v2')



    #print(account.status)

    #print(account)

    lines = open("data/NASDAQsmall.csv").readlines()

    #for line in lines:
        #print(line)

    symbolsinqqqm = [line.split(",")[0] for line in lines][1:]

    #print(symbolsinqqqm)

    clock = api.get_clock()


    def buyorders(ticker, quantity):
        api.submit_order(
        symbol=ticker,
        qty=quantity,
        side='buy',
        type='market',
        time_in_force='gtc'
    )

    def sellorders(ticker, quantity):
        api.submit_order(
        symbol=ticker,
        qty=quantity,
        side='sell',
        type='market',
        time_in_force='gtc'
    )
    #clock.is_open

    #position = tradeapi.REST(API_KEY, SECRET_KEY, 'https://paper-api.alpaca.markets/v2/positions/AAPL')

    #position = api.get_position('AAPL')

    #print(position)

    #asset = api.get_asset('AAPL')
    #print(asset.exchange)

    printcount = 0


    while clock.is_open:
        for symbol in symbolsinqqqm:

            try:
                clock = api.get_clock()
            except:
                if not clock.is_open:
                    break
                continue

            printcount += 1
            
            try:
                account = api.get_account()
            except:
                if not clock.is_open:
                    break
                continue
            #asset = tradeapi.REST(API_KEY, SECRET_KEY, 'https://paper-api.alpaca.markets/v2/assets/{}'.format(symbol.strip()))
            
            #print(asset)

            try:
                asset = api.get_asset('{}'.format(symbol.strip()))
                stock = TA_Handler(
                    symbol='{}'.format(symbol.strip()),
                    screener="america",
                    exchange=asset.exchange,
                    interval=Interval.INTERVAL_1_DAY
                )
            except:
                if not clock.is_open:
                    break
                continue

            try:
                if stock.get_analysis().summary['RECOMMENDATION'] == "BUY" and float(account.cash) > 0:
                    buyorders('{}'.format(symbol.strip()), 1)
            except:
                if not clock.is_open:
                    break
                continue

            

            try:
                position = api.get_position('{}'.format(symbol.strip()))
                if position.symbol == symbol.strip() and stock.get_analysis().summary['RECOMMENDATION'] == "SELL":
                    sellorders('{}'.format(symbol.strip()), int(position.qty))
            except:
                if not clock.is_open:
                    break
                continue
        #add this back later maybe.
        #if float(account.cash) <= 0:
            #break
        


    #tick = str(input("enter the ticker you want to buy ")).strip()

    #quantity = str(input("enter the quantity of stock you want to buy ")).strip()
    account = api.get_account()
    #position = tradeapi.REST(API_KEY, SECRET_KEY, 'https://paper-api.alpaca.markets/v2/positions')
    #buyorders(tick, int(quantity))
    #print(account.cash)
    #print(json.dumps(tradeapi.REST(API_KEY, SECRET_KEY, 'https://paper-api.alpaca.markets/v2/positions/aapl}', api_version='v2')))




    if printcount > 0:
        print('Percent Change of Account Today: ' + str(((float(account.equity) - float(account.last_equity))/float(account.equity))*100) + '%')


    time.sleep(60)