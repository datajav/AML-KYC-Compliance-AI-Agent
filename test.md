```mermaid
flowchart TD
    A[🖥️ Streamlit UI<br/>app.py] --> B[🤖 Compliance Orchestrator<br/>Claude 3.5 Sonnet]
    B --> C[🔍 Sanctions Checker<br/>BOJ · UN · OFAC]
    B --> D[📊 Risk Scorer<br/>CFATF Logic]
    C --> E[💾 Cache Layer]
    D --> E
    E --> F[📄 Audit Report<br/>JSON/PDF]
    
    style A fill:#1f77b4,stroke:#333,stroke-width:2px,color:#fff
    style B fill:#ff7f0e,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#2ca02c,stroke:#333,stroke-width:2px,color:#fff
    style D fill:#2ca02c,stroke:#333,stroke-width:2px,color:#fff
    style E fill:#9467bd,stroke:#333,stroke-width:2px,color:#fff
    style F fill:#1f77b4,stroke:#333,stroke-width:2px,color:#fff
