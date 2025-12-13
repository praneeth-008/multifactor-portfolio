## File Structure

```mermaid
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
