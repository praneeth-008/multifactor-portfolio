import pandas as pd
import numpy as np

class factor_portfolio:
    def __init__(self, name, prices, factor_scores, top_n = 25, weights = None):
        self.name = name
        self.prices = prices
        self.factor_scores = factor_scores
        self.top_n = top_n
        self.weights = weights
        self.portfolio_returns = None  # Initialize to avoid AttributeError
    def build(self):
        if self.factor_scores is None:
            raise ValueError("Factor scores not provided. Cannot build portfolio.")
        top_stocks = self.factor_scores.sort_values(ascending=False)[:self.top_n]
        self.weights = pd.Series(1/self.top_n, index=top_stocks.index)
        return self.weights

    def compute_returns(self):
        if self.weights is None:
            raise ValueError("Portfolio weights not defined. Run build() first.")
        top_prices = self.prices[self.weights.index]
        returns = top_prices.pct_change().dropna()
        self.portfolio_returns = (returns*self.weights).sum(axis = 1)
        return self.portfolio_returns

    def characteristics(self, rf = 0 , freq = 252):
        if self.portfolio_returns is None:
            raise ValueError("No portfolio returns found. Run compute_returns() first.")
        mean_return = self.portfolio_returns.mean()*freq
        volatility = self.portfolio_returns.std() * np.sqrt(freq)
        sharpe = (mean_return-rf)/volatility

        cumulative = (1 + self.portfolio_returns).cumprod()
        drawdown = cumulative / cumulative.cummax() - 1
        max_drawdown = drawdown.min()

        return {
            'Portfolio': self.name,
            'Annual Return': mean_return,
            'Volatility': volatility,
            'Sharpe Ratio': sharpe,
            'Max Drawdown': max_drawdown
        }

