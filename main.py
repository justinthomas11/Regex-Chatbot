import re

from matcher import get_response
from intent import INTENTS
from preprocess import preprocess

def run_chatbot():
    print("Indian Legal System Chatbot")
    print("Type 'bye' to exit.\n")

    while True:
        user_input= input("You: ").strip()
        if not user_input:
            continue

        response= get_response(user_input)
        print(f"Bot:{response}\n")

        cleaned = preprocess(user_input)

        for pattern in INTENTS["goodbye"]["patterns"]:
            if re.search(pattern, cleaned):
                break

        else:
            continue
        break

if __name__ == "__main__":
    run_chatbot()