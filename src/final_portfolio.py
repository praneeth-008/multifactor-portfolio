import pandas as pd
import numpy as np

def combine_factor_returns(factor_returns: dict, factor_weights: dict, normalize: bool = True) -> pd.Series:
    factor_rets_df = pd.DataFrame(factor_returns)
    w = pd.Series(factor_weights).reindex(factor_rets_df.columns).fillna(0.0)
    if normalize and w.sum() != 0:
        w = w / w.sum()
    final_returns = (factor_rets_df * w).sum(axis=1)
    return final_returns
def evaluate_portfolio(r: pd.Series, rf: float = 0.0, freq: int = 0) -> dict:
    r = r.dropna()
    mu = r.mean() * freq
    vol = r.std() * np.sqrt(freq)
    sharpe = (mu - rf) / (vol if vol != 0 else np.nan)
    eq = (1 + r).cumprod()
    peak = eq.cummax()
    dd = eq / peak - 1
    mdd = dd.min()
    return {
        "AnnReturn": mu,
        "AnnVol": vol,
        "Sharpe": sharpe,
        "MaxDrawdown": mdd
    }