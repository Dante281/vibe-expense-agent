import json
import os
from typing import List, Dict, Any

DATABASE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "data", "expenses.json"
)


def get_expenses_list() -> List[Dict[str, Any]]:
    """
    MCP Tool: Retrieves the full list of raw logged expenses.
    """
    if not os.path.exists(DATABASE_PATH):
        return []
    with open(DATABASE_PATH, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def get_monthly_total() -> float:
    """
    MCP Tool: Summarizes the total amount of money spent in the current calendar month.
    """
    # Placeholder return
    return 0.0


def add_expense_record(
    description: str, amount: float, date: str, category: str
) -> str:
    """
    MCP Tool: Appends a structured expense record to the local JSON database file.
    """
    # Placeholder return
    return "Success"
