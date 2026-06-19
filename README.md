# Wakhi Temperature Fieldwork: Audio Annotation and Linguistic Dataset Portfolio

## Overview

This repository documents my work on a field linguistics project focused on temperature expressions in Wakhi, an Eastern Pamir language spoken across the Wakhan region of Pakistan, Afghanistan, Tajikistan, and China.

The project was completed as part of the Field Linguistics course at Stockholm University and involved collecting, organising, annotating, transcribing, and analysing multilingual speech data from recorded consultant sessions.

The dataset demonstrates a complete audio annotation workflow including:

- audio recording organisation
- speech segmentation
- Praat TextGrid annotation
- transcription
- phonetic analysis
- interlinear glossing
- metadata creation
- semantic domain analysis
- lexicon development


## Project Focus

The research examined how temperature concepts are expressed in Wakhi and how these expressions are distributed across different semantic domains.

**Research questions:**

1. Which basic temperature concepts are distinguished in Wakhi?

2. How are temperature expressions used across different domains including:

- environment
- seasons
- food and liquids
- body sensations
- behaviour
- emotion
- colour


## Dataset Background

- **Language:** Wakhi
- **Language family:** Indo-European, Pamir branch
- **Consultant:** Sajid Ali Alvi
- **Profile:** First-language Wakhi speaker from Pakistan who also speaks Urdu, Pashto, and English.
- **Recording context:** Field methods sessions at Stockholm University, Språkstudion, Room E363.

- **Recording sessions:**

- Session 3: 11 February 2026
- Session 4: 18 February 2026
- Session 5: 25 February 2026
- Session 6: 4 March 2026


## Audio Dataset Structure

### Full Recordings

The `audio/full_recordings/` folder contains original uncut recordings.

These files represent complete consultant sessions and should be opened in Praat as Long Sound objects for analysis.

**Naming format:**
260211_S3a.wav


**Meaning:**

- 260211 = recording date
- S3 = Session 3
- a = first recording from that session


## Segmented Audio Parts

The `audio/parts/` folder contains shorter annotated recordings divided into thematic sections.

**Example:**
260211_S3a_A6_Making_Tea.wav

**Meaning:**
- 260211 = date
- S3 = session number
- a = recording identifier
- A6 = annotation part number
- Making_Tea = topic


## Annotation Workflow

Audio files were segmented and annotated using Praat.

Each TextGrid contains four main tiers:

### Part

Identifies the general conversation section.

### Speaker

Identifies the current speaker.

### Content

Contains the transcription or spoken content.

### Comments

Contains additional notes, uncertainty markers, or contextual information.


## Annotation Conventions

**Symbols used:**

- ```text
- //  broad transcription

- []  narrow transcription

- ''  loose translation

- ""  quotation or non-Wakhi terms

- |   Praat boundary marker

**Examples:**
| When we meet each other, we say |
/ʧɪsxəli/
'how are you'
which means "how are you"

metadata/
Audio recording information and dataset organisation.

audio/
Original and segmented recordings.

annotations/
Praat TextGrid files and annotation documentation.

transcripts/
Different levels of transcription and translation.

lexicon/
Temperature vocabulary and semantic mapping.

docs/
Research documentation and portfolio report.

scripts/
Helper scripts for dataset organisation and validation.


---

# 4. Create `.gitignore`

Create:
.gitignore


Paste:

```gitignore
# Python files
__pycache__/
*.py[cod]

# Virtual environments
venv/
env/

# Operating system files
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.log

# Praat temporary files
*.bak

# IDE files
.vscode/
.idea/

# Large audio exports
*.mp3
*.m4a
