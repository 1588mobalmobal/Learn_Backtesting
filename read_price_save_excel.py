from numpy import save
import pandas as pd
import pprint as pp
from datetime import datetime
import basic_info

binance = basic_info.binance

target_coin_ticker = "BTC/USDT"
target_coin_symbol = "BTCUSDT"
file_name = 'test02.xlsx'


def read_ohlcv():
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

    return df1


def save_excel(df1):
    df1.to_excel(file_name)
    print(f'{file_name} has been saved successfully')


if __name__ == '__main__':
    df = read_ohlcv()
    save_excel(df)





