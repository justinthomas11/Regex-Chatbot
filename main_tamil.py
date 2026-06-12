import re
import sys

# Ensure Tamil text renders correctly on Windows consoles
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

from matcher_tamil import get_response
from intent_tamil import INTENTS
from preprocess_tamil import preprocess

def run_chatbot():
    print("இந்திய சட்ட அமைப்பு சாட்போட் (தமிழ்)")
    print("வெளியேற 'போய் வருகிறேன்' என்று தட்டச்சு செய்யுங்கள்.\n")

    while True:
        user_input = input("நீங்கள்: ").strip()
        if not user_input:
            continue

        response = get_response(user_input)
        print(f"போட்: {response}\n")

        cleaned = preprocess(user_input)

        for pattern in INTENTS["goodbye"]["patterns"]:
            if re.search(pattern, cleaned):
                break
        else:
            continue
        break

if __name__ == "__main__":
    run_chatbot()
