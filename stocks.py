import requests
import logging as log
import difflib

nonTickers = ["STOCKS", "FINANCE", "TICKERS"]

def tickersOnly(strIn):
    words = strIn.split()
    maxIndex = len(words)
    for i in range(maxIndex - 1, -1, -1):
        if len(difflib.get_close_matches(words[i], nonTickers, 1, 0.8)) > 0:
            del words[i]

    print(words)
    return words

def getStockInfo(strIn):
    #get only stock tickers
    tickers = tickersOnly(strIn.upper())

    for ticker in tickers:
        requestJSON = requests.get("https://www.quandl.com/api/v3/datasets/EOD/{}.csv?api_key=oJCyqXpnD7HhA8Th7xNQ".format(ticker))
        dailyData = requestJSON.text

        #get only most recent day's stock data
        dailyData = dailyData[dailyData.index("\n") + 1:]
        dailyData = dailyData[:dailyData.index("\n")]

        if "Quandl" in dailyData:
            log.info("stocks.py: ticker not real: " + ticker)
        else:
            print(dailyData)

getStockInfo("   stocks aapl goog tickers tsla   asfsef ")
