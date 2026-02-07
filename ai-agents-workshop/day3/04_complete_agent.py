"""
Day 3: Complete Agent

This combines everything we've learned:
- Multiple built-in tools
- Custom tools
- Session memory
- Custom instructions
"""

from dotenv import load_dotenv
load_dotenv()

import random
from datetime import datetime
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.calculator import CalculatorTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools import tool
from agno.db.sqlite import SqliteDb

# Custom tools
@tool
def get_current_time() -> str:
    """Get the current date and time."""
    now = datetime.now()
    return now.strftime("%A, %B %d, %Y at %I:%M %p")

@tool
def roll_dice(sides: int = 6) -> str:
    """Roll a dice with the specified number of sides."""
    result = random.randint(1, sides)
    return f"Rolled a {result} on a d{sides}"

@tool
def make_decision(options: str) -> str:
    """Help make a random decision from comma-separated options.

    Args:
        options: Comma-separated list of choices
    """
    choices = [opt.strip() for opt in options.split(",")]
    choice = random.choice(choices)
    return f"I choose: {choice}"

# Create the complete agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[
        CalculatorTools(),
        DuckDuckGoTools(),
        get_current_time,
        roll_dice,
        make_decision
    ],
    add_history_to_context=True,
    num_history_runs=3,
    db=SqliteDb(db_file="tmp/data.db"),
    instructions="""You are a helpful personal assistant named Aria.

Your capabilities:
- Math calculations (use calculator)
- Web search for current information
- Tell the current time
- Roll dice for games
- Help make random decisions

Be friendly, helpful, and remember what the user tells you.
When using tools, briefly explain what you're doing.""",
)

# Interactive chat loop
print("=" * 50)
print("ARIA - Your Personal Assistant")
print("=" * 50)
print("Type 'quit' to exit\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ['quit', 'exit', 'q']:
        print("Goodbye!")
        break
    if not user_input:
        continue

    print("\nAria: ", end="")
    agent.print_response(user_input, stream=True)
    print()
