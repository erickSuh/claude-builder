# Start with an empty message list
from helper import add_assistant_message, add_user_message, chat
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv(override=True)

client = Anthropic()

messages = []

# Add the initial user question
add_user_message(messages, "Define quantum computing in one sentence")

# Get Claude's response
answer = chat(client, messages)

# Add Claude's response to the conversation history
add_assistant_message(messages, answer)

# Add a follow-up question
add_user_message(messages, "Write another sentence")

# Get the follow-up response with full context
final_answer = chat(client, messages)

print(final_answer)