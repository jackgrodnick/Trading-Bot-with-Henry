# Name of project: Trading-Bot-with-Henry. This trading bot uses an API from alpaca to paper trade stocks based on analyst's recommendations on whether to buy or sell a stock based on trading views API. First, the trading bot checks to make sure the market is open. If the market is open, it then iterates through a CSV file that I downloaded through invesco.com that contains a bunch of companies listed in the NASDAQ. If analysts say any of the stocks listed in the CSV file are a buy, my bot will continue buying one share at a time of the company until I no longer have cash left in my alpaca paper trading account. It also continuously iterates through my portfolio to check if analysts change their recommendation to a sell and then sells all the stock out of my portfolio. At the end of a trading day, the bot will print the percent change in equity of my paper trading account. The bot will also stop trading once I start getting into margin in my account.