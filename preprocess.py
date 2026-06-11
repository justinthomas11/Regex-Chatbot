import re

def preprocess(text:str) -> str:
    text= text.lower().strip()
    text= re.sub(r'\s+', ' ', text)
    text= re.sub(r"[^\w\s']",' ', text)
    return text


