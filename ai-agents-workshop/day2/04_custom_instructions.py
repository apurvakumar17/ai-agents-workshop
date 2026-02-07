"""
Day 2: The Art of Instructions

Same tools, different instructions = different behavior!
Run this to see how instructions shape the agent.
"""

from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.calculator import CalculatorTools
from agno.tools.duckduckgo import DuckDuckGoTools

tools = [CalculatorTools(), DuckDuckGoTools()]
question = "Who are you?"

# # Style 1: Concise Expert
# print("=" * 50)
# print("STYLE 1: Concise Expert")
# print("=" * 50)
# agent1 = Agent(
#     model=OpenAIChat(id="gpt-4o-mini"),
#     tools=tools,
#     instructions="Be extremely brief. Answer in one sentence maximum.",
#     debug_mode=True
# )
# agent1.print_response(question, stream=True)

# # Style 2: Friendly Teacher
# print("\n" + "=" * 50)
# print("STYLE 2: Friendly Teacher")
# print("=" * 50)
# agent2 = Agent(
#     model=OpenAIChat(id="gpt-4o-mini"),
#     tools=tools,
#     instructions="Explain like I'm learning. Break down the steps simply.",
#     debug_mode=True
# )
# agent2.print_response(question, stream=True)


# Style 4: You are Iron Man
print("\n" + "=" * 50)
print("STYLE 3: Iron Man")
print("=" * 50)
agent3 = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=tools,
    instructions="You are Tony Stark also known as Iron Man of Marvel Comics. Inherit his behaviour",
    debug_mode=True
)
agent3.print_response(question, stream=True)