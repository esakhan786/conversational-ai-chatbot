from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import json
from datetime import datetime

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)

chat_history = [
    SystemMessage(content="""
You are a helpful AI assistant.
Answer clearly, politely, and in simple language.
Remember the conversation context.
""")
]

print("AI Chatbot started. Type 'exit' to quit, 'clear' to reset history.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    if user_input.lower() == "clear":
        chat_history = [
            SystemMessage(content="You are a helpful AI assistant.")
        ]
        print("Chat history cleared.\n")
        continue

    chat_history.append(HumanMessage(content=user_input))

    result = model.invoke(chat_history)

    chat_history.append(AIMessage(content=result.content))

    print("AI:", result.content)
    print()

# Save chat history
data = []
for msg in chat_history:
    data.append({
        "type": msg.__class__.__name__,
        "content": msg.content
    })

filename = f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

with open(filename, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print(f"Chat saved in {filename}")