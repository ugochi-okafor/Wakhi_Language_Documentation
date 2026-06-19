# Simple segmentation helper for naming consistency

import os

def check_filename(name):
    """
    Validates naming convention:
    YYMMDD_SessionPart_Description.wav
    """
    parts = name.replace(".wav", "").split("_")
    
    if len(parts) < 3:
        return False
    
    date = parts[0]
    session = parts[1]
    
    return len(date) == 6 and session.startswith("S")

def main():
    folder = "../audio/full_recordings"
    
    for file in os.listdir(folder):
        if file.endswith(".wav"):
            valid = check_filename(file)
            print(file, "✔" if valid else "✘")

if __name__ == "__main__":
    main()
