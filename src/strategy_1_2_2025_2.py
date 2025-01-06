from data import market_data
import pandas as pd
from rolling_mean import rolling_mean
from global_parameters import increment

def strategy(timestamp): #Returns 'buy', 'sell', or 'do_nothing'
    try:
        #calculate indicators
        price = market_data[market_data['start'] == timestamp]['open'].values[0]
        current_rolling_5_mean = rolling_mean(timestamp, 5)
        current_rolling_30_mean = rolling_mean(timestamp, 30)

        if abs((price-current_rolling_30_mean)/price) < 0.012:
            return 'do_nothing'
        if price > current_rolling_30_mean*(1.04):
            # print(f'buying at price: {price}')
            # print(f'BUY: current price:{price} current rolling 5 mean:{current_rolling_5_mean}')
            return 'buy'
        if current_rolling_5_mean*(0.99) > price:
            # print(f'selling at price: {price}')
            # print(f'rolling 5 mean is: {current_rolling_5_mean}')
            # print(f'SELL: current price:{price} current rolling 5 mean:{current_rolling_5_mean}')
            return 'sell'
        else:
            # print(f'waiting... at price: {price}')
            # print(f'DO NOTHING: current price:{price} current rolling 5 mean:{current_rolling_5_mean}')
            return 'do_nothing'
    except IndexError:
        print('index bullshit')
        return 'do_nothing'
