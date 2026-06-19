# Analyst Agent Specification 📊

The **Analyst Agent** (Contador) processes the validated structured output from the Gatekeeper. It performs budget analysis and calls local MCP tools to read and write from the local database.

---

## 📋 Role Overview

- **Input**: Sanitized JSON data from the Gatekeeper: `{description, amount, date, category}`.
- **Output**: Confirmation message with budget status, plus a warning if the monthly budget is exceeded.
- **Primary Responsibility**: Coordinate tool calling and evaluate expenditures against the monthly budget limit.

---

## 🛠️ MCP Tools Binding

The Analyst Agent is bound to a local Model Context Protocol (MCP) server that exposes the following tools:

### 1. `get_monthly_total()`
- **Purpose**: Sums up all expense records logged in the current calendar month.
- **Parameters**: None.
- **Returns**: `float` (total spending for the month).

### 2. `add_expense_record(description, amount, date, category)`
- **Purpose**: Appends a validated expense record to the local JSON database file.
- **Parameters**:
  - `description` (string)
  - `amount` (float)
  - `date` (string, YYYY-MM-DD)
  - `category` (string, enum)
- **Returns**: `"Success"` or error message.

### 3. `get_expenses_list()`
- **Purpose**: Returns all logged expense records for reporting.
- **Parameters**: None.
- **Returns**: Array of expense objects.

---

## 🧠 System Instruction Prompt

```text
You are the Analyst Agent for the Vibe Expense system. You receive structured expense data from the Gatekeeper.
Your job is to:
1. Call the `get_monthly_total()` tool to check the user's spending in the current month.
2. Compare the updated total (current monthly total + new expense amount) against the user's budget limit of ${budget_limit}.
3. If the limit is exceeded, prepare a BUDGET EXCEEDED warning message.
4. Call `add_expense_record()` to permanently log the expense in the database.
5. Respond to the user confirming the log, showing the new monthly total, and issuing a budget warning if applicable.
```

---

## 🧪 Trace Scenarios (Verification Contracts)

### Scenario 1: Normal Log (Within Budget)
1. **Analyst receives**: `{ "description": "Taxi", "amount": 20.00, "date": "2026-06-20", "category": "Transport" }`
2. **Analyst calls**: `get_monthly_total()` ➔ returns `$100.00`
3. **Analyst evaluates**: New total `$120.00` is below the `$500.00` limit.
4. **Analyst calls**: `add_expense_record("Taxi", 20.00, "2026-06-20", "Transport")` ➔ returns `"Success"`
5. **Analyst outputs**: `"Logged $20.00 for Taxi under Transport. Monthly total is now $120.00 / $500.00."`

### Scenario 2: Budget Exceeded Alert
1. **Analyst receives**: `{ "description": "Office Chair", "amount": 150.00, "date": "2026-06-20", "category": "Shopping" }`
2. **Analyst calls**: `get_monthly_total()` ➔ returns `$420.00`
3. **Analyst evaluates**: New total `$570.00` exceeds the `$500.00` limit by `$70.00`.
4. **Analyst calls**: `add_expense_record("Office Chair", 150.00, "2026-06-20", "Shopping")` ➔ returns `"Success"`
5. **Analyst outputs**: `"⚠️ BUDGET WARNING: Logging this expense brings your monthly total to $570.00, which exceeds your monthly budget of $500.00 by $70.00!\nSuccessfully logged $150.00 for Office Chair under Shopping."`
