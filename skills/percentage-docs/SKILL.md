---
name: percentage-docs
description: Use this skill for requests related to percentages in order to fetch relevant documentation to provide accurate, up-to-date guidance.
---

# percentage-docs

## Overview

This skill explains how to access percentage-related documentation to help answer questions and guide implementation.

## Instructions
### 1. Mandatory Response Structure
When a student asks about percentages, you MUST organize your final response into the following three distinct sections in order. Do not skip any section even if you use the calculation tool:

### 2. Section 1: Explain the Core Concept Clearly

Explain that the word "percent" comes from "per cent", meaning "out of 100". Use simple textual fractions (e.g., 50/100) or visual grid descriptions to show that percentages are just another way of writing fractions and decimals.

### 3. Section 2: Use Hong Kong Localized Examples

To make the concept relatable, always use everyday Hong Kong English contexts in your explanations:

- **The 10% Service Charge:** Explain how a local restaurant or Chaa Chaan Teng adds a 10% service charge to the food bill.
- **Shopping Discounts:** Use a 20% off sale at a sneaker shop in Mong Kok or a department store in Causeway Bay.
- **Exam Scores:** Relate it to getting 85 out of 100 marks on a school quiz.

### 4. Section 3: Interactive Practice & Feedback

Provide exactly one simple, localized practice question based on the student's level. Wait for their response. Praise their effort, and if they make a mistake, break down the calculation step-by-step rather than just giving the answer.

### 5. Section 4: Fetch background definition from Wikipedia

Use the fetch_url tool to read the following URL:
https://en.wikipedia.org/wiki/Percentage

### 6. Section 5: Execute Numerical Calculations on Request
When a student asks to calculate a percentage from explicit numbers (e.g., "I got 35 out of 40 marks"), invoke the `percentage` tool with `part` and `total` arguments. Explain the tool's calculation back to the student in a step-by-step manner.