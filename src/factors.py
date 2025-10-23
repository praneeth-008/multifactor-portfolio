import pandas as pd
import numpy as np

class momentum12m:    # momentum is calculated by
    def __init__(self, calculated_days = 252, skip_days= 21):
        self.calculated_days = claculated_days
        self.skip_days = skip_days

    def score(self, price):
        returns = price.pct_change  #computes daily returns
        r252 = (returns + 1).iloc[-self.calculated_days:].prod() - 1
        r21 = (returns + 1).iloc[-self.skip_days:].prod() - 1

momentum = r252 - r21
return momentum

class value:   # to find the value of a company we use pe ratio
    def __init__(self, metric="PE"):
        self.metric = metric

    def score(self, fundamentals):
        if self.metric not in fundamentals:
            print (f" '{self.metric}' not found")
            return pd.Series(dtype=float)
        PE = fundamentals[self.metric].astype(float)

        value_score = 1/PE
        return value_score.sort_values(ascending=False)
class quality:         #for quality score we find the mean of net income on equity and assets
    def __init__(self, metric=["ROE","ROA"]):
        self.metric = metric
    def score(self, fundamentals):
        if self.metric not in fundamentals:
            print (f" '{self.metric}' not found")
            return pd.Series(dtype=float)

        roe = fundamentals["ROE"].astype(float)
        roa = fundamentals["ROA"].astype(float)
        quality_score = (roe+roa)/2
        return quality_score.sort_values(ascending=False)

class volatality:
    def __init__(self, calculated_days = 252):
        self.calculated_days = calculated_days

    def score(self, price):

        returns = price.pct_change().dropna()
        volatility = returns.std()
        annual_volatility = volatility * np.sqrt(self.calculated_days)
        vol_score = 1/annual_volatility
        return vol_score.sort_values(ascending=False)







