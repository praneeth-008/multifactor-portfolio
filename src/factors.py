import pandas as pd
import numpy as np

class momentum12m:    # momentum is calculated
    def __init__(self, calculated_days = 252, skip_days= 21):# we use the last 252 days to calculate return and skip the last 21 days
        self.calculated_days = calculated_days
        self.skip_days = skip_days

    def score(self, returns):
        r252 = (returns + 1).iloc[-self.calculated_days:].prod() - 1  #this calculates the returns of the last 252 days
        r21 = (returns + 1).iloc[-self.skip_days:].prod() - 1  # calculate the returns of the last 21 days(one month)

        momentum_score = r252 - r21 # subract them to get clean data
        momentum_score = momentum_score.dropna()

        return momentum_score.sort_values(ascending=False)


class value:   # to find the value of a company we use pe ratio
    def __init__(self, metric="PE"): # the metric we will be using is PE
        self.metric = metric

    def score(self, fundamentals):
        if self.metric not in fundamentals:
            print (f" '{self.metric}' not found") # if column PE is not found we will get this output
            return pd.Series(dtype=float)
        PE = pd.to_numeric(fundamentals[self.metric], errors="coerce")
        PE = PE.dropna()

        value_score = 1/PE # since for pe lower is better we inverse it so higher is better
        return value_score.sort_values(ascending=False)# getting our scores from higher to lower


class quality:
    def __init__(self, metric=["ROE LF", "ROA LF"]):
        self.metric = metric

    def score(self, fundamentals):

        for m in self.metric:
            if m not in fundamentals:
                print(f"'{m}' not found")
                return pd.Series(dtype=float)

        roe = pd.to_numeric(fundamentals["ROE LF"], errors="coerce")
        roa = pd.to_numeric(fundamentals["ROA LF"], errors="coerce")

        quality_score = (roe + roa) / 2

        quality_score = quality_score.dropna()

        return quality_score.sort_values(ascending=False)


class volatility:
    def __init__(self, calculated_days = 252): # we define days to calculate volatilty for the last one year
        self.calculated_days = calculated_days

    def score(self,returns):
        recent_returns = returns.iloc[-self.calculated_days:]

        volatility = recent_returns.std()  # volatility is standard  deviation of returns
        annual_volatility = volatility * np.sqrt(self.calculated_days) # we anualize the volatility
        vol_score = 1/annual_volatility #taking inverse as lower is better
        vol_score = vol_score.dropna()
        return vol_score.sort_values(ascending=False)

class size:
    def __init__(self, metric = "Market Cap" ):
        self.metric = metric

    def score(self, fundamentals):
        if self.metric not in fundamentals:
            print (f" '{self.metric}' not found")
            return pd.Series(dtype=float)
        market_cap = pd.to_numeric(fundamentals[self.metric] , errors="coerce")
        market_cap = market_cap.dropna()
        market_cap_score = 1/market_cap
        return market_cap_score.sort_values(ascending=False)


class esg:
    def __init__(self, metric="ESG"):
        self.metric = metric

    def score(self, fundamentals):
        if self.metric not in fundamentals:
            print(f"{self.metric} not found")
            return pd.Series(dtype=float)

        esg_score = pd.to_numeric(fundamentals[self.metric] , errors="coerce")
        esg_score = esg_score.dropna()
        return esg_score.sort_values(ascending=False)





