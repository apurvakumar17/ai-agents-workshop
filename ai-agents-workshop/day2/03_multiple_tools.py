"""
Day 2: Multiple Tools

The agent can now choose between tools based on the question.
Watch how it picks the right tool for each task!
"""

from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.calculator import CalculatorTools
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[CalculatorTools(), DuckDuckGoTools()],
    instructions="""You are a helpful assistant with access to:
    - A calculator for math operations
    - Web search for current information

    Use the appropriate tool for each task.""",
    debug_mode=True
)

# Test different types of questions
questions = [
    "What is the capital of India?",           # Should use calculator
    "What is the square root of 144?",           # Should use calculator
    "Who won the last Super Bowl?",               # Should use web search
    "What is 20% tip on a $85 dinner bill?",     # Should use calculator
    "What's the current price of Bitcoin?",       # Should use web search
]

for q in questions:
    print(f"\n{'='*50}")
    print(f"Question: {q}")
    print("=" * 50)
    agent.print_response(q, stream=True)
