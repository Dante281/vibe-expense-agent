import os
from dotenv import load_dotenv
from src.agents import GatekeeperAgent, AnalystAgent

# Load environment configuration
load_dotenv()


def main():
    print("==================================================")
    print("      🪙  Vibe Expense Agent Concierge  🪙      ")
    print("==================================================")
    print("Type your expense in natural language (e.g. 'spent $10 on lunch today')")
    print("Or type 'exit' to quit.\n")

    # Instantiate agents
    gatekeeper = GatekeeperAgent()

    budget_limit = float(os.getenv("MONTHLY_BUDGET_LIMIT", "500.00"))
    analyst = AnalystAgent(budget_limit=budget_limit)

    while True:
        try:
            user_input = input("> ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("exit", "quit"):
                print("Goodbye!")
                break

            # 1. Gatekeeper sanitizes & extracts data
            parsed = gatekeeper.process_input(user_input)

            if parsed.get("is_malicious"):
                print(f"❌ Refused: {parsed.get('refusal_reason')}\n")
                continue

            # 2. Analyst processes expense (checks budget and saves via MCP)
            response = analyst.process_expense(parsed)
            print(f"🤖 {response}\n")

        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
