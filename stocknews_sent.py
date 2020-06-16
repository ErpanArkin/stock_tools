#!/usr/bin/env python3

from stocknews import StockNews
import sys

stocks = sys.argv[1:] # ticker symbols as arguments

sn = StockNews(stocks, wt_key='yWxIn2zm4Ajp9Uu2hfFcecyZTWqH2mTky5QqBJ0TTzAVIBdika0H75v4NySH')

df = sn.read_rss()
print(df.groupby('stock').mean())