# Agent Context & Guidelines 🤖

This file serves as the context and instruction file for any AI assistant or coding agent operating within this repository.

---

## 🎯 Project Mission
**Vibe Expense Agent** is a secure, personal financial concierge. It allows users to log expenses in natural language, sanitizes data against prompt injection attacks, and securely commits them to a local JSON database via a Model Context Protocol (MCP) server.

---

## 📂 Architecture and Specifications
We follow modular documentation practices. You MUST read and adhere to the specifications in the following files before planning or writing any code:

1. **System Design & Roadmap**: See [agent/roadmap.md](file:///c:/Dev/github/Kaggle/5-Day%20AI%20Agents/Day%206%20Capstone%20Project/vibe-expense-agent/agent/roadmap.md)
   - Understands the multi-agent message sequence.
   - Summarizes development phases (CLI ➔ Web ➔ vision OCR).
2. **Gatekeeper Agent Spec**: See [agent/specs/gatekeeper.md](file:///c:/Dev/github/Kaggle/5-Day%20AI%20Agents/Day%206%20Capstone%20Project/vibe-expense-agent/agent/specs/gatekeeper.md)
   - Defines system prompts, strict JSON extraction schema, and prompt injection filters.
3. **Analyst Agent Spec**: See [agent/specs/analyst.md](file:///c:/Dev/github/Kaggle/5-Day%20AI%20Agents/Day%206%20Capstone%20Project/vibe-expense-agent/agent/specs/analyst.md)
   - Outlines budget checking logic and local MCP tools bindings.

---

## 📐 Multi-Agent Interaction Flow
The following sequential diagram illustrates how the CLI, the Gatekeeper, the Analyst, and the local MCP server collaborate to handle a user's request:

```mermaid
sequenceDiagram
    autonumber
    actor User as User (CLI)
    participant GK as Gatekeeper Agent
    participant AN as Analyst Agent
    participant MCP as MCP Server
    database DB as Local DB (expenses.json)

    User->>GK: Natural Language Input
    Note over GK: Security Sanitization (Anti-Injection Check)
    alt Malicious Input Detected
        GK-->>User: Deny Request & Show Refusal Reason
    else Input is Safe
        GK->>GK: Extract structured expense JSON
        GK->>AN: Structured JSON (item, amount, date, category)
        Note over AN: Read context & calculate budget status
        AN->>MCP: Call Tool: get_monthly_total()
        MCP->>DB: Read monthly sum
        DB-->>MCP: Return sum (float)
        MCP-->>AN: Return sum (float)

        alt Total exceeds budget limit
            AN-->>User: Prepare Budget Warning Alert
        end

        AN->>MCP: Call Tool: add_expense_record(expense)
        MCP->>DB: Write to expenses.json
        DB-->>MCP: Return success status
        MCP-->>AN: Return success status
        AN-->>User: Respond with confirmation and budget update
    end
```

---

## 📜 Development Guidelines & Constraints

- **Security First**: 
  - Never commit or log API keys or plaintext credentials. Use `.env` files.
  - Ensure Gatekeeper sanitization runs before Analyst processing.
- **Library-First Principles**:
  - Keep the agent logic in `src/agents.py` decoupled from the CLI execution in `src/main.py`.
- **Test-Driven Development (TDD)**:
  - Write test assertions for the Gatekeeper schema and Analyst logic prior to implementation.
- **MCP Server Protocol**:
  - Keep tools simple, stateless, and focused on file I/O operations inside the `data/` folder.
