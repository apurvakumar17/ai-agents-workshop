"""
Day 2: Adding a Calculator Tool

Compare this to Day 1's math test - now the agent can do accurate calculations!
Watch for "[Tool: calculator]" in the output.
"""

from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.calculator import CalculatorTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[CalculatorTools()],
    instructions="Use the calculator for any math operations. Show your work.",
    debug_mode=True  # This lets us see when tools are used!
)

# The same question from Day 1 - but now with tools!
print("Testing: 847 * 293")
print("-" * 30)
agent.print_response("What is 847 * 293?", stream=True)

print("\n\nTry some more complex math:")
print("-" * 30)
agent.print_response("What is 15% of 847, then multiply that by 3.14?", stream=True)
agent.print_response("Capital of India is?", stream=True)
