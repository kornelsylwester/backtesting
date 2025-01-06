from data import market_data
from global_parameters import increment

def rolling_mean(timestamp, window):
    sum = 0
    for i in range(window):
        price = market_data[market_data['start'] == (timestamp-60*(i+1)*increment)]['open'].values[0]
        sum += price
    #     print(f'current time:{timestamp}, current price:{price}, current sum:{sum}')
    # print(f"price: {price}, window:{window}")
    return sum/window
