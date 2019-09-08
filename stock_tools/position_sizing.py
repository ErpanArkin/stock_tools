
'''
This function gives the number of shares one should buy based on the net liquidation: net_cap,
entry price, stop loss, and the risk per share which is default to 1%
'''

def position(net_cap, entry_price, stop_loss, risk_per_share = 0.01):
    shares = net_cap * risk_per_share / (entry_price - stop_loss)
    return round(shares)