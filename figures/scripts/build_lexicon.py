# Basic lexicon builder (manual dataset)

lexicon = {
    "syr": "cold",
    "ʃlut": "lukewarm",
    "ʃund": "warm",
    "mats": "hot",
    "ɣamats": "very hot",
    "peʃt": "boil",
    "padze": "cook",
    "pisak": "cook (variant)",
    "vitk": "become (state change)"
}

for k, v in lexicon.items():
    print(k, "→", v)
