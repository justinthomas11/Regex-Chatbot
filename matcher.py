import re
import random
from intent import INTENTS, FALLBACK_RESPONSES
from preprocess import preprocess

def make_response_dynamic(response: str, query_term: str) -> str:
    if not query_term:
        return response

    query_term_lower = query_term.lower()

    # Pattern 1: Parentheses pattern (abbreviation/full name)
    # e.g., "The Indian Penal Code (IPC) is ..." or "An FIR (First Information Report) is ..."
    p1 = r"^(The|An?|A)?\s*([^(\n]+)\s+\(([^)]+)\)\s+(is|defines|refers to|stands for|are|were|was|guarantees|means|protects|covers|safeguards|lays down)\b"
    m1 = re.match(p1, response, re.IGNORECASE)
    if m1:
        article, name1, name2, verb = m1.groups()
        name1_clean = name1.strip()
        name2_clean = name2.strip()
        
        # Check which one matches query_term better
        if query_term_lower in name2_clean.lower() or name2_clean.lower() in query_term_lower:
            new_prefix = f"The term {name2_clean} ({name1_clean}) {verb}"
        else:
            new_prefix = f"The term {name1_clean} ({name2_clean}) {verb}"
        
        return new_prefix + response[m1.end():]

    # Pattern 2: No parentheses pattern
    # e.g., "Bail is conditional release ..." or "Article 21 of the Indian Constitution guarantees ..."
    p2 = r"^(The|An?|A)?\s*([^(\n]+)\s+(is|defines|refers to|stands for|are|were|was|guarantees|means|protects|covers|safeguards|lays down)\b"
    m2 = re.match(p2, response, re.IGNORECASE)
    if m2:
        article, name, verb = m2.groups()
        name_clean = name.strip()
        
        if query_term_lower in name_clean.lower() or name_clean.lower() in query_term_lower:
            display_term = name_clean
            if query_term_lower == name_clean.lower():
                display_term = query_term
            new_prefix = f"The term {display_term} {verb}"
            return new_prefix + response[m2.end():]

    # Pattern 3: Colon pattern
    # e.g., "India's court hierarchy from top to bottom: Supreme Court ..."
    p3 = r"^([^:\n]{1,80})\s*:\s*"
    m3 = re.match(p3, response)
    if m3:
        prefix = m3.group(1).strip()
        if query_term_lower in prefix.lower():
            # Check capitalization of first letter of response
            first_char = response[0]
            rest_response = response[1:]
            if first_char.isupper():
                first_char = first_char.lower()
            return f"The term {query_term.capitalize()} refers to {first_char}{rest_response}"

    # Fallback
    if len(query_term) <= 4:
        display_term = query_term.upper()
    else:
        display_term = query_term[0].upper() + query_term[1:]
        
    first_char = response[0]
    rest_response = response[1:]
    if first_char.isupper() and not response.startswith("I "):
        first_char = first_char.lower()
    
    return f"The term {display_term} is explained as: {first_char}{rest_response}"

def get_response(user_input: str)-> str:
    cleaned = preprocess(user_input)

    # Detect if user is asking to explain a term
    explain_match = re.search(r"\bexplain\s+(?:the\s+)?term\s+([\w\s\.\-]+)", user_input, re.IGNORECASE)
    query_term = None
    if explain_match:
        query_term = explain_match.group(1).strip("?.! ")

    matched_intent_data = None
    for intent_name, intent_data in INTENTS.items():
        for pattern in intent_data["patterns"]:
            if re.search(pattern, cleaned):
                matched_intent_data = intent_data
                break
        if matched_intent_data:
            break

    if matched_intent_data:
        response = random.choice(matched_intent_data["responses"])
        if query_term:
            return make_response_dynamic(response, query_term)
        return response

    return random.choice(FALLBACK_RESPONSES)