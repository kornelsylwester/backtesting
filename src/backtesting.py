
prices = [23, 67.9, 76.2, 6, 61, 0.8, 66, 90]
current_index = 0
cash = 1000
crypto = 0
current_price = 0
capital = cash + (crypto*current_price)

def strategy(price): #Returns 'buy', 'sell', or 'do_nothing'
    if price < 60:
        print(f'buying! current price is {price}')
        return 'buy'
    if price > 70:
        print(f'selling! current price is {price}')
        return 'sell'
    else:
        print(f'waiting... current price is {price}')
        return 'do_nothing'
    

def buy(cash, crypto, price):
    acquired_crypto = cash/price
    crypto = crypto + acquired_crypto
    cash = 0
    return cash, crypto

def sell(cash, crypto, price):
    acquired_cash = crypto*price
    cash = cash + acquired_cash
    crypto = 0
    return cash, crypto

def get_next_index (i):
    return i+1

def get_current_price (arr, i):
    price = arr[i]
    return price

for i in range(len(prices)):
    

    current_price = get_current_price(prices, current_index)

    if strategy(current_price) == 'buy':
        cash, crypto = buy(cash, crypto, current_price)
    

    if strategy(current_price) == 'sell':
        cash, crypto = sell(cash, crypto, current_price)

    if strategy(current_price) == 'do_nothing':
        pass
    capital = cash + (crypto*current_price)
    print(cash, crypto, capital, current_price)
    current_index = get_next_index(current_index)