# Annotation Notes

## Overview

This folder contains time-aligned speech annotations created using Praat TextGrid files.

The annotations represent segmented Wakhi speech data collected during field linguistics sessions at Stockholm University.

Each TextGrid links:

- recorded audio segments
- speaker identification
- transcription content
- contextual notes


## Annotation Software

Tool used:

Praat

Purpose:

- audio segmentation
- speech alignment
- transcription organisation
- annotation review


## TextGrid Structure

Each annotation file contains four main tiers:

1. Part
2. Speaker
3. Content
4. Comments


# Tier Descriptions


## Part Tier

The Part tier identifies the topic or section of the recording.

Examples:
Metadata
or:
A6 – Describe the process of making tea.
or:
A1 – How does the weather change in the Wakhan region?

The Part tier allows researchers to connect each audio segment to the elicitation task.


---

## Speaker Tier

The Speaker tier identifies the person speaking.

Examples:
S
= Sajid Ali Alvi, language consultant

H
= Henrik, researcher/session participant


Some segments contain multiple speakers:
S/H
when overlap or interaction occurs.


---

## Content Tier

The Content tier contains the spoken material.

Examples include:
you put the pot on the fire and warm it up
from:
260211_S3a_A6_Making_Tea.TextGridWakhan also called Pamir
for hiking it is a good place
from:
260211_S3a_A1_Weather_Change.TextGrid

The content tier may include:

- transcription
- translations
- elicitation prompts
- spoken explanations


---

## Comments Tier

The Comments tier stores additional information.

Examples:
the word for 'month' is from Urdu
or:
:) 
or notes about uncertainty.

Comments are kept separate from transcription to maintain annotation clarity.


# Example Annotation Structure

A TextGrid follows this structure:
File type = "ooTextFile"

Object class = "TextGrid"

Tier 1:
Part

Tier 2:
Speaker

Tier 3:
Content

Tier 4:
Comments


# Annotation Conventions


## Broad Transcription

Symbol:
//
Used for broad transcription.


Example:
/ʧɪsxəli/

## Narrow Transcription

Symbol:
[]
Used when more detailed phonetic information is required.


## Translation

Single quotation marks:
'translation'
Used for loose translations.


Example:
'how are you'

## Quotation / Non-Wakhi Terms

Double quotation marks:
""
Used for quoted expressions or non-Wakhi terms.


Example:
"salam alaykum"

## Praat Boundaries

Symbol:
|
Used to mark segmentation boundaries inside annotation examples.


Example:
| When we meet each other, we say |

# Annotation Guidelines Applied


## Consultant Speech

All Wakhi speech produced by Sajid Ali Alvi was annotated.

This includes:

- lexical information
- translations
- semantic explanations
- relevant cultural context


## Researcher Speech

Researcher questions and explanations were annotated more selectively.

Only information useful for understanding the interaction was included.


## Unclear Material

When speech could not be confidently interpreted:

- it was left blank
- marked as uncertain
- or noted in comments


## Irrelevant Audio

Sections not contributing to the research objective were:

- removed
- left unmarked
- or marked with:
--

# Quality Control Approach

Annotation decisions were based on:

- repeated listening
- comparison with consultant explanations
- separation between transcription and interpretation
- maintaining consistent tier usage


# Current TextGrid Examples Included

The repository contains examples from:


## A1 - Weather Change

File:
260211_S3a_A1_Weather_Change.TextGrid
Focus:

Weather descriptions and seasonal temperature expressions.


## A6 - Making Tea

File:
260211_S3a_A6_Making_Tea.TextGrid
Focus:

Procedural speech describing tea preparation.

This file was used for interlinear glossing and lexical analysis.


## A7 - Water Too Hot

File:
260211_S3a_A7_Water_Too_Hot.TextGrid
Focus:

Physical temperature effects and body sensation.


## A8 - Water Got Cold

File:
260211_S3a_A8_Water_Got_Cold.TextGrid
Focus:

Change of state from hot to cold.


## A9 - Coldest Day Ever

File:
260211_S3a_A9_Coldest_Day_Ever.TextGrid
Focus:

Extreme cold experience.


## A10 - Hottest Day Ever

File:
260211_S3a_A10_Hottest_Day_Ever.TextGrid
Focus:

Extreme heat experience.


# Notes on Dataset Use

The TextGrid files demonstrate practical experience with:

- speech segmentation
- linguistic annotation
- multilingual audio processing
- structured speech dataset preparation

They are intended as portfolio examples showing the workflow from raw recording to annotated linguistic data.
