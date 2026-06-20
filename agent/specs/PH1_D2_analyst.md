# Phase 1: Local CLI & Storage Core (Deliverable D2 - Analyst Agent)

## 0. Cabecera operativa (obligatoria)
- Deliverable: `D2`
- Fase: `PH1`
- Estado: `In progress`
- Prioridad: `P1`
- Owner: `Analyst Agent`
- Ultima actualizacion: `2026-06-20`
- Dependencias: `D1`
- Spec relacionada: `agent/specs/PH1_D3_mcp_server.md`

---

## 1. Vision General
The **Analyst Agent** acts as the financial auditor. It receives clean JSON from the Gatekeeper, calculates whether the transaction breaches the monthly budget limit, and formats warning messages or confirmation logs.

---

## 2. Contexto y Objetivos
- **Problem**: We need to warn the user dynamically if they exceed their target spending allowance for the month.
- **Objective**: Implement budget limit threshold comparison math.

---

## 3. Alcance

### Incluido
- Loading the monthly budget limit dynamically from the environment.
- Invoking MCP tools to check the monthly aggregate spend.
- Emitting warning alerts if the budget threshold is breached.

### No incluido
- Executing file writes (delegated to MCP server in `D3` spec).

---

## 4. Cambios tecnicos

### Backend
- `AnalystAgent` class in `src/agents.py` implementing `process_expense()`.

### Trazabilidad de archivos (obligatoria)

#### Files touched (planned)
- `src/agents.py` - Implement AnalystAgent class and budget logic.
- `tests/test_analyst.py` - Assert warning triggers.

#### Files touched (final)
- *(To be completed when work is executed)*

---

## 5. Invariantes y guardrails
- The Analyst Agent only routes safe inputs (`is_malicious: false`) to the MCP tools.

---

## 6. ADRs del entregable
`Sin ADR nuevo en este entregable`.

---

## 7. Validacion

### Automatizado
```bash
uv run pytest tests/test_analyst.py
```

---

## 8. Estado y Slices

### 8.1 Estado
- Estado actual: `In progress`
- Ultima actualizacion: `2026-06-20`

### 8.2 Slices
- `D2-S1` (`2026-06-20`, planned):
  - Problema: Lack of test suite for budget auditing.
  - Fix aplicado: Implement `tests/test_analyst.py` with mock assertions (TDD RED phase).
  - commit: `local-doc-only`
- `D2-S2` (`2026-06-20`, planned):
  - Problema: AnalystAgent class and budget comparisons are not coded.
  - Fix aplicado: Write budget calculation and routing logic in `src/agents.py`.
  - commit: `local-doc-only`

---

## 9. Definition of Done (DoD)
- [ ] Analyst agent triggers warning statements for over-budget items.
- [ ] Pytest checks pass.
