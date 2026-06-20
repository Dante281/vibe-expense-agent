# Phase 1: Local CLI & Storage Core (Deliverable D3 - Local MCP Server)

## 0. Cabecera operativa (obligatoria)
- Deliverable: `D3`
- Fase: `PH1`
- Estado: `In progress`
- Prioridad: `P1`
- Owner: `Analyst Agent`
- Ultima actualizacion: `2026-06-20`
- Dependencias: `D2`
- Spec relacionada: `agent/specs/PH1_D2_analyst.md`

---

## 1. Vision General
The **Local MCP Server** acts as the data persistence layer. It exposes three secure tools to read and write records from the local `data/expenses.json` database.

---

## 2. Contexto y Objetivos
- **Problem**: Expense data must be stored persistently, privately, and locally without resorting to complex database engines.
- **Objective**: Expose standard Model Context Protocol (MCP) tools that handle file I/O operations inside the workspace securely.

---

## 3. Alcance

### Incluido
- `get_expenses_list()`: Reads all records from `data/expenses.json`.
- `get_monthly_total()`: Calculates the sum of expense amounts logged in the current calendar month.
- `add_expense_record(description, amount, date, category)`: Appends a new expense record to `data/expenses.json`.

### No incluido
- Exposing tools to write outside the `data/` folder.

---

## 4. Cambios tecnicos

### Backend
- MCP tool definitions in `src/mcp_server.py`.
- JSON structure in `data/expenses.json`.

### Trazabilidad de archivos (obligatoria)

#### Files touched (planned)
- `src/mcp_server.py` - Implement file storage tools.
- `data/expenses.json` - Target database file.

#### Files touched (final)
- *(To be completed when work is executed)*

---

## 5. Invariantes y guardrails
- **File Safety**: Ensure write operations don't corrupt the JSON structure (i.e. handle file locks, append properly, and validate fields).

---

## 6. ADRs del entregable
`Sin ADR nuevo en este entregable`.

---

## 7. Validacion

### Automatizado
- pytest checks verifying correct I/O outcomes.

### Manual
1. Open `data/expenses.json` before and after logging an expense to verify that the entry is correctly written.

---

## 8. Estado y Slices

### 8.1 Estado
- Estado actual: `In progress`
- Ultima actualizacion: `2026-06-20`

### 8.2 Slices
- `D3-S1` (`2026-06-20`, planned):
  - Problema: No file-based storage server is implemented.
  - Fix aplicado: Implement `src/mcp_server.py` defining the required database read/write tools.
  - commit: `local-doc-only`

---

## 9. Definition of Done (DoD)
- [ ] Database read and write tools return success codes and persist data correctly.
- [ ] monthly total calculations match the sum of items in `expenses.json`.
