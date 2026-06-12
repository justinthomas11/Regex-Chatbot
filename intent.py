# LAYER 1: The data

INTENTS = {
    "greeting": {
        "patterns": [
            r"\b(hello|hi|hey|namaste)\b",
            r"\bgood\s+(morning|evening|afternoon|day)\b",
            r"(hey|hi|hello)\s+there",
        ],
        "responses": [
            "Hello! I can help you with questions about the Indian legal system.",
            "Hi there! Ask me about courts, laws, or your legal rights in India.",
            "Namaste! How can I assist you with Indian law today?"
        ]
    },

    "ipc": {
        "patterns": [
            # specific first — full phrases
            r"(what'?s?|define|explain|tell me about)\s+(the\s+)?i\.?p\.?c\.?",
            r"(what'?s?|define|explain|tell me about)\s+(the\s+)?indian penal code",
            r"(what'?s?|define|explain|tell me about)\s+(the\s+)?penal code",
            # section-specific queries
            r"(ipc|indian penal code)\s+section\s+\d+",
            # broad fallback
            r"\b(ipc|indian penal code|penal code)\b",
        ],
        "responses": [
            "The Indian Penal Code (IPC) is the main criminal code of India, enacted in 1860. It covers all substantive aspects of criminal law.",
            "The IPC defines crimes and their punishments. It has 511 sections covering offences from theft to murder."
        ]
    },

    "court_hierarchy": {
        "patterns": [
            # specific structural queries first
            r"how\s+(are|is)\s+(the\s+)?courts?\s+(structured|organized|arranged|set\s+up)",
            r"(explain|describe|tell me about)\s+(the\s+)?court\s+(hierarchy|structure|system)",
            r"which\s+(courts?)\s+(are\s+there|exist)\s+(in\s+)?india",
            # broad fallback
            r"\b(court hierarchy|court structure|types of courts|judicial system)\b",
        ],
        "responses": [
            "India's court hierarchy from top to bottom: Supreme Court → High Courts (one per state) → District Courts → Sub-divisional Courts → Magistrate Courts."
        ]
    },

    "supreme_court": {
        "patterns": [
            # specific queries first
            r"(what'?s?|tell me about|explain|describe)\s+(the\s+)?supreme court",
            r"(highest|apex|top)\s+court\s+(in\s+)?india",
            r"(role|function|jurisdiction|power)s?\s+of\s+(the\s+)?supreme court",
            # broad fallback
            r"\bsupreme\s+court\b",
        ],
        "responses": [
            "The Supreme Court of India is the highest judicial authority, located in New Delhi. It has original, appellate, and advisory jurisdiction.",
            "India's Supreme Court was established in 1950. It has a Chief Justice and up to 33 other judges."
        ]
    },

    "fir": {
        "patterns": [
            # action-based queries first
            r"how\s+(to|do\s+i|can\s+i)\s+(file|lodge|register)\s+(a\s+)?(complaint|case|fir)",
            r"(steps?|process|procedure)\s+(to|for)\s+(file|filing|register|registering)\s+(a\s+)?fir",
            r"(what\s+happens?|what\s+to\s+do)\s+(after|when)\s+(filing|registering)?\s*(a\s+)?fir",
            # definition queries
            r"(what'?s?|define|explain)\s+(a\s+|the\s+)?(fir|first information report)",
            # broad fallback
            r"\b(fir|first information report)\b",
        ],
        "responses": [
            "An FIR (First Information Report) is filed at a police station to report a cognizable offence. It sets the criminal justice process in motion.",
            "To file an FIR: visit your nearest police station, describe the offence, and the officer must register it under Section 154 CrPC. You're entitled to a free copy."
        ]
    },

    "fundamental_rights": {
        "patterns": [
            # specific queries first
            r"(what are|list|explain|tell me about)\s+(the\s+)?fundamental rights?",
            r"rights?\s+(guaranteed|given|provided)\s+by\s+(the\s+)?constitution",
            r"(what is|explain)\s+part\s+iii\s+(of\s+(the\s+)?constitution)?",
            r"how\s+many\s+fundamental\s+rights?\s+(are\s+there)?\s*(in\s+india)?",
            # broad fallback
            r"\bfundamental\s+rights?\b",
        ],
        "responses": [
            "The 6 Fundamental Rights in India (Part III of Constitution): Right to Equality, Right to Freedom, Right against Exploitation, Right to Freedom of Religion, Cultural/Educational Rights, Right to Constitutional Remedies."
        ]
    },

    "bail": {
        "patterns": [
            # specific action queries first
            r"how\s+(do\s+i|can\s+i|to)\s+(get|apply\s+for|obtain)\s+bail",
            r"(types?|kinds?|forms?)\s+of\s+bail|bail\s+(types?|kinds?)",
            r"(what is|explain|define)\s+(a\s+|the\s+)?bail",
            r"(arrested|in\s+custody|in\s+jail).*(bail)",
            r"(anticipatory|regular|interim)\s+bail",
            r"bail\s+under\s+section\s+(437|438|439)",
            # broad fallback
            r"\bbail\b",
        ],
        "responses": [
            "Bail is conditional release of an arrested person. Types: Regular bail (Section 437/439 CrPC), Anticipatory bail (Section 438 CrPC), and Interim bail.",
            "Anticipatory bail is applied for BEFORE arrest. Regular bail is applied for after arrest. A sessions court or High Court can grant anticipatory bail."
        ]
    },

    "article_21": {
        "patterns": [
            # specific queries first
            r"(what'?s?|explain|define|tell me about)\s+article\s*21",
            r"right\s+to\s+(life|personal\s+liberty|privacy|dignity)",
            r"article\s*21\s+(of\s+(the\s+)?constitution)?",
            r"(deprive|violation).*(life|liberty)",
            # broad fallback
            r"\barticle\s*21\b",
        ],
        "responses": [
            "Article 21 of the Indian Constitution guarantees the Right to Life and Personal Liberty. No person can be deprived of their life or liberty except according to procedure established by law.",
            "Article 21 is one of the most important fundamental rights. Courts have expanded it to include right to privacy, right to education, right to health, and right to a dignified life."
        ]
    },

    "legal_aid": {
        "patterns": [
            # specific situation queries first
            r"(can'?t|cannot|cant|don'?t)\s+(afford|pay\s+for)\s+(a\s+)?lawyer",
            r"how\s+(do\s+i|can\s+i)\s+get\s+(a\s+)?free\s+lawyer",
            r"(what is|explain|tell me about)\s+(legal\s+aid|free\s+legal\s+help)",
            r"right\s+to\s+(a\s+)?lawyer",
            r"(dlsa|district legal services)",
            r"article\s*39\s*a",
            # broad fallback
            r"\b(legal\s+aid|free\s+lawyer|free\s+legal\s+help)\b",
        ],
        "responses": [
            "Under Article 39A of the Constitution, free legal aid is a fundamental right. If you cannot afford a lawyer, the state must provide one.",
            "You can get free legal help through the District Legal Services Authority (DLSA) in your district. Every accused person has the right to legal representation regardless of financial status."
        ]
    },

    "cognizable_offences": {
        "patterns": [
            # specific comparison queries first
            r"(difference|distinguish|compare)\s+between\s+cognizable\s+and\s+non[\s\-]?cognizable",
            r"(what is|explain|define)\s+(a\s+)?cognizable\s+offence",
            r"can\s+police\s+(arrest|detain)\s+without\s+(a\s+)?warrant",
            r"(arrest\s+without|warrantless)\s+arrest",
            # broad fallback
            r"\b(cognizable|non[\s\-]?cognizable)\b",
        ],
        "responses": [
            "A cognizable offence is one where police can arrest without a warrant — like murder, robbery, or rape. A non-cognizable offence requires a warrant for arrest — like cheating or defamation.",
            "Cognizable offences are serious crimes where police have immediate power to arrest and investigate. Non-cognizable offences require prior permission from a magistrate."
        ]
    },

    "high_court": {
        "patterns": [
            # specific queries first
            r"(what does|role|function|jurisdiction|power)s?\s+(of\s+)?(the\s+)?high\s+court",
            r"how\s+many\s+high\s+courts?\s+(are\s+there\s+)?(in\s+india)?",
            r"(what'?s?|explain|tell me about)\s+(the\s+)?high\s+court",
            r"(appeal|writ)\s+(to|in|at)\s+(the\s+)?high\s+court",
            # broad fallback
            r"\bhigh\s+court\b",
        ],
        "responses": [
            "India has 25 High Courts, one for each state or group of states. They have original, appellate, and supervisory jurisdiction over all courts within their territory.",
            "A High Court is the highest court within a state. It hears appeals from district courts and has the power to issue writs for enforcement of fundamental rights."
        ]
    },

    "pocso": {
        "patterns": [
            # specific queries first
            r"(what'?s?|explain|define|tell me about)\s+(the\s+)?pocso(\s+act)?",
            r"protection\s+of\s+children\s+from\s+sexual\s+offences",
            r"child\s+(sexual\s+)?(abuse|offence|assault|harassment)",
            r"(law|act|protection)\s+(for|against)\s+(child|minor|children)",
            # broad fallback
            r"\bpocso\b",
        ],
        "responses": [
            "POCSO (Protection of Children from Sexual Offences Act, 2012) is a comprehensive law protecting children under 18 from sexual abuse, harassment, and exploitation.",
            "Under POCSO, any sexual offence against a child under 18 is a criminal offence. It mandates child-friendly court procedures and strict punishments. Reporting is mandatory — failure to report is also an offence."
        ]
    },

    "goodbye": {
        "patterns": [
            r"\b(bye|goodbye|see\s+you|exit|quit)\b",
            r"\b(thanks|thank\s+you|thank\s+u|thx)\b",
            r"(that'?s?\s+all|i'?m\s+done|no\s+more\s+questions?)",
        ],
        "responses": [
            "Goodbye! Remember to always consult a qualified lawyer for specific legal advice.",
            "Take care! This bot provides general information only, not legal advice."
        ]
    }
}

FALLBACK_RESPONSES = [
    "I don't have information on that specific topic yet. Try asking about: FIR, bail, IPC, Supreme Court, or Fundamental Rights.",
    "That's outside my current knowledge. I can help with courts, FIR filing, bail, or constitutional rights."
]