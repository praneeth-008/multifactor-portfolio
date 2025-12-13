# Factor-Based Portfolio Optimization

This project implements a multi-factor equity portfolio construction framework.
Equity factors are computed from price and fundamental data, used to construct
single-factor portfolios, and then combined into a multi-factor portfolio.
Mean–variance optimization is applied at the factor level to improve
risk-adjusted performance.

---

## System Architecture

```mermaid
flowchart LR
    A[Price & Fundamental Data] --> B[Factor Models]
    B --> C[Factor Scores]
    C --> D[Single-Factor Portfolios]
    D --> E[Factor Return Series]
    E --> F[Mean-Variance Optimizer]
    F --> G[Optimized Factor Weights]
    G --> H[Final Multi-Factor Portfolio]
    H --> I[Performance Evaluation]
flowchart TD
    A[multifactor-portfolio]

    A --> B[src]

    B --> C[main.py]
    B --> D[price_data.py]
    B --> E[factors.py]
    B --> F[factor_portfolio.py]
    B --> G[final_portfolio.py]
    B --> H[mean_variance_optimizer.py]

    B --> I[momentum_returns.csv]
    B --> J[volatility_returns.csv]
    B --> K[value_returns.csv]
    B --> L[quality_returns.csv]
    B --> M[size_returns.csv]
    B --> N[esg_returns.csv]

    B --> O[final_portfolio_returns.csv]
    B --> P[mvo_returns.csv]
    B --> Q[max_sharpe_weights.csv]

    B --> R[return_plots.ipynb]

    A --> S[spx_all_values.xlsx]
    A --> T[README.md]
    A --> U[LICENSE]
    A --> V[.gitignore]
