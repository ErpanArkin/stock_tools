#!/usr/bin/env python3

from stock_tools.position_sizing import position

net_cap = 1000; entry_price = 10.0; stop_loss = 9.80;

print('number of shares are {}'.format(position(net_cap, entry_price, stop_loss)))