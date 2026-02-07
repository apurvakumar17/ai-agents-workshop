"""
Day 2: Adding Web Search

Now the agent can access real-time information from the web!
Watch for "[Tool: duckduckgo_search]" in the output.
"""

from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools # type: ignore

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    instructions="Search the web for current information. Cite your sources.",
    debug_mode=True
)

# The same question from Day 1 - but now with web search!
print("Testing: Current information")
print("-" * 30)
agent.print_response("What's the weather in Tokyo right now?", stream=True)

print("\n\nTry asking about recent news:")
print("-" * 30)
agent.print_response("What are the top tech news stories today?", stream=True)
