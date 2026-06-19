import re

def preprocess(text: str) -> str:
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    # Remove punctuation but keep Tamil characters, digits, dots, and spaces
    text = re.sub(r"[^\u0B80-\u0BFF\w\s\.]", ' ', text)
    return text
