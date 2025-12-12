## System Architecture

```mermaid
flowchart TB

    subgraph Data["Data Layer"]
        A1[Price Data]
        A2[Fundamental Data]
    end

    subgraph Factors["Factor Layer"]
        B1[Momentum]
        B2[Value]
        B3[Quality]
        B4[Low Volatility]
        B5[Size]
        B6[ESG]
    end

    subgraph Portfolios["Portfolio Construction"]
        C1[Single-Factor Portfolios]
        C2[Factor Return Series]
    end

    subgraph Optimization["Optimization Layer"]
        D1[Mean-Variance Optimizer]
        D2[Optimized Factor Weights]
    end

    subgraph Final["Final Output"]
        E1[Multi-Factor Portfolio]
        E2[Performance Evaluation]
    end

    A1 --> B1
    A1 --> B4
    A2 --> B2
    A2 --> B3
    A2 --> B5
    A2 --> B6

    B1 --> C1
    B2 --> C1
    B3 --> C1
    B4 --> C1
    B5 --> C1
    B6 --> C1

    C1 --> C2
    C2 --> D1
    D1 --> D2
    D2 --> E1
    E1 --> E2
