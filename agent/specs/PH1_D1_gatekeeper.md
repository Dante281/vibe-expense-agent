# Phase 1: Local CLI & Storage Core (Deliverable D1 - Gatekeeper Agent)

## 0. Cabecera operativa (obligatoria)
- Deliverable: `D1`
- Fase: `PH1`
- Estado: `In progress`
- Prioridad: `P1`
- Owner: `Gatekeeper Agent`
- Ultima actualizacion: `2026-06-20`
- Dependencias: `N/A`
- Spec relacionada: `agent/specs/PH1_D5_security_filters.md`

---

## 1. Vision General
The **Gatekeeper Agent** parses raw natural language descriptions of expenses into a strictly validated JSON structure. It separates conversational input from structured database attributes.

---

## 2. Contexto y Objetivos
- **Problem**: Natural language expense reports are messy and non-standardized. We need to extract clean values (`description`, `amount`, `date`, `category`) to perform budget checks.
- **Objective**: Use Gemini's structured JSON output mode to extract structured data securely.

---

## 3. Alcance

### Incluido
- Extracting expense fields (`description`, `amount`, `date`, `category`) from conversational text.
- Formating dates to YYYY-MM-DD.
- Enforcing enum validation for categories (Food, Transport, Utilities, Entertainment, Shopping, Others).

### No incluido
- Prompt injection protection (delegated to `D5` spec).
- Database commits (delegated to `D3` spec).

---

## 4. Cambios tecnicos

### Backend
- `GatekeeperAgent` in `src/agents.py` implementing `process_input()`.

### Trazabilidad de archivos (obligatoria)

#### Files touched (planned)
- `src/agents.py` - Implement schema parser.
- `tests/test_gatekeeper.py` - Assert parsing results.

#### Files touched (final)
- *(To be completed when work is executed)*

---

## 5. Invariantes y guardrails
- Categories must strictly match the enum fields.

---

## 6. ADRs del entregable
`Sin ADR nuevo en este entregable`.

---

## 7. Validacion

### Automatizado
```bash
uv run pytest tests/test_gatekeeper.py -k test_gatekeeper_valid_extraction
```

---

## 8. Estado y Slices

### 8.1 Estado
- Estado actual: `In progress`
- Ultima actualizacion: `2026-06-20`

### 8.2 Slices
- `D1-S1` (`2026-06-20`, planned):
  - Problema: Lack of test suite for valid text parsing.
  - Fix aplicado: Implement `test_gatekeeper_valid_extraction` in `tests/test_gatekeeper.py`.
  - commit: `local-doc-only`
- `D1-S2` (`2026-06-20`, planned):
  - Problema: Gatekeeper parser logic is missing.
  - Fix aplicado: Implement parsing logic inside `src/agents.py` using Gemini client schemas.
  - commit: `local-doc-only`

---

## 9. Definition of Done (DoD)
- [ ] Schema extraction returns exact categories, parsed amounts, and format-verified dates.
- [ ] Pytest validations pass.
