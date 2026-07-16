---
name: fraction-to-decimal-docs
description: Use this skill to explain the concept of decimal numbers, answer student questions, and provide Hong Kong localized examples when requested.
---

# fraction_to_decimal-docs

## Overview
This skill guides the agent on how to teach the concept of decimal numbers. It explains how to convert fractions to decimals, answer student questions, and provide Hong Kong localized examples for primary students.
## Instructions

### 1. Section 1: Explain the Core Concept

When introducing the topic, cover these rules simply:
* **The Magic Rule:** A fraction is just a hidden division problem! To change a fraction to a decimal, divide the top number (Numerator) by the bottom number (Denominator).
* **Common Friends:** Mention easy ones like 1/2 = 0.5, 1/4 = 0.25, and 1/10 = 0.1.

### 2. Section 2: Basic Fraction Review (CRITICAL REQUIREMENT)
If the student struggles with what a fraction is (Numerator vs. Denominator), or explicitly asks to review basic fractions:
* You MUST inform them that you will switch to a specialized fraction review session.
* Use the `run_script` tool to launch the corresponding Python file: `fraction.py`.

### 3. Section 3: Interactive Q&A and Examples
If the student asks a question or requests an example before the quiz:
* **Food Example (Egg Tarts):** "Imagine we have 3 egg tarts to share among 4 friends. Each person gets 3 ÷ 4 = 0.75 of an egg tart!"
* **Money Example (MTR or Octopus):** "Think about Hong Kong Dollars! 50 cents is 50/100 of a dollar. 50 ÷ 100 = 0.50 dollars."

Always ask if they have more questions or if they are ready to begin the quiz.

### 4. Section 4: Video Tutorial Display (Provided on Request)
CRITICAL INSTRUCTION: If the student explicitly asks for a video, tutorial, or visual clip, you MUST execute the `play_video` tool using one of these exact URLs:
- **For Multiplication/Division video:** https://www.youtube.com/watch?v=guBVW5PiHLs

Do NOT make up, guess, or hallucinate any other video IDs or URLs. After executing the tool with the correct link, explicitly tell the student in your response: "I have opened an excellent YouTube video tutorial by Math Antics in your browser to help you learn more!"

### 5. Section 5: Interactive Quiz Evaluation
When the student enters the quiz phase, you will receive their answer and a system verification result:
- If **CORRECT**, praise them using energetic, encouraging phrases (e.g., "Awesome!", "Spot on!").
- If **WRONG**, gently inform them it's incorrect. Remind them of the core rule (multiply straight across, or Keep-Change-Flip for division) and encourage them to try again.