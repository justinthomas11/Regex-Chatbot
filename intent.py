#LAYER 1: The data

INTENTS = {
    "greeting": {
        "patterns": [
            r"\b(hello|hi|hey|namaste|good morning|good evening)\b"
        ],
        "responses": [
            "Hello! I can help you with questions about the Indian legal system.",
            "Hi there! Ask me about courts, laws, or your legal rights in India.",
            "Namaste! How can I assist you with Indian law today?"
        ]
    },
    "ipc": {
        "patterns": [
            r"\b(ipc|indian penal code|penal code)\b",
            r"what is ipc",
            r"tell me about ipc"
        ],
        "responses": [
            "The Indian Penal Code (IPC) is the main criminal code of India, enacted in 1860. It covers all substantive aspects of criminal law.",
            "The IPC defines crimes and their punishments. It has 511 sections covering offences from theft to murder."
        ]
    },
    "court_hierarchy": {
        "patterns": [
            r"\b(court hierarchy|court structure|types of courts|judicial system)\b",
            r"how (are|is) (the )?courts? (structured|organized|arranged)",
            r"which (court|courts) (are there|exist) in india"
        ],
        "responses": [
            "India's court hierarchy from top to bottom: Supreme Court → High Courts (one per state) → District Courts → Sub-divisional Courts → Magistrate Courts.",
        ]
    },
    "supreme_court": {
        "patterns": [
            r"\b(supreme court)\b",
            r"highest court in india",
            r"apex court"
        ],
        "responses": [
            "The Supreme Court of India is the highest judicial authority, located in New Delhi. It has original, appellate, and advisory jurisdiction.",
            "India's Supreme Court was established in 1950. It has a Chief Justice and up to 33 other judges."
        ]
    },
    "fir": {
        "patterns": [
            r"\b(fir|first information report)\b",
            r"how to (file|lodge|register) a (complaint|case|fir)",
        ],
        "responses": [
            "An FIR (First Information Report) is filed at a police station to report a cognizable offence. It sets the criminal justice process in motion.",
            "To file an FIR: visit your nearest police station, describe the offence, and the officer must register it under Section 154 CrPC. You're entitled to a free copy."
        ]
    },
    "fundamental_rights": {
        "patterns": [
            r"\b(fundamental rights?)\b",
            r"rights? (guaranteed|given|provided) by (the )?constitution",
            r"part iii (of the constitution)?"
        ],
        "responses": [
            "The 6 Fundamental Rights in India (Part III of Constitution): Right to Equality, Right to Freedom, Right against Exploitation, Right to Freedom of Religion, Cultural/Educational Rights, Right to Constitutional Remedies.",
        ]
    },
    "bail": {
        "patterns": [
            r"\b(bail)\b",
            r"how (to get|do i get|can i get) bail",
            r"types of bail"
        ],
        "responses": [
            "Bail is conditional release of an arrested person. Types: Regular bail (Section 437/439 CrPC), Anticipatory bail (Section 438 CrPC), and Interim bail.",
            "Anticipatory bail is applied for BEFORE arrest. Regular bail is applied for after arrest. A sessions court or High Court can grant anticipatory bail."
        ]
    },
    "goodbye": {
        "patterns": [
            r"\b(bye|goodbye|see you|exit|quit|thanks|thank you)\b"
        ],
        "responses": [
            "Goodbye! Remember to always consult a qualified lawyer for specific legal advice.",
            "Take care! This bot provides general information only, not legal advice."
        ]
    }
}

FALLBACK_RESPONSES = [
    "I don't have information on that specific topic yet. Try asking about: FIR, bail, IPC, Supreme Court, or Fundamental Rights.",
    "That's outside my current knowledge. I can help with courts, FIR filing, bail, or constitutional rights.",
]