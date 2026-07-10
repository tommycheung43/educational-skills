---
name: ratio-proportion-docs
description: Use this skill for requests related to ratio-proportion in order to fetch relevant documentation to provide accurate, up-to-date guidance.
---

# ratio-proportion-docs

## Overview

This skill explains how to access ratio-proportion-related documentation to help answer questions and guide implementation.

## Instructions
### 1. Mandatory Response Structure
When a student asks about ratio, you MUST organize your final response into the following three distinct sections in order. Do not skip any section even if you use the calculation tool:

### 2. Section 1: Explain the Core Concept Clearly

Pre-defined Explanation of Ratio and Proportion

First, explain the core mathematical concepts clearly:
- **What is a Ratio?** A ratio is a way to compare two or more quantities to show how much of one thing there is compared to another. It is written with a colon, like `A:B` (read as "A to B"), or as a fraction `A/B`.

- **What is a Proportion?** A proportion states that two ratios are equal. For example, if `1:3` is equal to `2:6`, that is a proportion. It means the relative sizes haven't changed, just the total amounts.

### 3. Section 2: Use Hong Kong Localized Examples

Second, use this pre-defined everyday Hong Kong English context to illustrate the concept:

- **The HK Milk Tea Golden Ratio:** To make an authentic Hong Kong-style milk tea (絲襪奶茶), the classic ratio of Evaporated Milk to Black Tea is `1:3`. This means for every 1 cup of milk, you need 3 cups of tea.

- **Pocket Money Sharing:** If two siblings share a sum of money in the ratio of `2:3`, the older sibling gets 2 parts and the younger sibling gets 3 parts out of the total 5 parts.

### 4. Section 3:Visual Explanation - Generate Ratio JPG
You MUST call the `generate_ratio_chart` tool with the two student-provided quantities as arguments to create the educational visual file. Inform the student in the text response that you have successfully generated and saved the visual helper as `ratio_visual.jpg` in their workspace.

### 5. Section 4: Interactive Practice & Feedback

Provide exactly one simple, localized practice question based on the student's level. Wait for their response. Praise their effort, and if they make a mistake, break down the calculation step-by-step rather than just giving the answer.

### 6. Section 5: Fetch background definition from Wikipedia

Use the fetch_url tool to read the following URL:
https://www.bbc.co.uk/bitesize/articles/zwxt2v4#zdg8kty


### 7. Section 6: Proportion Scaling Calculation
When a student asks to calculate a ratio from two numbers, invoke the `ratio` tool with two quantities as arguments. Explain the tool's calculation back to the student in a step-by-step manner.

