---
name: fraction-add-sub-docs
description: Use this skill to explain adding and subtracting fractions with the same denominator, show Hong Kong examples, and trigger YouTube video tutorials.
---

# fraction-add-sub-docs

## Overview
This skill guides the agent on how to teach fraction addition and subtraction (like fractions) using Math Antics principles and local Hong Kong examples.

## Instructions
### 1. Mandatory Response Structure
When a student asks about adding or subtracting fractions, you MUST organize your final response into the following distinct sections in order. Do not skip any section.

### 2. Section 1: Explain the Core Concept
Explain the golden rule of adding and subtracting "like fractions" (fractions with the same bottom number/denominator):
- **The Rule:** You ONLY add or subtract the top numbers (numerators).
- **The Trap:** You MUST keep the bottom number (denominator) exactly the same. Do not add or subtract the bottom numbers!
- **Video Example:** Just like in the video, `5/16 + 2/16 = 7/16`, and `5/9 - 2/9 = 3/9`.

### 3. Section 2: Hong Kong Localized Examples
Use these pre-defined everyday Hong Kong contexts:
- **Dim Sum Addition (Siu Mai):** If you eat `2/8` of a bamboo basket of Siu Mai, and your friend eats `3/8` of the basket, together you have eaten `(2+3)/8 = 5/8` of the basket.
- **MTR Journey Subtraction:** If a journey takes `7/10` of an hour, and you have already traveled `4/10` of an hour, you have `(7-4)/10 = 3/10` of an hour left on the train.

### 4. Section 3: Video Tutorial Display
CRITICAL INSTRUCTION: You MUST actually EXECUTE the `open_youtube_video` tool to open the Math Antics video on Adding and Subtracting Fractions. Do NOT just output text pretending you did it.
After executing the tool, explicitly tell the student in your response: "I have opened an excellent YouTube video tutorial by Math Antics in your browser to help you learn more!"
