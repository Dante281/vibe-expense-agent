# Phase 1: Local CLI & Storage Core (Deliverable D1 - Gatekeeper Agent Spec)

## 0. Cabecera operativa (obligatoria)
- Deliverable: `D1`
- Fase: `PH1`
- Estado: `In progress`
- Prioridad: `P1`
- Owner: `Gatekeeper Agent`
- Ultima actualizacion: `2026-06-20`
- Dependencias: `N/A`
- Spec relacionada: `agent/roadmap.md`

---

## 1. Vision General
The **Gatekeeper Agent** is the user-facing security shield. It acts as the parser and sanitizer for raw natural language input, transforming conversational text into a structured JSON schema while detecting and preventing prompt injection threats.

---

## 2. Contexto y Objetivos
- **Current Problem**: Financial inputs coming from untrusted user strings can introduce prompt injection attacks, aiming to wipe database files, execute system commands, or modify application configuration (e.g., budget limits).
- **Implementation Objective**: Implement a robust sanitization and parsing engine using Gemini's structured output capability.
- **Constraints**: 
  - Must run before the Analyst Agent receives any data.
  - Schema parsing must strictly conform to the defined JSON structure.

---

## 3. Alcance

### Incluido
- Input sanitization against prompt injection payloads.
- Flagging threats using `is_malicious` and generating explanations in `refusal_reason`.
- Extraction of expense details (`description`, `amount`, `date`, `category`) in safe inputs.
- Defaulting missing dates to the current date.

### No incluido
- Saving to the database (delegated to the MCP server).
- Budget limits checking (delegated to the Analyst Agent).

---

## 4. Cambios tecnicos

### Backend
- Class `GatekeeperAgent` in `src/agents.py` implementing parsing logic.

### Trazabilidad de archivos (obligatoria)

#### Files touched (planned)
- `src/agents.py` - Implement GatekeeperAgent class and prompt engineering.
- `tests/test_gatekeeper.py` - Unit test suite verifying parsing and security guardrails.

#### Files touched (final)
- *(To be completed when work is executed)*

---

## 5. Invariantes y guardrails
- **Security Guardrail**: Any input attempting to ignore instructions or access system configurations must set `is_malicious: true`.
- **Validation Constraint**: Output schema must be strictly enforced.

---

## 6. ADRs del entregable
`Sin ADR nuevo en este entregable`.

---

## 7. Validacion

### Automatizado
```bash
# Run Gatekeeper-specific tests
pytest tests/test_gatekeeper.py
```

### Manual
1. Input standard conversational inputs in the CLI wrapper to verify correct parsing.
2. Input known prompt injection payloads to verify rejection and refusal logs.

---

## 8. Estado y Slices

### 8.1 Estado
- Estado actual: `In progress`
- Ultima actualizacion: `2026-06-20`

### 8.2 Slices
- `D1-S1` (`2026-06-20`, planned):
  - Problema: Lack of test suite for input validation.
  - Fix aplicado: Implement `tests/test_gatekeeper.py` with standard inputs and malicious payload checks (TDD RED phase).
  - commit: `local-doc-only`
- `D1-S2` (`2026-06-20`, planned):
  - Problema: Gatekeeper Agent class is not implemented.
  - Fix aplicado: Implement `GatekeeperAgent` logic in `src/agents.py` with Gemini structured schema outputs.
  - commit: `local-doc-only`

---

## 9. Definition of Done (DoD)
- [ ] Strict JSON schema extraction implemented and validated.
- [ ] Prompt injection detection sets `is_malicious: true` for malicious inputs.
- [ ] Unit tests in `tests/test_gatekeeper.py` are passing.
