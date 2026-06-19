# Phase 1: Local CLI & Storage Core (Deliverable D2 - Analyst Agent Spec)

## 0. Cabecera operativa (obligatoria)
- Deliverable: `D2`
- Fase: `PH1`
- Estado: `In progress`
- Prioridad: `P1`
- Owner: `Analyst Agent`
- Ultima actualizacion: `2026-06-20`
- Dependencias: `D1`
- Spec relacionada: `agent/roadmap.md`

---

## 1. Vision General
The **Analyst Agent** evaluates the sanitized financial JSON payload emitted by the Gatekeeper, compares the transaction amount against the user's monthly budget limits, and invokes local MCP tools to read and write records from the database.

---

## 2. Contexto y Objetivos
- **Current Problem**: Structured expense data needs to be logged persistently in a private local file, and the user must be alerted immediately if the transaction breaches their monthly allowance limit.
- **Implementation Objective**: Connect the agent to a local MCP server that handles database read/write actions, perform budget validation math, and write records to `data/expenses.json`.
- **Constraints**: 
  - All file inputs and outputs must pass through the local MCP server tools.
  - The budget limit must be loaded dynamically from the environment.

---

## 3. Alcance

### Incluido
- Loading configuration values (`MONTHLY_BUDGET_LIMIT`) from `.env`.
- Invoking the `get_monthly_total()` MCP tool to calculate current monthly expenditures.
- Comparing new amounts to ensure they don't exceed the limit, preparing warnings.
- Invoking the `add_expense_record()` MCP tool to append the record to the database.

### No incluido
- Parsing raw text strings (delegated to the Gatekeeper Agent).
- Direct local file writes (delegated to the local MCP server).

---

## 4. Cambios tecnicos

### Backend
- Class `AnalystAgent` in `src/agents.py` implementing audit and routing logic.
- Local MCP Server tools in `src/mcp_server.py`.

### Trazabilidad de archivos (obligatoria)

#### Files touched (planned)
- `src/agents.py` - Implement AnalystAgent class and connection to MCP tools.
- `src/mcp_server.py` - Implement MCP server hosting database tools.
- `tests/test_analyst.py` - Unit test suite verifying budget calculation warnings.
- `data/expenses.json` - JSON database initialized with `[]`.

#### Files touched (final)
- *(To be completed when work is executed)*

---

## 5. Invariantes y guardrails
- **Multi-Agent Constraint**: The Analyst Agent will only process inputs that have `is_malicious: false`.
- **Database Safety**: Write transactions must be structured and validated.

---

## 6. ADRs del entregable
`Sin ADR nuevo en este entregable`.

---

## 7. Validacion

### Automatizado
```bash
# Run Analyst-specific tests
uv run pytest tests/test_analyst.py
```

### Manual
1. Insert mock database records and input values near the budget threshold to trigger and verify the Warning message.
2. Verify that write actions correctly save records inside `data/expenses.json`.

---

## 8. Estado y Slices

### 8.1 Estado
- Estado actual: `In progress`
- Ultima actualizacion: `2026-06-20`

### 8.2 Slices
- `D2-S1` (`2026-06-20`, planned):
  - Problema: Lack of test suite for budget threshold validation.
  - Fix aplicado: Implement `tests/test_analyst.py` with mock tools and budget logic asserts (TDD RED phase).
  - commit: `local-doc-only`
- `D2-S2` (`2026-06-20`, planned):
  - Problema: Local storage capability and MCP tool endpoints are missing.
  - Fix aplicado: Implement `src/mcp_server.py` providing file-based storage tools.
  - commit: `local-doc-only`
- `D2-S3` (`2026-06-20`, planned):
  - Problema: Analyst Agent logic and tools integration are missing.
  - Fix aplicado: Implement `AnalystAgent` logic in `src/agents.py`.
  - commit: `local-doc-only`

---

## 9. Definition of Done (DoD)
- [ ] Database read/write tools exposed via local MCP server.
- [ ] Analyst Agent executes budget checking math correctly against the limit.
- [ ] Analyst Agent triggers warning alert if budget limit is breached.
- [ ] Unit tests in `tests/test_analyst.py` are passing.
