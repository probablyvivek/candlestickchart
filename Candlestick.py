#Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web
import mplfinance as mpf
import datetime as dt

#Input the Stock
ticker = 'AAPL'

#Start and End Date of the Stock
start = dt.datetime(2021,1,1)
end = dt.datetime.now()

#Getting the Data 
data = web.DataReader(ticker, 'yahoo', start, end)

#Getting the right theme
colors = mpf.make_marketcolors(up="##b92b27",down="##1db954",wick="inherit",edge="inherit",volume="in")
mpf_style = mpf.make_mpf_style(base_mpf_style="nightclouds", marketcolors=colors)

#Plotting the Data on the theme
fig, axes = mpf.plot(data, type='candle', style=mpf_style, volume=True, returnfig=True)
axes[0].set_title(f"Price from {start} to {end} of {ticker}")
fig.show()


