import pandas as pd
import numpy as np
from factors import value, quality, size, esg
from price_data import download_prices

fundamentals = pd.read_csv(r"C:\Users\prane\Downloads\spx all vlaues.csv")
fundamentals.columns = fundamentals.columns.str.strip()
fundamentals["Ticker"] = fundamentals["Ticker"].str.split().str[0]
fundamentals = fundamentals.set_index("Ticker")
fundamentals.index = fundamentals.index.str.replace("/", "-", regex=False)
# using the above line because our data was downloaded from bloomberg as since we are using yfinace to get prices
# we need to replace these values for y finance to understand a few tickers 'BRK/B', 'BF/B' both these tickers specifically

tickers = fundamentals.index.tolist()
prices = download_prices(tickers)

value_factor = value()
value_scores = value_factor.score(fundamentals)
quality_factor = quality()
quality_scores = quality_factor.score(fundamentals)
market_cap_factor = size()
size_score = market_cap_factor.score(fundamentals)
esg_factor = esg()
esg_scores = esg_factor.score(fundamentals)








