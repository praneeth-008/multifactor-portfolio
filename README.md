# Factor-Based Portfolio Optimization

This project implements a multi-factor equity portfolio construction framework.
Individual equity factors are computed from price and fundamental data, used to
construct single-factor portfolios, and then combined into a multi-factor
portfolio. Mean–variance optimization is applied at the factor level to improve
risk-adjusted performance.

---

## Project Architecture

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
