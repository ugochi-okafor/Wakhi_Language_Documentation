# Wakhi Temperature Fieldwork: Audio Annotation and Linguistic Dataset Portfolio

## Overview

This repository documents my work on a field linguistics project focused on temperature expressions in Wakhi, an Eastern Pamir language spoken across the Wakhan region of Pakistan, Afghanistan, Tajikistan, and China.

The project was completed as part of the Field Linguistics course at Stockholm University and involved collecting, organising, annotating, transcribing, and analysing multilingual speech data from recorded consultant sessions. 

## Important Note on Audio Data

No raw audio recordings are included in this repository.

**This is intentional due to:**
- Privacy considerations for the consultant
- Ethical handling of field data
- Focus on transcription, annotation, and analysis workflows rather than raw recordings

However, the full dataset is represented through:

- Time-aligned Praat TextGrid files  
- Transcripts (orthographic, phonetic, glossed, and translated)  
- Structured metadata files  
- Lexical and semantic analysis outputs  

This ensures the full linguistic workflow remains reproducible without exposing sensitive audio material.

---

## Research Focus

The project investigates:

1. How temperature is expressed in Wakhi through lexical and grammatical means  
2. How these expressions behave across semantic domains such as:
   - Environment  
   - Food and liquids  
   - Body sensation  
   - Behaviour  
   - Colour  

The analysis focuses on:

- Scalar temperature systems  
- Degree marking  
- Change-of-state expressions  
- Domain restriction vs metaphorical extension  

---

## Key Findings

- A clear temperature scale exists from extreme cold to extreme heat  
- Temperature expressions are strongly domain-specific  
- Food and environmental contexts show the richest usage  
- Body sensation is expressed indirectly through effects (e.g. burning)  
- No systematic metaphorical extension into behaviour or colour domains  
- Intensity is expressed through dedicated lexical markers rather than metaphor  

Temperature in Wakhi functions primarily as a physical descriptive system rather than a metaphorical one.

---

## Repository Structure
```text
wakhi_language _documentation/
├── README.md
├── LICENSE
├── .gitignore
│
├── metadata/
│   ├── sessions.csv
│   ├── speakers.csv
│   ├── file_index.csv
│   └── annotation_conventions.md
│
├── annotations/
│   ├── textgrids/
│   ├── praat_scripts/
│   └── annotation_notes.md
│
├── transcripts/
│   ├── orthographic/
│   ├── phonetic/
│   ├── glossed/
│   └── translations/
│
├── lexicon/
│   ├── wakhi_temperature_lexicon.csv
│   ├── domain_mapping.csv
│   └── analysis_notes.md
│
├── docs/
│   ├── methodology.md
│   ├── portfolio_report.pdf
│   ├── examples.md
│   └── limitations.md
│
├── figures/
└── scripts/
    ├── segment_audio.py
    ├── validate_filenames.py
    ├── export_metadata.py
    └── build_lexicon.py
```

### Transcripts

Instead of audio files, the dataset includes full linguistic representations:

- Orthographic transcripts  
- IPA-based phonetic approximations  
- Interlinear glossed texts  
- English translations  

All files are aligned with structured annotation tiers.

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
---

## Data Description

### Audio Data

The dataset includes:

- Full session recordings (~30 minutes each)
- Segmented clips aligned with elicitation tasks
- Controlled narrative and procedural speech data

### Full Recordings

The `audio/full_recordings/` folder contains original uncut recordings.

These files represent complete consultant sessions and should be opened in Praat as Long Sound objects for analysis.

### File Naming Convention
**Naming format:** 260211_S3a.wav

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

---

## Annotation System

All annotations are created using Praat TextGrid format with four tiers:

- **Part** → discourse segment or elicitation task  
- **Speaker** → speaker identifier  
- **Content** → transcription of speech  
- **Comments** → analytical notes  

### Transcription Conventions

- `//` broad transcription  
- `[]` narrow transcription (IPA)  
- `''` translation  
- `""` non-Wakhi terms  
- `|` alignment boundary  

---

## Methodology

### 1. Elicitation Design

Data was collected using structured prompts targeting:

- Seasonal and environmental temperature
- Bodily sensation and perception
- Food and liquid temperature (tea-making)
- Extreme temperature memory recall
- Metaphorical extension testing

---

### 2. Recording and Segmentation

- Recordings made in controlled field sessions  
- Segmentation completed in Praat  
- Each file aligned with elicitation tasks  

---

### 3. Annotation Workflow

- Orthographic transcription first  
- IPA transcription for phonetic approximation  
- Interlinear glossing following Leipzig Glossing Rules  
- Lexical normalisation after repeated verification  

---

## Lexical Summary

### Cold Domain

- `/syr/` → cold  
- `/syr-i/` → it is cold  
- `/syr vitk/` → become cold  
- `/ik rɑŋʃu/` → extremely cold  

---

### Mid Range

- `/ʃlut/` → lukewarm  

---

### Warm to Hot Domain

- `/ʃund/` → warm  
- `/garm/` → hot  
- `/mats/` → very hot  
- `/ɣaˈmats/` → extremely hot  
- `/ˈtɑːodi mɑts/` → too hot to drink  

---

### Degree Marking

- `/ɣaftʃ/` → intensifier (very, strongly)  

---

## Semantic Domain Results

### Environment

Temperature terms are heavily used for:

- Seasonal change  
- Weather description  
- Landscape conditions  

---

### Food and Liquids

Highly structured temperature descriptions occur in:

- Tea preparation  
- Boiling processes  
- Consumption thresholds  

---

### Body Sensation

Temperature is expressed indirectly through effects:

- Burning sensations  
- Physical discomfort  

---

### Behaviour and Emotion

No temperature metaphors observed.

Alternative lexical items include:

- `/baghet/` → unfriendly person  
- `/karha/` → anger or conflict  

---

### Colour

No temperature-based colour metaphors exist.

- `/sik/` → red  
- `/osˈmoni sabs/` → blue/sky green expression  
- Intensity marked by `/ɣaftʃ/`

---

## Tools Used

- Praat (TextGrid annotation)
- Manual transcription and verification
- CSV-based lexicon construction
- Python scripts for validation and structure checks
- Markdown documentation system

---

## Limitations
- No raw audio included  
- Single consultant dataset  
- Limited dialect variation  
- Some phonetic uncertainty in early transcription stages  
- Verb distinctions require further verification   

---

## Outputs Included

- Fully segmented audio corpus  
- Annotated TextGrid files  
- Interlinear glossed texts  
- Structured lexicon dataset  
- Semantic analysis report  

---

## Purpose

This repository demonstrates:

- Field linguistics data collection  
- Audio segmentation and annotation  
- Multilingual transcription and glossing  
- Semantic domain analysis  
- Structured linguistic documentation workflow  

---

## Final Note

This project is based on controlled elicitation sessions and is intended to demonstrate analytical and annotation skills in field linguistics. It represents a focused semantic analysis of temperature in Wakhi rather than a complete language description.
