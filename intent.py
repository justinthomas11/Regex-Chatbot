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

    # =============================================
    # 15 NEW INTENTS BELOW
    # =============================================

    "rti": {
        "patterns": [
            r"(what'?s?|explain|define|tell me about)\s+(the\s+)?(rti|right to information)(\s+act)?",
            r"how\s+(do\s+i|can\s+i|to)\s+(file|submit|make)\s+(an?\s+)?rti",
            r"(rti|right to information)\s+(application|request|query)",
            r"(process|procedure|steps?)\s+(to|for)\s+(file|filing)\s+(an?\s+)?rti",
            r"\b(rti|right to information)\b",
        ],
        "responses": [
            "The Right to Information (RTI) Act, 2005 empowers citizens to request information from public authorities. You can file an RTI application with a fee of ₹10 to any government body.",
            "To file an RTI: write an application to the Public Information Officer (PIO) of the concerned department, pay ₹10 fee, and they must reply within 30 days. Appeals can go to the Central/State Information Commission."
        ]
    },

    "domestic_violence": {
        "patterns": [
            r"(what'?s?|explain|define|tell me about)\s+(the\s+)?domestic\s+violence(\s+act)?",
            r"(protection|law|act)\s+(against|from|for)\s+domestic\s+violence",
            r"(husband|spouse|partner|in[\s\-]?laws?)\s+(abuse|beat|assault|harass|violence)",
            r"how\s+(do\s+i|can\s+i|to)\s+(report|file\s+a\s+case\s+for)\s+domestic\s+violence",
            r"(women'?s?\s+protection|protection\s+of\s+women)\s+(act|law)",
            r"\bdomestic\s+violence\b",
        ],
        "responses": [
            "The Protection of Women from Domestic Violence Act, 2005 covers physical, emotional, verbal, sexual, and economic abuse. It provides for protection orders, residence orders, and monetary relief.",
            "If you face domestic violence, you can approach a Protection Officer, file a complaint at the nearest police station, or contact the Women Helpline at 181. The law also covers live-in relationships."
        ]
    },

    "consumer_rights": {
        "patterns": [
            r"(what'?s?|explain|define|tell me about)\s+(the\s+)?(consumer\s+(protection|rights?)|consumer\s+act)",
            r"(file|lodge|register)\s+(a\s+)?consumer\s+complaint",
            r"(defective|faulty)\s+(product|goods|service)",
            r"consumer\s+(court|forum|commission|dispute)",
            r"(cheated|fraud|scam)\s+by\s+(a\s+)?(seller|company|shop|merchant)",
            r"\b(consumer\s+rights?|consumer\s+protection|consumer\s+court)\b",
            r"rights\s+of\s+consumers",
        ],
        "responses": [
            "The Consumer Protection Act, 2019 safeguards buyers against defective goods, deficient services, unfair trade practices, and misleading advertisements. Complaints can be filed online at edaakhil.nic.in.",
            "Consumer disputes are handled by: District Commission (claims up to ₹1 crore), State Commission (₹1–10 crore), and National Commission (above ₹10 crore). No lawyer is mandatory — you can argue your own case.",
            "Consumer rights include the right to safety, information, choice, representation, redressal, and consumer education under consumer protection laws."
        ]
    },

    "crpc": {
        "patterns": [
            r"(what'?s?|explain|define|tell me about)\s+(the\s+)?(crpc|cr\.?p\.?c\.?|code\s+of\s+criminal\s+procedure)",
            r"(difference|distinguish)\s+between\s+(ipc|crpc|cpc)\s+and\s+(ipc|crpc|cpc)",
            r"criminal\s+procedure\s+code",
            r"\b(crpc|cr\.?p\.?c\.?|code\s+of\s+criminal\s+procedure)\b",
        ],
        "responses": [
            "The Code of Criminal Procedure (CrPC), 1973 lays down the procedural framework for criminal law enforcement — how investigations, arrests, trials, and appeals are conducted.",
            "While the IPC defines WHAT is a crime and its punishment, the CrPC defines HOW the criminal justice process works — from FIR to investigation, charge sheet, trial, and sentencing."
        ]
    },

    "cyber_crime": {
        "patterns": [
            r"(what'?s?|explain|define|tell me about)\s+(cyber\s+crime|cyber\s+law|it\s+act)",
            r"(how\s+(do\s+i|can\s+i|to)\s+)?(report|file|complain\s+about)\s+(a\s+)?cyber\s+crime",
            r"(online|internet|digital)\s+(fraud|scam|hack|hacking|theft|crime)",
            r"(information\s+technology|it)\s+act",
            r"(identity\s+theft|phishing|ransomware|data\s+breach)",
            r"\b(cyber\s+crime|cyber\s+law|cyber\s+fraud)\b",
        ],
        "responses": [
            "Cyber crimes in India are governed by the Information Technology Act, 2000. Common offences include hacking (Sec 66), identity theft (Sec 66C), cyber stalking (Sec 354D IPC), and data theft (Sec 43).",
            "To report a cyber crime: file a complaint at cybercrime.gov.in, visit the nearest Cyber Crime Cell, or call the Cyber Crime Helpline 1930. Preserve all digital evidence (screenshots, emails, URLs)."
        ]
    },

    "divorce": {
        "patterns": [
            r"(what'?s?|explain|tell me about)\s+(the\s+)?(divorce|divorce\s+law|divorce\s+procedure)",
            r"how\s+(do\s+i|can\s+i|to)\s+(get|file\s+for|apply\s+for)\s+(a\s+)?divorce",
            r"(grounds?|reasons?)\s+(for|of)\s+divorce",
            r"(mutual\s+consent|contested)\s+divorce",
            r"(maintenance|alimony)\s+(after|during|in)\s+divorce",
            r"\bdivorce\b",
        ],
        "responses": [
            "Divorce in India is governed by personal laws: Hindu Marriage Act (Hindus), Special Marriage Act (inter-faith), Muslim Personal Law, Indian Divorce Act (Christians). Grounds include cruelty, adultery, desertion, and mental disorder.",
            "Mutual consent divorce requires both spouses to agree and has a 6-month cooling period (can be waived by court). Contested divorce can take 2-5 years. Maintenance/alimony is decided based on income, lifestyle, and needs."
        ]
    },

    "pil": {
        "patterns": [
            r"(what'?s?|explain|define|tell me about)\s+(a\s+|the\s+)?pil",
            r"(what'?s?|explain|define|tell me about)\s+(a\s+|the\s+)?public\s+interest\s+litigation",
            r"how\s+(do\s+i|can\s+i|to)\s+file\s+(a\s+)?pil",
            r"(who\s+can|can\s+anyone)\s+file\s+(a\s+)?pil",
            r"\b(pil|public\s+interest\s+litigation)\b",
        ],
        "responses": [
            "A Public Interest Litigation (PIL) is a case filed in the High Court or Supreme Court in the interest of the general public. Any citizen can file it — even by writing a letter to the Chief Justice.",
            "PILs were introduced to provide access to justice for disadvantaged groups. They cover issues like environmental protection, corruption, human rights violations, and public health. No court fee is required for a PIL.",
            "Public Interest Litigation (PIL) allows any person to approach the court to protect public interest and enforce legal rights of disadvantaged groups."
        ]
    },

    "sedition": {
        "patterns": [
            r"(what'?s?|explain|define|tell me about)\s+(the\s+)?sedition(\s+law)?",
            r"(section|sec)\s+124\s*a",
            r"(ipc|penal\s+code)\s+(section\s+)?124\s*a",
            r"(charged\s+with|arrested\s+for|accused\s+of)\s+sedition",
            r"\bsedition\b",
        ],
        "responses": [
            "Sedition (Section 124A IPC) criminalizes acts that bring hatred, contempt, or disaffection towards the Government of India. It carries punishment up to life imprisonment.",
            "The Supreme Court in 2022 effectively suspended the sedition law, directing that no new cases be filed until the government reconsiders the provision. The law has been widely debated as conflicting with free speech (Article 19)."
        ]
    },

    "dowry": {
        "patterns": [
            r"(what'?s?|explain|define|tell me about)\s+(the\s+)?dowry(\s+(prohibition|law|act))?",
            r"(demand|giving|taking|asking\s+for)\s+dowry",
            r"dowry\s+(harassment|death|torture|demand|complaint)",
            r"section\s+498\s*a",
            r"\b(dowry|498\s*a)\b",
        ],
        "responses": [
            "The Dowry Prohibition Act, 1961 makes giving or taking dowry a criminal offence punishable by up to 5 years imprisonment and ₹15,000 fine (or value of dowry, whichever is more).",
            "Dowry harassment is punishable under Section 498A IPC (cruelty by husband/relatives — up to 3 years). Dowry death (Section 304B IPC) carries a minimum 7 years to life imprisonment."
        ]
    },

    "juvenile_justice": {
        "patterns": [
            r"(what'?s?|explain|define|tell me about)\s+(the\s+)?juvenile\s+justice(\s+act)?",
            r"(law|act|rules?)\s+(for|about|regarding)\s+(juvenile|minor|child)\s+(offender|crime|delinquen)",
            r"(can|will)\s+(a\s+)?(minor|juvenile|child)\s+(be\s+)?(tried|punished|arrested|jailed)",
            r"juvenile\s+(court|board|home|delinquen)",
            r"\bjuvenile\s+justice\b",
        ],
        "responses": [
            "The Juvenile Justice (Care and Protection of Children) Act, 2015 governs children in conflict with the law. Children under 18 are tried by the Juvenile Justice Board (JJB), not regular courts.",
            "Under the JJ Act, children aged 16-18 accused of heinous offences may be tried as adults after a preliminary assessment. Children below 16 cannot be tried as adults. Rehabilitation and reformation are prioritized over punishment."
        ]
    },

    "lok_adalat": {
        "patterns": [
            r"(what'?s?|explain|define|tell me about)\s+(a\s+|the\s+)?lok\s+adalat",
            r"(people'?s?\s+court|alternative\s+dispute\s+resolution|adr)",
            r"how\s+(does|do)\s+(a\s+)?lok\s+adalat\s+work",
            r"(settle|resolve)\s+(case|dispute)\s+(in|through|at|via)\s+(a\s+)?lok\s+adalat",
            r"\blok\s+adalat\b",
        ],
        "responses": [
            "A Lok Adalat (People's Court) is an alternative dispute resolution mechanism where cases are settled amicably. Its decisions are final, binding, and non-appealable. No court fee is charged.",
            "Lok Adalats can settle motor accident claims, matrimonial disputes, labour disputes, and cases pending in courts. If both parties agree, the matter is resolved in a single sitting — saving years of litigation."
        ]
    },

    "defamation": {
        "patterns": [
            r"(what'?s?|explain|define|tell me about)\s+(the\s+)?(law\s+(of|on)\s+)?defamation",
            r"(can\s+i|how\s+to)\s+(sue|file\s+a\s+case)\s+for\s+defamation",
            r"(someone|person)\s+(defamed|slandered|libeled)\s+me",
            r"(section|sec)\s+499|section\s+500",
            r"(criminal|civil)\s+defamation",
            r"\bdefamation\b",
        ],
        "responses": [
            "Defamation in India is both a civil wrong (tort) and a criminal offence (Sections 499-500 IPC). Criminal defamation carries up to 2 years imprisonment. Civil defamation can result in monetary compensation.",
            "To prove defamation, the statement must be: (1) false, (2) published to a third party, (3) harmful to reputation. Truth is a valid defence. Defamation can be spoken (slander) or written (libel)."
        ]
    },

    "cheque_bounce": {
        "patterns": [
            r"(what'?s?|explain|tell me about)\s+(the\s+)?(law\s+(on|for)\s+)?cheque\s+bounce",
            r"(section|sec)\s+138\s+(of\s+)?(ni\s+act|negotiable\s+instruments?)",
            r"cheque\s+(dishonour|bounced?|return)",
            r"(what\s+to\s+do|action|remedy)\s+(if|when)\s+(a\s+)?cheque\s+(bounce|dishonour|return)",
            r"\bcheque\s+bounce\b",
        ],
        "responses": [
            "Cheque bounce is an offence under Section 138 of the Negotiable Instruments Act, 1881. Punishment is up to 2 years imprisonment or fine up to twice the cheque amount, or both.",
            "If a cheque bounces: (1) Send a legal notice within 30 days of receiving the bank memo, (2) Wait 15 days for payment, (3) If unpaid, file a complaint in court within 30 days of the notice period expiring."
        ]
    },

    "property_law": {
        "patterns": [
            r"(what'?s?|explain|tell me about)\s+(the\s+)?(property\s+law|transfer\s+of\s+property|property\s+rights?)",
            r"(how\s+to|process\s+(of|for))\s+(transfer|register|buy|sell)\s+(a\s+)?property",
            r"(property\s+)(registration|dispute|ownership|deed|title)",
            r"(land\s+)(registration|dispute|ownership|deed|title|grab)",
            r"(encroachment|trespassing|illegal\s+possession)\s+(on\s+)?(my\s+)?(property|land)",
            r"\b(property\s+law|property\s+dispute|land\s+dispute)\b",
        ],
        "responses": [
            "Property law in India is governed by the Transfer of Property Act, 1882 and the Registration Act, 1908. All property transactions above ₹100 must be registered with the Sub-Registrar.",
            "To transfer property: execute a sale deed, pay stamp duty (varies by state, typically 5-7%), register it at the Sub-Registrar's office, and update mutation records with local authorities. Always verify the seller's title through an encumbrance certificate."
        ]
    },

    "motor_vehicle_act": {
        "patterns": [
            r"(what'?s?|explain|tell me about)\s+(the\s+)?motor\s+vehicle(s)?\s+act",
            r"(traffic|driving)\s+(fine|penalty|challan|violation|offence|rule)",
            r"(drunk\s+driving|drunken\s+driving|drink\s+and\s+drive)\s+(law|penalty|fine|punishment)",
            r"(driving\s+without|no)\s+(licence|license|insurance)",
            r"(hit\s+and\s+run|rash\s+driving|over\s*speeding)",
            r"\b(motor\s+vehicle\s+act|traffic\s+law|traffic\s+challan)\b",
        ],
        "responses": [
            "The Motor Vehicles (Amendment) Act, 2019 introduced heavy penalties: drunk driving (₹10,000), driving without licence (₹5,000), over-speeding (₹1,000-2,000), and hit-and-run compensation up to ₹2 lakh.",
            "Key traffic penalties: no seatbelt (₹1,000), no helmet (₹1,000), using phone while driving (₹5,000), juvenile driving — guardian/owner fined ₹25,000 with 3 years imprisonment and vehicle registration cancellation."
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

}

FALLBACK_RESPONSES = [
    "I don't have information on that specific topic yet. Try asking about: FIR, bail, IPC, RTI, cyber crime, divorce, consumer rights, or Fundamental Rights.",
    "That's outside my current knowledge. I can help with courts, FIR filing, bail, constitutional rights, property law, cheque bounce, and more."
]