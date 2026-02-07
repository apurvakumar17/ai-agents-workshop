"""
Day 3: Session Memory

The agent can now remember what you said earlier in the conversation.
This is NOT magic - it's just keeping track of message history!
"""

from dotenv import load_dotenv
load_dotenv()
from agno.db.sqlite import SqliteDb

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.calculator import CalculatorTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[CalculatorTools()],
    add_history_to_context=True,
    num_history_runs=3,
    db=SqliteDb(db_file="tmp/data.db"),
    instructions="You are a friendly assistant. Remember what the user tells you.",
    debug_mode=True
)

# Multi-turn conversation
print("=" * 50)
print("CONVERSATION WITH MEMORY")
print("=" * 50)

# Turn 1: Introduce yourself
print("\n[Turn 1]")
agent.print_response("Hi! My name is Alex and I'm learning about AI agents.", stream=True)

# Turn 2: Ask something unrelated
print("\n[Turn 2]")
agent.print_response("What's 42 * 17?", stream=True)

# Turn 3: Reference earlier context
print("\n[Turn 3]")
agent.print_response("What's my name?", stream=True)

# Turn 4: Continue the context
print("\n[Turn 4]")
agent.print_response("What am I learning about?", stream=True)

print("\n" + "=" * 50)
print("HOW IT WORKS")
print("=" * 50)
print("""
Session memory works by:
1. Storing all messages (user + assistant) in a list
2. Sending the ENTIRE conversation with each new request
3. The LLM sees the full history and can reference it

Limitation: This only lasts for the current session.
When you restart the script, memory is gone!

For PERSISTENT memory across sessions, you need:
- A database to store conversations
- Or RAG (Retrieval-Augmented Generation) for knowledge
""")
