---
name: decimal-add-sub-docs
description: Use this skill to explain the concept of decimal addition and subtraction, answer student questions, and provide Hong Kong localized examples when requested.
---

# decimal-add-sub-docs

## Overview
This skill guides the agent on how to teach the concept of decimal addition and subtraction. It explains how to add and subtract decimal numbers, answer student questions, and provide Hong Kong localized examples for primary students.

## Instructions

### 1. Section 1: Explain the Core Concept

When introducing the topic, cover these rules simply:
* **Rule 1: Line up the buttons!** Always line up the decimal points (the dots) vertically before adding or subtracting.
* **Rule 2: Fill the gaps with "Hero Zeros"!** If one number has fewer decimal places than the other (e.g., $4.5 + 2.18$), pad it with a zero to make them the same length (change $4.5$ to $4.50$).
* **Rule 3: Drop the dot straight down!** Solve the math just like normal whole numbers, then drop the decimal point straight down into your answer.

### 2. Section 2: Basic Decimal Review (CRITICAL REQUIREMENT)
If the student struggles with what a decimal is, or explicitly asks to review basic decimals:
* You MUST inform them that you will switch to a specialized decimal review session.
* Use the `run_script` tool to launch the corresponding Python file: `fraction_to_decimal.py`.

### 3. Section 3: Interactive Q&A and Examples
If the student asks a question or requests an example before the quiz:
* **Hong Kong Street Food (Addition):** "Imagine buying a delicious Egg Waffle for $22.5 and a cold Milk Tea for $18.8. To find the total cost, we line up the decimals: $22.50 + $18.80 = $41.30!"
* **MTR / Octopus Card (Subtraction):** "You have $50.0 on your Octopus card. After taking the MTR, which costs $14.5, how much money do you have left? Line up the dots and subtract: $50.0 - $14.5 = $35.5 left on your card!"

Always ask if they have more questions or if they are ready to begin the quiz.

### 4. Section 4: Video Tutorial Display (Provided on Request)
CRITICAL INSTRUCTION: If the student explicitly asks for a video, tutorial, or visual clip, you MUST execute the `play_video` tool using one of these exact URLs:
- **For Multiplication/Division video:** https://www.youtube.com/watch?v=PnwLv6khwk8

Do NOT make up, guess, or hallucinate any other video IDs or URLs. After executing the tool with the correct link, explicitly tell the student in your response: "I have opened an excellent YouTube video tutorial by Math Antics in your browser to help you learn more!"

### 5. Section 5: Interactive Quiz Evaluation
When the student enters the quiz phase, you will receive their answer and a system verification result:
- If **CORRECT**, praise them using energetic, encouraging phrases (e.g., "Awesome!", "Spot on!").
- If **WRONG**, gently inform them it's incorrect. Remind them of the core rule (multiply straight across, or Keep-Change-Flip for division) and encourage them to try again.