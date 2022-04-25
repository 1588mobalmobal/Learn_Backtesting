import ccxt
import time
import pandas as pd
import pprint as pp
import numpy as np
from datetime import datetime

access = 'Fofo123nKyvG7b1vHS4dxExFHsszf0ZEDgG5mFhGfGp37MpvvNe5qc6IOMyHAozJ'
secret = 'lt4qHHwGHb2sJhfYe84u6F8DzjWfnPv8KP4z4nBYW1mgB7adTmDD8trpB2Su59Zo'

binance = ccxt.binance(config={
    'apiKey' : access,
    'secret' : secret,
    'enableRateLimit' : True,
    'options' : {
        'defaultType' : 'future'
    }
})


target_coin_ticker = "BTC/USDT"
target_coin_symbol = "BTCUSDT"


btc = binance.fetch_ohlcv(target_coin_ticker, '1d')
date_list = []

for ohlcv in btc:
    date = datetime.fromtimestamp(ohlcv[0]/1000).strftime('%Y-%m-%d %H:%M:%S')
    date_list.append(date)

s = pd.Series(date_list)
df = pd.DataFrame(btc, columns=['date','open', 'high', 'low', 'close','volume'])
df1 = df.drop(['date'], axis=1)
df1['date'] = s
df1 = df1.set_index('date')

print(df1)


# df_data = df.set_index('date')


# print(df_data)