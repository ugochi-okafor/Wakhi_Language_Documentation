# Ensures consistency across dataset naming

import os
import re

pattern = r"^\d{6}_S\d+[ab]?_A\d+_.*\.wav$"

def validate(filename):
    return bool(re.match(pattern, filename))

folder = "../audio/parts"

for f in os.listdir(folder):
    if f.endswith(".wav"):
        print(f, validate(f))
