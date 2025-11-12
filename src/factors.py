import pandas as pd
import numpy as np

class momentum12m:    # momentum is calculated
    def __init__(self, calculated_days = 252, skip_days= 21):# we use the last 252 days to calculate return and skip the last 21 days
        self.calculated_days = claculated_days
        self.skip_days = skip_days

    def score(self, price):
        returns = price.pct_change  #computes daily returns using pct_change
        r252 = (returns + 1).iloc[-self.calculated_days:].prod() - 1 #this calculates the returns of the last 252 days
        r21 = (returns + 1).iloc[-self.skip_days:].prod() - 1 # calculate the returns of the last 21 days(one month)

        momentum = r252 - r21 #(subract them to get clean data)
        return momentum


class value:   # to find the value of a company we use pe ratio
    def __init__(self, metric="PE"): # the metric we will be using is PE
        self.metric = metric

    def score(self, fundamentals):
        if self.metric not in fundamentals:
            print (f" '{self.metric}' not found") # if column PE is not found we will get this output
            return pd.Series(dtype=float)
        PE = fundamentals[self.metric].astype(float)

        value_score = 1/PE # since for pe lower is better we inverse it so higher is better
        return value_score.sort_values(ascending=False)# getting our scores from higher to lower


class quality:#for quality score we find the mean of return on equity and assets
    def __init__(self, metric=["ROE","ROA"]):
        self.metric = metric
    def score(self, fundamentals): #this code might be wrong gotta look at it again and chang it
        for m in self.metric:
            if m not in fundamentals:
                print (f" '{self.metric}' not found")
                return pd.Series(dtype=float)

        roe = fundamentals["ROE"].astype(float)
        roa = fundamentals["ROA"].astype(float)
        quality_score = (roe+roa)/2
        return quality_score.sort_values(ascending=False)

class volatality:
    def __init__(self, calculated_days = 252): # we define days to calculate volatilty for the last one year
        self.calculated_days = calculated_days

    def score(self, price):

        returns = price.pct_change().dropna() #calculates returns
        volatility = returns.std()  # volatility is standard  deviation of returns
        annual_volatility = volatility * np.sqrt(self.calculated_days) # we anualize the volatility
        vol_score = 1/annual_volatility #taking inverse as lower is better
        return vol_score.sort_values(ascending=False)

class size:
    def __init__(self, metric = "MarketCap" ):
        self.metric = metric

    def score(self, fundamentals):
        if self.metric not in fundamentals:
            print (f" '{self.metric}' not found")
            return pd.Series(dtype=float)
        market_cap = fundamentals[self.metric].astype(float)
        market_cap_score = 1/market_cap
        return market_cap_score.sort_values(ascending=False)


class esg:
    def __init__(self, metric="ESG_Score"):
        self.metric = metric

    def score(self, fundamentals):
        if self.metric not in fundamentals:
            print(f"{self.metric} not found")
            return pd.Series(dtype=float)

        esg_score = fundamentals[self.metric].astype(float)
        return esg_score.sort_values(ascending=False)





