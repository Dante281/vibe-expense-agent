from src.agents import AnalystAgent


def test_analyst_within_budget():
    """
    Test that an expense within the monthly limit is approved
    and does not trigger a warning.
    """
    analyst = AnalystAgent(budget_limit=500.00)
    mock_expense = {
        "is_malicious": False,
        "refusal_reason": "",
        "description": "Taxi",
        "amount": 20.00,
        "date": "2026-06-20",
        "category": "Transport",
    }

    # Note: This will fail initially (Red phase of TDD)
    response = analyst.process_expense(mock_expense)
    assert "Warning" not in response
    assert "Logged" in response or "Success" in response


def test_analyst_exceeds_budget():
    """
    Test that an expense exceeding the monthly limit triggers a warning.
    """
    analyst = AnalystAgent(budget_limit=100.00)
    mock_expense = {
        "is_malicious": False,
        "refusal_reason": "",
        "description": "Office Chair",
        "amount": 150.00,
        "date": "2026-06-20",
        "category": "Shopping",
    }

    # Note: This will fail initially (Red phase of TDD)
    response = analyst.process_expense(mock_expense)
    assert "Warning" in response or "exceed" in response.lower()
