import yfinance as yf
import pandas as pd

def download_prices(tickers, start="2015-01-01", end=None):
    # auto_adjust=True is default → Close = Adjusted Close
    data = yf.download(tickers, start=start, end=end, group_by="ticker")

    # MULTIINDEX case (many tickers)
    if isinstance(data.columns, pd.MultiIndex):
        prices = data.xs("Close", axis=1, level=1)
    else:
        # SINGLE TICKER case
        prices = data["Close"].to_frame()

    # Drop empty tickers
    prices = prices.dropna(axis=1, how="all")

    # Fill missing values
    prices = prices.ffill().bfill()

    # Daily returns
    returns = prices.pct_change().dropna()

    return prices, returns
