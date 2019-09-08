
def position(net_cap, entry_price, stop_loss, risk_per_share = 0.01):
    shares = net_cap * risk_per_share / (entry_price - stop_loss)
    return round(shares)