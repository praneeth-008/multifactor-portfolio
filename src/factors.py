import pandas as pd
import numpy as np

class momentum12m:
    def __init__(self, calculated_days = 252, skip_days= 21):
        self.calculated_days = claculated_days
        self.skip_days = skip_days

    def score(self, price):
        returns = price.pct_change  #computes daily returns
        r252 = (returns + 1).iloc[-self.calculated_days:].prod() - 1
        r21 = (returns + 1).iloc[-self.skip_days:].prod() - 1

momentum = r252 - r21
return momentum




