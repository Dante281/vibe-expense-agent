# Phase 1: Local CLI & Storage Core (Deliverable D4 - Interactive CLI Wrapper)

## 0. Cabecera operativa (obligatoria)
- Deliverable: `D4`
- Fase: `PH1`
- Estado: `Completed`
- Prioridad: `P1`
- Owner: `Developer`
- Ultima actualizacion: `2026-06-20`
- Dependencias: `D2, D3`
- Spec relacionada: `agent/specs/PH1_D1_gatekeeper.md`

---

## 1. Vision General
The **Interactive CLI Wrapper** coordinates the user prompt execution loop. It takes inputs from terminal stdin, passes them to the Gatekeeper Agent, feeds output into the Analyst Agent, and prints final answers.

---

## 2. Contexto y Objetivos
- **Problem**: Users need a direct command-line interface to enter expenses conversatially and check outputs.
- **Objective**: Implement a `while True` loop that loads environment variables and handles program interruption.

---

## 3. Alcance

### Incluido
- Loading configuration values (`MONTHLY_BUDGET_LIMIT`, `GEMINI_API_KEY`) from `.env`.
- An interactive shell prompt loop.
- Handling of `exit`, `quit` commands, and KeyboardInterrupt (`Ctrl+C`).
- Printing confirmation and validation error messages clearly.

### No incluido
- Web dashboards (delegated to Phase 2).

---

## 4. Cambios tecnicos

### Backend
- Main execution entrypoint in `src/main.py`.

### Trazabilidad de archivos (obligatoria)

#### Files touched (planned)
- `src/main.py` - Core loop and configurations loading.

#### Files touched (final)
- [src/main.py](file:///c:/Dev/github/Kaggle/5-Day%20AI%20Agents/Day%206%20Capstone%20Project/vibe-expense-agent/src/main.py) - Integrated agents and database loops, resolved console Unicode encoding crashes.

---

## 5. Invariantes y guardrails
- Ensure KeyboardInterrupt does not dump tracebacks, but exits cleanly.

---

## 6. ADRs del entregable
`Sin ADR nuevo en este entregable`.

---

## 7. Validacion

### Manual
1. Run `uv run src/main.py` and write expenses.
2. Input empty lines and check if the loop continues gracefully.
3. Input `exit` and verify program terminates.

---

## 8. Estado y Slices

### 8.1 Estado
- Estado actual: `Completed`
- Ultima actualizacion: `2026-06-20`

### 8.2 Slices
- `D4-S1` (`2026-06-20`, planned):
  - Problema: Lack of CLI entrypoint shell.
  - Fix aplicado: Implement basic command prompt loop and load configuration variables in `src/main.py`.
  - commit: `d54f690`

---

## 9. Definition of Done (DoD)
- [x] User can input natural language sentences and get formatted outputs.
- [x] Environment secrets and configurations are successfully loaded.
