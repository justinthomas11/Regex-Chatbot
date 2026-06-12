import re

def preprocess(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'\s+', ' ', text)
    # keep dots so i.p.c stays intact before matching
    text = re.sub(r"[^\w\s\.]", ' ', text)
    return text