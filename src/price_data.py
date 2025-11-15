import yfinance as yf
import pandas as pd


def download_prices(tickers, start="2015-01-01", end=None):
    data = yf.download(tickers, start=start, end=end, group_by='ticker')

    # MultiIndex case (many tickers)
    if isinstance(tickers, list) and len(tickers) > 1:
        prices = data.xs("Adj Close", axis=1, level=1)
    else:
        prices = data["Adj Close"].to_frame()

    # Drop empty tickers
    prices = prices.dropna(axis=1, how="all")

    # Forward / backward fill
    prices = prices.ffill().bfill()

    return prices

    returns = prices.pct_change().dropna(how="all")

    return prices
    return returns

