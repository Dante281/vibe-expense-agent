import json
import os
import datetime
from typing import List, Dict, Any


def get_database_path() -> str:
    return os.getenv(
        "EXPENSE_DB_PATH",
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "expenses.json"
        ),
    )


def get_expenses_list() -> List[Dict[str, Any]]:
    """
    MCP Tool: Retrieves the full list of raw logged expenses.
    """
    db_path = get_database_path()
    if not os.path.exists(db_path):
        return []
    with open(db_path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def get_monthly_total() -> float:
    """
    MCP Tool: Summarizes the total amount of money spent in the current calendar month.
    """
    expenses = get_expenses_list()
    current_month = datetime.date.today().strftime("%Y-%m")
    total = 0.0
    for exp in expenses:
        exp_date = exp.get("date", "")
        if exp_date.startswith(current_month):
            try:
                total += float(exp.get("amount", 0.0))
            except (ValueError, TypeError):
                pass
    return total


def add_expense_record(
    description: str, amount: float, date: str, category: str
) -> str:
    """
    MCP Tool: Appends a structured expense record to the local JSON database file.
    """
    expenses = get_expenses_list()

    max_id = 0
    for exp in expenses:
        exp_id = exp.get("id")
        if isinstance(exp_id, int) and exp_id > max_id:
            max_id = exp_id
    new_id = max_id + 1

    new_record = {
        "id": new_id,
        "date": date,
        "category": category,
        "description": description,
        "amount": float(amount),
    }
    expenses.append(new_record)

    db_path = get_database_path()
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    with open(db_path, "w") as f:
        json.dump(expenses, f, indent=2)

    return "Success"
