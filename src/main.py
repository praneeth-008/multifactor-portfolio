import pandas as pd
import numpy as np
from factors import value, quality, size, esg, momentum12m, volatility
from price_data import download_prices
from factor_portfolio import factor_portfolio
from final_portfolio import combine_factor_returns, evaluate_portfolio

fundamentals = pd.read_csv(r"C:\Users\prane\Downloads\spx all vlaues.csv")
fundamentals.columns = fundamentals.columns.str.strip()
fundamentals["Ticker"] = fundamentals["Ticker"].str.split().str[0]
fundamentals = fundamentals.set_index("Ticker")
fundamentals.index = fundamentals.index.str.replace("/", "-", regex=False)

tickers = fundamentals.index.tolist()
prices, returns = download_prices(tickers)

momentum_factor = momentum12m()
momentum_scores = momentum_factor.score(returns)
volatility_factor = volatility()
volatility_scores = volatility_factor.score(returns)
value_factor = value()
value_scores = value_factor.score(fundamentals)
quality_factor = quality()
quality_scores = quality_factor.score(fundamentals)
market_cap_factor = size()
size_score = market_cap_factor.score(fundamentals)
esg_factor = esg()
esg_scores = esg_factor.score(fundamentals)

def run_factor(name, scores):
    port = factor_portfolio(
        name=name,
        prices=prices,
        factor_scores=scores,
        top_n=25
    )
    port.build()
    r = port.compute_returns()
    print(port.characteristics())
    return r

moment_port_returns = run_factor("momentum portfolio", momentum_scores)
vol_port_returns = run_factor("volatility portfolio", volatility_scores)
value_port_returns = run_factor("value portfolio", value_scores)
quality_port_returns = run_factor("quality_scores", quality_scores)
size_port_returns = run_factor("size portfolio", size_score)
esg_port_return = run_factor("Esg portfolio", esg_scores)

factor_returns = {
    "momentum": moment_port_returns,
    "volatility":vol_port_returns ,
    "value": value_port_returns,
    "quality": quality_port_returns ,
    "size": size_port_returns ,
    "esg": esg_port_return
}

factor_weights = {
    "momentum": 1/6,
    "volatility": 1/6,
    "value": 1/6,
    "quality": 1/6,
    "size": 1/6,
    "esg": 1/6
}


final_returns = combine_factor_returns(factor_returns, factor_weights)
final_stats = evaluate_portfolio(final_returns, freq=252)

moment_port_returns.to_csv("momentum_returns.csv")
vol_port_returns.to_csv("volatility_returns.csv")
value_port_returns.to_csv("value_returns.csv")
quality_port_returns.to_csv("quality_returns.csv")
size_port_returns.to_csv("size_returns.csv")
esg_port_return.to_csv("esg_returns.csv")
final_returns.to_csv("final_portfolio_returns.csv")

print(final_stats)




