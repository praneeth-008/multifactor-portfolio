import pandas as pd
import numpy as np

class factor_portfolio:
    def __init__(self, name, returns, factor_scores, top_n = 25, weights = None):
        self.name = name
        self.returns = returns
        self.factor_scores = factor_scores
        self.top_n = top_n
        self.weights = weights
    def build(self):
        if self.factor_scores is not None:
            top_stocks = self.factor_scores.sort_values(ascending=False)[:self.top_n]
        self.weights = pd.series(1/self.top_n , index = top_stocks.index)
        return self.weights

    def returns(self):

