# Nyaya — Indian Legal System Chatbot

A domain-specific rule-based chatbot built with Python that answers questions about the Indian legal system using regex pattern matching.

---

## Overview

Nyaya is a lightweight chatbot that uses regular expressions to match user queries to predefined legal intents and return relevant responses. It covers core topics in Indian law including constitutional rights, criminal procedure, and court structure.

This is a group project built as part of an NLP course at Christ University, Bangalore.

---

## Project Structure

```
RegexChatbot/
├── intents.py        # Intent dictionary — patterns and responses
├── preprocessor.py   # Text normalization before matching
├── matcher.py        # Core regex matching logic
└── main.py           # Chat loop and entry point
```

---

## How It Works

1. User input is received in `main.py`
2. `preprocessor.py` normalizes the text — lowercase, strip punctuation, collapse whitespace
3. `matcher.py` runs `re.search()` against every pattern in every intent
4. The first matching intent returns a randomly selected response
5. If nothing matches, a fallback response is returned

---

## Topics Covered

| Intent | Example Queries |
|---|---|
| Greeting | "Hello", "Hi", "Namaste" |
| IPC | "What is the IPC?", "IPC section 302" |
| Court Hierarchy | "How are courts structured in India?" |
| Supreme Court | "What is the apex court?", "Role of the Supreme Court" |
| High Court | "How many High Courts in India?", "Jurisdiction of High Court" |
| FIR | "How to file an FIR?", "What is a First Information Report?" |
| Bail | "Types of bail", "How to get anticipatory bail?" |
| Fundamental Rights | "What are Fundamental Rights?", "Rights under Part III" |
| Article 21 | "What is Article 21?", "Right to life and personal liberty" |
| Legal Aid | "Can't afford a lawyer", "What is DLSA?" |
| Cognizable Offences | "Can police arrest without a warrant?", "Difference between cognizable and non-cognizable" |
| POCSO | "What is POCSO?", "Child protection laws in India" |

---

## Regex Techniques Used

- **Optional characters** (`?`) — handles "what is" vs "what's"
- **Flexible whitespace** (`\s+`) — handles extra spaces between words
- **Grouped alternatives** (`|`) — matches multiple phrasings in one pattern
- **Wildcard bridging** (`.*`) — skips unknown words between key terms
- **Digit matching** (`\d+`) — catches any IPC section number
- **Word boundaries** (`\b`) — prevents partial word matches
- **Specific → broad ordering** — precise patterns are checked before fallback patterns

---

## Setup

**Requirements**

- Python 3.7+
- No external libraries needed — uses only the built-in `re` and `random` modules

**Run the chatbot**

```bash
git clone https://github.com/your-username/RegexChatbot.git
cd RegexChatbot
python main.py
```

---

## Contributing

This project uses a feature branch workflow. No one pushes directly to `main`.

```bash
# 1. Pull latest main
git checkout main
git pull origin main

# 2. Create your branch
git checkout -b your-name/what-youre-adding

# 3. Make changes, commit, push
git add .
git commit -m "describe what you changed"
git push origin your-name/what-youre-adding

# 4. Open a Pull Request on GitHub — requires 1 approval before merging
```

**Branch naming convention:** `name/what-you-did`
Example: `olive/constitutional-intents`, `mahamat/ipc-sections`

---

## Limitations

- Cannot handle paraphrasing or synonyms outside defined patterns
- No context memory — each message is treated independently
- Regex matching stops at the first hit, so pattern order matters
- Not a substitute for professional legal advice

---

## Disclaimer

This chatbot provides general legal information only. It is not a substitute for advice from a qualified lawyer. Always consult a legal professional for specific legal matters.

---

## Authors

- Justin
- Olive  
- Mahamat

*Christ University, Bangalore — NLP Course Project*
