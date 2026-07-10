---
name: fraction-docs
description: Use this skill for requests related to fractions in order to fetch relevant documentation to provide accurate, up-to-date guidance.
---

# fraction-docs

## Overview

This skill explains how to access fraction-related documentation to help answer questions and guide implementation.

## Instructions
### 1. Mandatory Response Structure
When a student asks about fractions, you MUST organize your final response into the following three distinct sections in order. Do not skip any section even if you use the calculation tool:

### 2. Section 1: Explain the Core Concept Clearly

Pre-defined Explanation of Ratio and Proportion

First, explain the core mathematical concepts clearly:

- **What is a Fraction?** A fraction represents a part of a whole object or a whole group. It is written as one number over another, separated by a line.
- **Numerator:** The top number, which tells us how many parts we are choosing or looking at.
- **Denominator:** The bottom number, which tells us the total number of equal parts the whole is divided into.


### 3. Section 2: Use Hong Kong Localized Examples

Second, use this pre-defined everyday Hong Kong English context to illustrate the concept:

Always use everyday Hong Kong contexts to illustrate fractions:
- **The Hong Kong Egg Tart:** If you cut a freshly baked local egg tart into 4 equal slices and eat 1 slice, you have consumed `1/4` of the egg tart, and `3/4` is left for your friends.

- **Sharing a Pineapple Bun:** If you and your classmate split a golden pineapple bun perfectly in half, each person gets exactly `1/2` of the bun.

### 4. Section 3:Visual Explanation & Cake Image Display

CRITICAL INSTRUCTION FOR IMAGE DISPLAY:
You MUST actually EXECUTE the `view_image` tool with the argument `"cake.png"`. Do NOT just output text pretending you did it. 
After you have successfully executed the tool, explicitly tell the student in your text response: "I have popped up the cake.png image for you to see!"


### 5. Section 4: Interactive Practice & Feedback

Provide exactly one simple, localized practice question based on the student's level. Wait for their response. Praise their effort, and if they make a mistake, break down the calculation step-by-step rather than just giving the answer.

### 6. Section 5: Fetch background definition from Wikipedia

Use the fetch_url tool to read the following URL:
https://en.wikipedia.org/wiki/Fraction


### 7. Section 6: Proportion Scaling Calculation
When a student asks to calculate a fraction from two numbers, invoke the `fraction` tool with two quantities as arguments. Explain the tool's calculation back to the student in a step-by-step manner.

