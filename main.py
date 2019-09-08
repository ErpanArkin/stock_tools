#!/usr/bin/env python3

from stock_tools.position_sizing import position
import argparse

parser = argparse.ArgumentParser(description='Stock tools')
parser.add_argument('net_cap',help='total net liquidation', type=float)
parser.add_argument('entry_price',help='entry price for the trade per share', type=float)
parser.add_argument('stop_loss',help='stop loss for the trade per share', type=float)
parser.add_argument('-r', '--risk', dest='risk_per_share', help='risk per share in percentage', default = 1.0, type=float)

args = parser.parse_args()

print('total net liquidation: {}, entry price: {}, stop loss: {}, risk per share: {}%'.format(
       args.net_cap, args.entry_price, args.stop_loss, args.risk_per_share ))
print('number of shares are {}'.format(position(args.net_cap, args.entry_price, args.stop_loss, args.risk_per_share / 100 )))