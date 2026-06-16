# LAYER 1: The data

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
            "India's court hierarchy from top to bottom: Supreme Court → High Courts (one per state) → District Courts → Sub-divisional Courts → Magistrate Courts."
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
            r"how to (file|lodge|register) a (complaint|case|fir)"
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
            "The 6 Fundamental Rights in India (Part III of Constitution): Right to Equality, Right to Freedom, Right against Exploitation, Right to Freedom of Religion, Cultural/Educational Rights, Right to Constitutional Remedies."
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

    "article_21": {
        "patterns": [
            r"\b(article 21)\b",
            r"right to life",
            r"right to (life|personal liberty)",
            r"what is article 21"
        ],
        "responses": [
            "Article 21 of the Indian Constitution guarantees the Right to Life and Personal Liberty. No person can be deprived of their life or liberty except according to procedure established by law.",
            "Article 21 is one of the most important fundamental rights. Courts have expanded it to include right to privacy, right to education, right to health, and right to a dignified life."
        ]
    },

    "legal_aid": {
        "patterns": [
            r"\b(legal aid|free lawyer|free legal help)\b",
            r"(can't|cannot|cant) afford (a )?lawyer",
            r"right to (a )?lawyer",
            r"how (do i|can i) get (a )?free lawyer"
        ],
        "responses": [
            "Under Article 39A of the Constitution, free legal aid is a fundamental right. If you cannot afford a lawyer, the state must provide one.",
            "You can get free legal help through the District Legal Services Authority (DLSA) in your district. Every accused person has the right to legal representation regardless of financial status."
        ]
    },

    "cognizable_offences": {
        "patterns": [
            r"\b(cognizable|non[\s-]?cognizable)\b",
            r"(difference|distinguish) between cognizable and non[\s-]?cognizable",
            r"what is a cognizable offence",
            r"can police arrest without warrant"
        ],
        "responses": [
            "A cognizable offence is one where police can arrest without a warrant — like murder, robbery, or rape. A non-cognizable offence requires a warrant for arrest — like cheating or defamation.",
            "Cognizable offences are serious crimes where police have immediate power to arrest and investigate. Non-cognizable offences require prior permission from a magistrate."
        ]
    },

    "high_court": {
        "patterns": [
            r"\b(high court)\b",
            r"what does (the )?high court do",
            r"jurisdiction of high court",
            r"how many high courts (are there )?(in india)?"
        ],
        "responses": [
            "India has 25 High Courts, one for each state or group of states. They have original, appellate, and supervisory jurisdiction over all courts within their territory.",
            "A High Court is the highest court within a state. It hears appeals from district courts and has the power to issue writs for enforcement of fundamental rights."
        ]
    },

    "pocso": {
        "patterns": [
            r"\b(pocso)\b",
            r"protection of children from sexual offences",
            r"child sexual (abuse|offence|assault)",
            r"what is pocso"
        ],
        "responses": [
            "POCSO (Protection of Children from Sexual Offences Act, 2012) is a comprehensive law protecting children under 18 from sexual abuse, harassment, and exploitation.",
            "Under POCSO, any sexual offence against a child under 18 is a criminal offence. It mandates child-friendly court procedures and strict punishments. Reporting is mandatory — failure to report is also an offence."
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
    },

    "constitution_of_india": {
    "patterns": [
    r"(what'?s?|explain|define|tell me about)\s+(the\s+)?constitution\s+of\s+india",
    r"indian\s+constitution",
    r"\bconstitution\b"
    ],
    "responses": [
    "The Constitution of India is the supreme law of the country. It came into force on 26 January 1950 and lays down the framework of governance and citizens' rights."
    ]
    },

    "directive_principles": {
    "patterns": [
    r"(what'?s?|explain|define|tell me about)\s+(the\s+)?directive\s+principles",
    r"directive\s+principles\s+of\s+state\s+policy",
    r"\bdpsp\b"
    ],
    "responses": [
    "Directive Principles of State Policy are guidelines in Part IV of the Constitution that direct the government to promote social and economic welfare."
    ]
    },

    "fundamental_duties": {
    "patterns": [
    r"(what'?s?|explain|define|tell me about)\s+(the\s+)?fundamental\s+duties",
    r"list\s+of\s+fundamental\s+duties",
    r"\bfundamental\s+duties\b"
    ],
    "responses": [
    "Fundamental Duties are listed in Article 51A of the Constitution. Citizens are expected to follow these duties to promote harmony and national integrity."
    ]
    },

    "president_of_india": {
    "patterns": [
    r"(what'?s?|explain|tell me about)\s+(the\s+)?president\s+of\s+india",
    r"role\s+of\s+(the\s+)?president",
    r"\bpresident\s+of\s+india\b"
    ],
    "responses": [
    "The President of India is the constitutional head of the country and acts on the advice of the Council of Ministers."
    ]
    },

    "parliament": {
    "patterns": [
    r"(what'?s?|explain|tell me about)\s+(the\s+)?parliament",
    r"indian\s+parliament",
    r"\bparliament\b"
    ],
    "responses": [
    "The Parliament of India consists of the President, Lok Sabha, and Rajya Sabha. It is responsible for making laws for the country."
    ]
    },

    "lok_sabha": {
    "patterns": [
    r"(what'?s?|explain|tell me about)\s+(the\s+)?lok\s+sabha",
    r"lower\s+house\s+of\s+parliament",
    r"\blok\s+sabha\b"
    ],
    "responses": [
    "Lok Sabha is the House of the People and the lower house of Parliament. Its members are directly elected by citizens."
    ]
    },

    "rajya_sabha": {
    "patterns": [
    r"(what'?s?|explain|tell me about)\s+(the\s+)?rajya\s+sabha",
    r"upper\s+house\s+of\s+parliament",
    r"\brajya\s+sabha\b"
    ],
    "responses": [
    "Rajya Sabha is the Council of States and the upper house of Parliament. Its members represent the states and union territories."
    ]
    },

    "governor": {
    "patterns": [
    r"(what'?s?|explain|tell me about)\s+(the\s+)?governor",
    r"role\s+of\s+(the\s+)?governor",
    r"\bgovernor\b"
    ],
    "responses": [
    "A Governor is the constitutional head of a state and acts on the advice of the state's Council of Ministers."
    ]
    },

    "chief_minister": {
    "patterns": [
    r"(what'?s?|explain|tell me about)\s+(the\s+)?chief\s+minister",
    r"role\s+of\s+(the\s+)?chief\s+minister",
    r"\bchief\s+minister\b"
    ],
    "responses": [
    "The Chief Minister is the head of the state government and exercises executive authority in the state."
    ]
    },

    "writs": {
    "patterns": [
    r"(what'?s?|explain|define|tell me about)\s+writs?",
    r"types\s+of\s+writs?",
    r"\bwrits?\b"
    ],
    "responses": [
    "The Constitution provides five writs: Habeas Corpus, Mandamus, Certiorari, Prohibition, and Quo Warranto for protecting legal and fundamental rights."
    ]
    },

    "habeas_corpus": {
    "patterns": [
    r"(what'?s?|explain|define)\s+habeas\s+corpus",
    r"\bhabeas\s+corpus\b"
    ],
    "responses": [
    "Habeas Corpus means 'produce the body'. It is issued to bring a detained person before the court and protect against unlawful detention."
    ]
    },

    "mandamus": {
    "patterns": [
    r"(what'?s?|explain|define)\s+mandamus",
    r"\bmandamus\b"
    ],
    "responses": [
    "Mandamus means 'we command'. It is issued by a court directing a public authority to perform its legal duty."
    ]
    },

    "certiorari": {
    "patterns": [
    r"(what'?s?|explain|define)\s+certiorari",
    r"\bcertiorari\b"
    ],
    "responses": [
    "Certiorari is issued by a higher court to quash an order passed by a lower court or tribunal acting beyond its jurisdiction."
    ]
    },

    "prohibition": {
    "patterns": [
    r"(what'?s?|explain|define)\s+prohibition",
    r"writ\s+of\s+prohibition",
    r"\bprohibition\b"
    ],
    "responses": [
    "The writ of Prohibition is issued by a higher court to stop a lower court or tribunal from exceeding its jurisdiction."
    ]
    },

    "quo_warranto": {
    "patterns": [
    r"(what'?s?|explain|define)\s+quo\s+warranto",
    r"\bquo\s+warranto\b"
    ],
    "responses": [
    "Quo Warranto means 'by what authority'. It is issued to question a person's legal right to hold a public office."
    ]
    },

    "pil": {
    "patterns": [
    r"(what'?s?|explain|define)\s+(pil|public\s+interest\s+litigation)",
    r"\bpil\b",
    r"public\s+interest\s+litigation"
    ],
    "responses": [
    "Public Interest Litigation (PIL) allows any person to approach the court to protect public interest and enforce legal rights of disadvantaged groups."
    ]
    },

    "consumer_rights": {
    "patterns": [
    r"(what'?s?|explain|tell me about)\s+consumer\s+rights",
    r"rights\s+of\s+consumers",
    r"\bconsumer\s+rights\b"
    ],
    "responses": [
    "Consumer rights include the right to safety, information, choice, representation, redressal, and consumer education under consumer protection laws."
    ]
    },

}

FALLBACK_RESPONSES = [
    "I don't have information on that specific topic yet. Try asking about: FIR, bail, IPC, Supreme Court, or Fundamental Rights.",
    "That's outside my current knowledge. I can help with courts, FIR filing, bail, or constitutional rights."
]