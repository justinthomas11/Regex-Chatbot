import re
import random
from intent_tamil import INTENTS, FALLBACK_RESPONSES
from preprocess_tamil import preprocess

def get_response(user_input: str) -> str:
    cleaned = preprocess(user_input)

    for intent_name, intent_data in INTENTS.items():
        for pattern in intent_data["patterns"]:
            if re.search(pattern, cleaned):
                return random.choice(intent_data["responses"])

    return random.choice(FALLBACK_RESPONSES)
