stock_prices_yesterday = [10, 7, 5, 8, 11, 9, 3, 10, 3, 21, 18, 17, 20, 4, 2, 10, 12, 19]
stock_prices_yesterday2 = [11, 10, 9, 8]


def get_max_profit(stock):
    vmin = stock[0]
    vmax = stock[0]
    profit = stock[1]-stock[0]
    max_profit = stock[1]-stock[0]
    for i, price in enumerate(stock):
        if price > vmax:
            vmax = price
        if price <= vmin:
            if(i+1 != len(stock)): 
                vmax = stock[i+1]
            vmin = price
        if(vmin != vmax): 
            profit = vmax-vmin
            print('profit:', profit)
        if profit > max_profit:
            max_profit = profit
    return max_profit

print(get_max_profit(stock_prices_yesterday))
