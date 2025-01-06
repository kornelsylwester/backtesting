from strategy_1_2_2025_2 import strategy
from data import market_data
import pandas as pd
from global_parameters import increment, exchange_fee, start_time_timestamp, end_time_timestamp, stop_loss_percentage

starting_time = start_time_timestamp # starting+current time is LESS than endtime - end time is in the 'future', start time is the 'past'
end_time = end_time_timestamp
current_time = starting_time
current_row = market_data[market_data['start'] == current_time]



current_index = 0
cash = 1000
crypto = 0
current_price = 0
capital = cash + (crypto*current_price)


def buy(cash, crypto, price):
    acquired_crypto = cash/price
    crypto = crypto + acquired_crypto
    cash = 0
    return cash*(1-exchange_fee), crypto*(1-exchange_fee)

def sell(cash, crypto, price):
    acquired_cash = crypto*price
    cash = cash + acquired_cash
    crypto = 0
    return cash*(1-exchange_fee), crypto*(1-exchange_fee)

def do_nothing(cash, crypto, price):
    pass

# strategy_switch = {
#     'buy': buy,
#     'sell': sell,
#     'do_nothing': do_nothing,
# }

def get_next_index (i):
    return i+1

def get_current_price (market_data, current_time):
    price = market_data[market_data['start'] == current_time]['open'].values[0]
    return price
counter = 1
stop_loss_price = get_current_price(market_data, current_time) * stop_loss_percentage
while current_time <= end_time:
    try:
        current_action = strategy(current_time)

        current_price = get_current_price(market_data, current_time)
        
        if (stop_loss_price >= current_price)&(crypto>10):
            cash, crypto = sell(cash,crypto,current_price)
            print('STOP LOSS SELL')
        elif (current_action == 'buy')&(cash>10):
            cash, crypto = buy(cash,crypto,current_price)
            stop_loss_price = current_price * 0.99

        elif (current_action == 'sell')&(crypto>10):
            cash, crypto = sell(cash,crypto,current_price)
        else:
            pass

        capital = cash + (crypto*current_price)
        print(f'cash:{cash} crypto:{crypto} capital:{capital} action:{current_action} timestamp:{current_time} price: {current_price}')

        current_time += 60*increment
        current_row = market_data[market_data['start'] == current_time]
        counter += 1
    except IndexError:
        current_time += 60*increment
# for i in range(len(market_data)):
    

#     current_price = get_current_price(market_data, current_index)

#     current_action = strategy(current_price)

#     strategy_switch.get(current_action)(cash,crypto,current_price)

#     capital = cash + (crypto*current_price)
#     print(cash, crypto, capital, current_price)
#     current_index = get_next_index(current_index)