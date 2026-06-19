# Annotation Conventions

## Overview

This document describes the annotation conventions used for the Wakhi temperature fieldwork dataset.

Annotations were created using Praat TextGrid files with time-aligned tiers.

The main purpose of annotation was to create structured speech data containing:

- speaker information
- segmented audio units
- spoken content
- linguistic notes
- translation information


# File Naming Convention

Audio filenames follow this structure:
YYMMDD_SessionRecording_PartNumber_Topic.wav


Example:
260211_S3a_A6_Making_Tea.wav



Meaning:

- 260211 = date in YYMMDD format
- S3 = Session 3
- a = first recording from that session
- A6 = Part 6
- Making_Tea = topic


# Recording Structure

## Full recordings

Full recordings are uncut session files.

Example:
260211_S3a.wav


These files should be opened in Praat as Long Sound objects.


## Parts

Parts contain shorter thematic sections.

Example:
260211_S3a_A1_Weather_Change.wav


Each part contains its corresponding annotation file.


# TextGrid Tier Structure

Each TextGrid contains four main tiers.


## Part Tier

Purpose:

Identifies the general section or topic.

Example:
A6 - Making Tea

## Speaker Tier

Purpose:

Identifies who is speaking.

Examples:
S
Consultant:
Sajid

## Content Tier

Purpose:

Contains spoken content and transcription.


## Comments Tier

Purpose:

Contains additional notes, uncertainty, or contextual information.


# Transcription Symbols

| Symbol | Meaning |
|---|---|
| // | broad transcription |
| [] | narrow transcription |
| '' | loose translation |
| "" | quotation or non-Wakhi terms |
| | | Praat boundary marker |


Example:
| When we meet each other, we say |
/ʧɪsxəli/
'how are you'
which means "how are you"

# Annotation Guidelines

## General Rules

- All Wakhi content produced by Sajid was annotated.
- Irrelevant sections were removed or marked.
- Experimenter speech could be annotated less extensively.
- Unknown forms were not assigned unsupported meanings.
- Cultural explanations were retained when they contributed meaning.


# Quality Principles

Annotations prioritised:

- accuracy
- consistency
- transparency
- clear separation between observation and interpretation


# Limitations

Some transcription examples remain preliminary because the dataset was collected in a fieldwork setting with limited recording conditions.

Further validation with additional speakers would be required for broader linguistic conclusions.
