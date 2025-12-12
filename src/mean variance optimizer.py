import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

momentum = pd.read_csv("momentum_returns.csv", index_col=0, parse_dates=True)
volatility = pd.read_csv("volatility_returns.csv", index_col=0, parse_dates=True)
value = pd.read_csv("value_returns.csv", index_col=0, parse_dates=True)
quality = pd.read_csv("quality_returns.csv", index_col=0, parse_dates=True)
size = pd.read_csv("size_returns.csv", index_col=0, parse_dates=True)
esg = pd.read_csv("esg_returns.csv", index_col=0, parse_dates=True)

factors = pd.concat([momentum, volatility, value, quality, size, esg], axis=1)
factors.columns = ["Momentum", "Volatility", "Value", "Quality", "Size", "ESG"]

mu = factors.mean()
cov = factors.cov()

n = len(mu)
num_portfolios = 50000

results = {
    "Returns": [],
    "Volatility": [],
    "Sharpe": [],
    "Weights": []
}

# RANDOM PORTFOLIOS
for _ in range(num_portfolios):
    w = np.random.random(n)
    w /= w.sum()

    port_return = np.dot(w, mu) * 252
    port_vol = np.sqrt(np.dot(w.T, np.dot(cov * 252, w)))
    sharpe = port_return / port_vol

    results["Returns"].append(port_return)
    results["Volatility"].append(port_vol)
    results["Sharpe"].append(sharpe)
    results["Weights"].append(w)

results = pd.DataFrame(results)

max_sharpe_index = results["Sharpe"].idxmax()
min_var_index = results["Volatility"].idxmin()

max_sharpe_weights = results.loc[max_sharpe_index, "Weights"]
min_var_weights = results.loc[min_var_index, "Weights"]

print("\n\n MAX SHARPE PORTFOLIO WEIGHTS ")
for name, weight in zip(factors.columns, max_sharpe_weights):
    print(f"{name}: {weight:.4f}")

print("\n MINIMUM VARIANCE PORTFOLIO WEIGHTS ")
for name, weight in zip(factors.columns, min_var_weights):
    print(f"{name}: {weight:.4f}")

weights_df = pd.DataFrame({
    "Factor": factors.columns,
    "Weight": max_sharpe_weights
})
weights_df.to_csv("max_sharpe_weights.csv", index=False)

mvo_returns = (factors * max_sharpe_weights).sum(axis=1)

mvo_returns.to_csv("mvo_returns.csv")

plt.figure(figsize=(10,7))
plt.scatter(results["Volatility"], results["Returns"], c=results["Sharpe"], cmap='viridis', s=10)
plt.colorbar(label='Sharpe Ratio')
plt.xlabel("Portfolio Volatility")
plt.ylabel("Portfolio Expected Return")
plt.title("Efficient Frontier (Factor Portfolios)")

plt.scatter(results.loc[max_sharpe_index, "Volatility"],
            results.loc[max_sharpe_index, "Returns"],
            color='red', s=80, label="Max Sharpe")

plt.scatter(results.loc[min_var_index, "Volatility"],
            results.loc[min_var_index, "Returns"],
            color='blue', s=80, label="Min Variance")

plt.legend()
plt.grid(True)
plt.show()
