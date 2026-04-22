# 🏦 AML/KYC Compliance AI Agent

> An automated audit and reporting agent for Anti-Money Laundering (AML) and Know Your Customer (KYC) compliance, built using the [VSCode Foundry Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) and powered by **Claude Sonnet** via the Anthropic API.

---

## 📌 Overview

This project implements a multi-agent AI system designed to automate the compliance audit lifecycle — from real-time transaction screening and KYC document verification, to structured audit report generation. It was prototyped using the VSCode AI Toolkit Agent Builder (no-code), then exported and extended in Python for production use.

**Compliance scope:** FATF recommendations, FinCEN guidance, sanctions screening, PEP identification

**AI/ML discipline:** AI Engineering · Agentic NLP Systems · Anomaly Detection · Decision Support

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│              Audit Orchestrator Agent            │
│         (aggregates sub-agent outputs)          │
└────────────┬──────────────────┬─────────────────┘
             │                  │
     ┌───────▼──────┐   ┌───────▼───────┐
     │  Screening   │   │  KYC Verifier │
     │    Agent     │   │     Agent     │
     │              │   │               │
     │ Transactions │   │ ID · UBO ·    │
     │ + Watchlists │   │ Risk Profile  │
     └──────────────┘   └───────────────┘
             │                  │
     ┌───────▼──────────────────▼───────┐
     │         MCP Tool Layer           │
     │  Filesystem · DB · REST APIs     │
     │  Sanctions Lists · PEP Registry  │
     └──────────────────────────────────┘
```

---

## ✨ Features

- **Automated transaction screening** against sanctions lists and watchlists
- **KYC document analysis** — ID verification, Ultimate Beneficial Owner (UBO) mapping, and risk profile assembly
- **Risk scoring engine** — classifies entities and transactions by AML risk level
- **Structured audit reports** — outputs timestamped, signed PDF/JSON reports per entity or transaction batch
- **Decision audit trail** — full runtime tracing of agent reasoning for regulatory defensibility
- **Multi-agent orchestration** — specialised sub-agents coordinated by a central orchestrator
- **One-click cloud deployment** via Microsoft Foundry

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| IDE & Agent Builder | [VSCode Foundry Toolkit](https://code.visualstudio.com/docs/intelligentapps/overview) |
| LLM | Claude Sonnet (`claude-sonnet-4-6`) via Anthropic API |
| Agent Framework | Microsoft Agent Framework SDK (Python) |
| Tool Integration | Model Context Protocol (MCP) servers |
| Cloud Deployment | Microsoft Foundry |
| Language | Python 3.11+ |
| Report Output | PDF · JSON |

---

## 📁 Project Structure

```
aml-kyc-compliance-agent/
├── agents/
│   ├── orchestrator.py          # Audit orchestrator agent
│   ├── screening_agent.py       # Transaction screening sub-agent
│   └── kyc_verifier_agent.py    # KYC document verifier sub-agent
├── tools/
│   ├── sanctions_checker.py     # Sanctions list + PEP screening tool
│   ├── risk_scorer.py           # Risk classification tool
│   └── report_generator.py      # PDF/JSON audit report tool
├── prompts/
│   └── system_prompt.txt        # Compliance agent system prompt
├── evals/
│   ├── test_cases/              # Labelled SAR scenarios + clean cases
│   └── run_evals.py             # Evaluation pipeline
├── mcp_config/
│   └── mcp.json                 # MCP server configuration
├── config.py                    # Environment and threshold config
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/)
- [Foundry Toolkit Extension](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)
- Python 3.11+
- Anthropic API key

### 1. Clone the repository

```bash
git clone https://github.com/your-username/aml-kyc-compliance-agent.git
cd aml-kyc-compliance-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env`:

```env
ANTHROPIC_API_KEY=your_api_key_here
SANCTIONS_API_URL=https://your-sanctions-api.com
PEP_REGISTRY_URL=https://your-pep-registry.com
RISK_THRESHOLD_HIGH=0.75
RISK_THRESHOLD_MEDIUM=0.45
```

### 4. Configure MCP servers

Update `mcp_config/mcp.json` with your filesystem paths and database connection strings. Refer to the [MCP documentation](https://code.visualstudio.com/docs/intelligentapps/agentbuilder) for setup instructions.

### 5. Run the agent

```bash
python agents/orchestrator.py --input data/transactions.json
```

---

## 🧪 Evaluation

Run the built-in evaluation suite against labelled compliance test cases:

```bash
python evals/run_evals.py
```

Evaluation metrics include:
- True positive rate on SAR-labelled transactions
- False positive rate on clean customer profiles
- Report generation accuracy and completeness
- Agent reasoning trace quality

---

## 📊 Agent Workflow

```
Input (transactions / customer data)
        │
        ▼
Screening Agent ──► Sanctions match · PEP flag · Pattern anomaly
        │
        ▼
KYC Verifier Agent ──► Document validity · UBO map · Risk profile
        │
        ▼
Audit Orchestrator ──► Aggregates findings · Assigns risk score
        │
        ▼
Report Generator ──► Timestamped PDF/JSON audit report
        │
        ▼
Output ──► Compliance dashboard · SIEM · Case management system
```

---

## ⚖️ Compliance Frameworks Supported

- **FATF** — Financial Action Task Force 40 Recommendations
- **FinCEN** — Financial Crimes Enforcement Network guidelines
- **OFAC** — Office of Foreign Assets Control sanctions lists
- **EU 6AMLD** — Sixth Anti-Money Laundering Directive
- **Basel AML Index** — Risk country classification

---

## 🔒 Important Notes

> **This agent is a decision-support tool.** All flagged cases should be reviewed by a qualified compliance officer before action is taken. The agent's reasoning traces are designed to assist — not replace — human judgement.

- All agent decisions are logged with a full reasoning trace for regulatory audit purposes
- Risk thresholds are configurable and should be calibrated to your institution's risk appetite
- Ensure your data handling complies with applicable data protection regulations (e.g. GDPR) before processing customer data

---

## 🗺️ Roadmap

- [X] Real-time streaming transaction monitoring
- [ ] Integration with SWIFT transaction messaging
- [ ] Automated SAR (Suspicious Activity Report) filing draft generation
- [ ] Fine-tuned risk scoring model on institution-specific historical data
- [ ] Web dashboard for compliance officer case review

---

## 🤝 Contributing

Contributions are welcome. Please open an issue first to discuss proposed changes. Ensure all new tools include evaluation test cases.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

Built with [VSCode Foundry Toolkit](https://code.visualstudio.com/docs/intelligentapps/overview) · Powered by [Claude](https://www.anthropic.com/claude) by Anthropic