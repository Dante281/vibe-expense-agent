# Vibe Expense Agent Roadmap 🗺️

This roadmap translates the product goals defined in `agents.md` into a structured, high-level execution plan.

The roadmap is intentionally organized using a standard hierarchy, delegating granular implementation details to specific specification files:
1. `Project`
2. `Phases`
3. `Milestones`
4. `Deliverables`

The core product mission is to build a secure, personal financial concierge that allows logging expenses in natural language, sanitizes inputs, and commits them to a local JSON database using an MCP server.

---

## 🎯 Active Execution Focus (Priority Order)

This is the current active execution sequence to construct and stabilize the initial release:
1. Complete validation of the **Gatekeeper Agent** schema parsing.
2. Implement and test the **Analyst Agent** budget verification math.
3. Bind the agents to the local **MCP Server** read/write tools.
4. Implement the interactive **CLI wrapper** (`src/main.py`) to connect all pieces.
5. Verify security guardrails against standard prompt injection payloads.

*Rule of Sequence*: No Phase 2 (Web Dashboard) features should be opened before Phase 1 (CLI & Core) is marked as `Done` and validated.

---

## 📂 Index

| ID | Level | Element | Status | Priority | Effort | Completed Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **P1** | Project | [Vibe Expense Agent Concierge](#p1-vibe-expense-agent-concierge) | In Progress | - | - | - |
| **PH1**| Phase | [Phase 1: Local CLI & Storage Core](#ph1-phase-1-local-cli--storage-core) | In Progress | P1 | M | |
| **M1** | Milestone | [Secure CLI & File Storage Core functional](#m1-secure-cli--file-storage-core-functional) | In Progress | P1 | M | |
| `D1`  | Deliverable | Gatekeeper Agent Sanitizer & Schema Parser | In Progress | P1 | S | |
| `D2`  | Deliverable | Analyst Agent Budget Gate & Router | In Progress | P1 | S | |
| `D3`  | Deliverable | Local file-based MCP Server | In Progress | P1 | S | |
| `D4`  | Deliverable | Interactive CLI Interface wrapper | In Progress | P1 | S | |
| `D5`  | Deliverable | Anti-Prompt Injection filters | In Progress | P1 | S | |
| **PH2**| Phase | [Phase 2: Web Dashboard & API](#ph2-phase-2-web-dashboard--api) | Planned | P2 | L | |
| **M2** | Milestone | [Web UI for Expense Monitoring ready](#m2-web-ui-for-expense-monitoring-ready) | Planned | P2 | L | |
| `D6`  | Deliverable | FastAPI Server exposing REST endpoints | Planned | P2 | M | |
| `D7`  | Deliverable | Responsive Web UI (glassmorphism/custom HSL) | Planned | P2 | L | |
| `D8`  | Deliverable | Interactive visual budget charts | Planned | P2 | M | |
| **PH3**| Phase | [Phase 3: Multimodal OCR Scanning](#ph3-phase-3-multimodal-ocr-scanning) | Planned | P3 | L | |
| **M3** | Milestone | [Physical Receipt Processing functional](#m3-physical-receipt-processing-functional) | Planned | P3 | L | |
| `D9`  | Deliverable | File Uploader MCP Tool | Planned | P3 | S | |
| `D10` | Deliverable | Gemini Multimodal Vision Scanner | Planned | P3 | L | |
| **PH4**| Phase | [Phase 4: Smart Personalization](#ph4-phase-4-smart-personalization) | Planned | P4 | M | |
| **M4** | Milestone | [Contextual Predictions active](#m4-contextual-predictions-active) | Planned | P4 | M | |
| `D11` | Deliverable | Historical category lookup tool | Planned | P4 | S | |
| `D12` | Deliverable | Personal prediction heuristics | Planned | P4 | M | |

---

## 🏗️ P1. Vibe Expense Agent Concierge
**Goal**: Build a personal assistant that automates expense tracking with a strong emphasis on data privacy (local storage) and input sanitization (security).

---

## 📅 Phases and Specifications

### PH1. Phase 1: Local CLI & Storage Core
> **Milestone M1. Secure CLI & File Storage Core functional.** The user can safely input expenses in natural language, which are then sanitized, parsed, and logged to `expenses.json` by the agents using MCP tools.

- **Specifications**:
  - [Gatekeeper Agent Spec](file:///c:/Dev/github/Kaggle/5-Day%20AI%20Agents/Day%206%20Capstone%20Project/vibe-expense-agent/agent/specs/gatekeeper.md) handles `D1` and `D5`.
  - [Analyst Agent Spec](file:///c:/Dev/github/Kaggle/5-Day%20AI%20Agents/Day%206%20Capstone%20Project/vibe-expense-agent/agent/specs/analyst.md) handles `D2` and `D3`.
  - CLI execution loop in `src/main.py` handles `D4`.

---

### PH2. Phase 2: Web Dashboard & API
> **Milestone M2. Web UI for Expense Monitoring ready.** The CLI is augmented with a lightweight, secure web dashboard displaying analytics and status.

- **Deliverables**:
  - `D6`: FastAPI Backend to support the web UI.
  - `D7`: Single Page Application (SPA) with curated HSL color schemes, dark mode support, and smooth micro-animations.
  - `D8`: Dynamic SVG/CSS budget charts showing remaining allowance.

---

### PH3. Phase 3: Multimodal OCR Scanning
> **Milestone M3. Physical Receipt Processing functional.** Users can drag-and-drop or upload pictures of physical receipt tickets to parse them.

- **Deliverables**:
  - `D9`: MCP tools expanded to accept base64-encoded receipt images.
  - `D10`: Analyst Agent utilizes Gemini Multimodal prompts to extract name, amount, date, and items from the image.

---

### PH4. Phase 4: Smart Personalization
> **Milestone M4. Contextual Predictions active.** The system improves over time by learning custom categorization defaults from user history.

- **Deliverables**:
  - `D11`: Search tool to query historically similar descriptions.
  - `D12`: Local classification correction rules.
