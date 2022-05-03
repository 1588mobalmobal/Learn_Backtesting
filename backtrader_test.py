import backtrader as bt
from datetime import datetime

class firstStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.indicators.RSI_SMA(self.data.close, period=21)

    def next(self):
        if not self.position:
            if self.rsi < 30:
                self.buy(size=100)
        else:
            if self.rsi > 70:
                self.sell(size=100)


#Variable for our starting cash
startcash = 10000

#Create an instance of cerebro
cerebro = bt.Cerebro()

#Add our strategy
cerebro.addstrategy(firstStrategy)

#Get Apple data from Yahoo Finance.

# data = bt.feeds.Quandl(
#     dataname='AAPL',
#     fromdate = datetime(2015,1,1),
#     todate = datetime(2017,1,1),
#     buffered= True
#     )

data = bt.feeds.GenericCSVData(
    dataname = 'test03.csv' ,
    fromdate = datetime(2020,12,15),
    todate = datetime(2021,4,25),

    nullvalue = 0.0,

    dtformat=('%Y-%m-%d %H:%M:%S'),

    datetime=0,
    open=1,
    high=2,
    low=3,
    close=4,
    volume=5
)

#Add the data to Cerebro
cerebro.adddata(data)

# Set our desired cash start
cerebro.broker.setcash(startcash)

# Run over everything
cerebro.run()

#Get final portfolio Value
portvalue = cerebro.broker.getvalue()
pnl = portvalue - startcash

#Print out the final result
print('Final Portfolio Value: ${}'.format(portvalue))
print('P/L: ${}'.format(pnl))

#Finally plot the end results
cerebro.plot(style='candlestick')