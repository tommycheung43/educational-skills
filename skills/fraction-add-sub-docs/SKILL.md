---
name: fraction-add-sub-docs
description: Use this skill to explain adding and subtracting fractions with the same denominator, show Hong Kong examples, and trigger YouTube video tutorials.
---

# fraction-add-sub-docs

## Overview
This skill instructs the agent on how to explain fraction arithmetic for both same (like) and different (unlike) denominators, and provide responsive quiz evaluations.

## Instructions
### 1. Mandatory Response Structure
When a student asks about adding or subtracting fractions, you MUST organize your final response into the following distinct sections in order. Do not skip any section.

### 2. Section 1: Explain the Core Concept

#### A. Like Denominators (Same Bottom Number)
- **The Rule:** You ONLY add or subtract the top numbers (numerators).
- **The Trap:** You MUST keep the bottom number (denominator) exactly the same. Do not add or subtract them!
- **Example:** 5/16 + 2/16 = 7/16 or 5/9 - 2/9 = 3/9.

#### B. Unlike Denominators (Different Bottom Numbers)
- **The Rule:** You cannot add or subtract fractions directly if the bottom numbers are different. You must first change them so they have a **Common Denominator** (making them "like fractions").
- **The Strategy:** Find a common multiple for the denominators. Multiply the numerator and denominator of each fraction by the required factor to match that common multiple, then follow the standard rules.
- **Example:** To solve 1/2 + 1/4, change 1/2 into 2/4. Then add: 2/4 + 1/4 = 3/4.

### 3. Section 2: Hong Kong Localized Examples
Always frame hints and explanations within relatable Hong Kong situations:
- **Like Denominator Example:** Sharing a bamboo basket of Siu Mai at a dim sum restaurant.
- **Unlike Denominator Example:** Mixing 1/2 cup of evaporated milk with 1/3 cup of Ceylon black tea to create the ultimate Hong Kong Style Milk Tea.

### 4. Section 3: Video Tutorial Display
CRITICAL INSTRUCTION: You MUST actually EXECUTE the `play_video` tool to open the Math Antics video on Adding and Subtracting Fractions. Do NOT just output text pretending you did it.
After executing the tool, explicitly tell the student in your response: "I have opened an excellent YouTube video tutorial by Math Antics in your browser to help you learn more!"

### 5. Section 4: Interactive Problem Validation
- When given the generated problem details and the student's input answer:
  - Check mathematically if the student's answer is correct.
  - If **correct**, praise their effort and state that the answer is accurate.
  - If **incorrect**, explicitly state that it is wrong, provide a helpful step-by-step hint (reminding them about the denominator rules or finding a common multiple if unlike), and state that you are ready for another attempt.
