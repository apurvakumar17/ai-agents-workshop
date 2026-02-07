"""
Day 3: Creating Custom Tools

Any Python function can become an agent tool!
The key is the @tool decorator and a good docstring.
"""

from dotenv import load_dotenv
load_dotenv()

import random
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool

# Custom tool: Dice roller
@tool
def roll_dice(sides: int = 6) -> str:
    """Roll a dice with the specified number of sides.

    Args:
        sides: Number of sides on the dice (default: 6)

    Returns:
        The result of the dice roll
    """
    result = random.randint(1, sides)
    return f"Rolled a {result} on a d{sides}"

# Custom tool: Coin flip
@tool
def flip_coin() -> str:
    """Flip a coin and return heads or tails."""
    result = random.choice(["Heads", "Tails"])
    return f"{result}!"

# Custom tool: Random number
@tool
def random_number(min_val: int = 1, max_val: int = 100) -> str:
    """Generate a random number between min and max (inclusive).

    Args:
        min_val: Minimum value (default: 1)
        max_val: Maximum value (default: 100)
    """
    result = random.randint(min_val, max_val)
    return f"Random number: {result}"

# Create agent with custom tools
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[roll_dice, flip_coin, random_number],
    instructions="You are a game master. Use your tools to help with games and random decisions.",
)

# Test the custom tools
print("Testing custom tools:")
print("=" * 50)

agent.print_response("Roll a d20 for my attack roll", stream=True)
print()
agent.print_response("Flip a coin to decide who goes first", stream=True)
print()
agent.print_response("Pick a random number between 1 and 10 for treasure", stream=True)
