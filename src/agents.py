from typing import Dict, Any


class GatekeeperAgent:
    """
    Gatekeeper Agent (Recibidor):
    Responsible for text sanitization, prompt injection checks, and structured JSON parsing.
    """

    def __init__(self):
        # Initialized configuration or client here
        pass

    def process_input(self, raw_text: str) -> Dict[str, Any]:
        """
        Parses raw conversational text. Returns a dictionary matching the Gatekeeper output contract schema.
        """
        # Placeholder returns
        return {
            "is_malicious": False,
            "refusal_reason": "",
            "description": "",
            "amount": 0.0,
            "date": "",
            "category": "Others",
        }


class AnalystAgent:
    """
    Analyst Agent (Contador):
    Responsible for budget limit checks, tool interactions, and database records insertion.
    """

    def __init__(self, budget_limit: float = 500.00):
        self.budget_limit = budget_limit

    def process_expense(self, parsed_expense: Dict[str, Any]) -> str:
        """
        Processes a sanitized expense dictionary, runs budget arithmetic, and triggers MCP tools to log it.
        """
        # Placeholder returns
        return ""
