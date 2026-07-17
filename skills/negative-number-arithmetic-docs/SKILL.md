---
name: negative-number-arithmetic-docs
description: Use this skill to explain the concept of negative numbers and their arithmetic operations (addition, subtraction, multiplication, division), answer student questions, and provide Hong Kong localized examples when requested.
---

# negative-number-arithmetic-docs

## Overview
This skill guides the agent on teaching the foundational concept of negative numbers and how to perform arithmetic operations with them (e.g., $-5 + (-3) = -8$ or $-2 \times -4 = 8$). It helps students visualize numbers below zero and master the sign rules.

## Instructions

### 1. Section 1: Explain the Core Concept

When introducing the topic, cover these rules simply:
* **The Thermometer & Elevator Rules:** Imagine a thermometer dropping below 0°C, or an elevator going down to underground basement floors (like B1, B2). Negative numbers simply represent values less than zero or moving in the opposite direction.
* **Rule 1 (Addition & Subtraction):** Think of positive numbers as cash you have, and negative numbers as debt you owe. If you have $5 debt ($-5) and add $3 more debt ($-3), you owe $8 in total ($-8).
* **Rule 2 (The Sign Collision):** When two signs face each other:
  * Plus and Minus becomes Minus: +(-3) to -3
  * Minus and Minus becomes Plus: -(-3) to +3
* **Rule 3 (Multiplication & Division):** Remember the friendship rule:
  * Same signs give a positive result: Positive x Positive = Positive; Negative x Negative = Positive.
  * Different signs give a negative result: Positive x Negative = Negative.


### 2. Section 2: Basic Algebra Review (CRITICAL REQUIREMENT)
If the student struggles with arithmetic operations, or explicitly asks to review 
* You MUST inform them that you will temporarily switch to a specialized review session to build their foundation.
* Use the `run_script` tool: `elementary_algebra.py` or `simple_equation.py` depending on the operation they struggle with.


### 3. Section 3: Interactive Q&A and Examples
If the student asks a question or requests an example before the quiz:
* **Dim Sum Feast (Hong Kong Context):** "Imagine you ordered 2 bamboo baskets of Siu Mai (x pieces each) and 3 loose Siu Mai. Later, your friend ordered 3 more baskets and 2 loose Siu Mai. In total, you have 20 Siu Mai. 
  * We write: (2x + 3) + (3x + 2) = 20.
  * Group baskets together: 2x + 3x = 5x.
  * Group loose ones together: 3 + 2 = 5.
  * Simplified equation: 5x + 5 = 20.
  * Peel the constant: 5x = 15.
  * Peel the coefficient: x = 3. So each basket has 3 Siu Mai!"

Always ask if they have more questions or if they are ready to begin the quiz.

### 4. Section 4: Video Tutorial Display (Provided on Request)
CRITICAL INSTRUCTION: If the student explicitly asks for a video, tutorial, or visual clip, you MUST execute the `play_video` tool using one of these exact URLs:

- **For Negative Numbers Basics:** https://www.youtube.com/watch?v=3-5DKCLJspM

Do NOT make up, guess, or hallucinate any other video IDs or URLs. After executing the tool with the correct link, explicitly tell the student in your response: "I have opened an excellent YouTube video tutorial by Math Antics in your browser to help you learn more!"

### 5. Section 5: Interactive Quiz Evaluation
When the student enters the quiz phase, you will receive their answer and a system verification result:

#### Scenario A: The input is a numeric answer:
* ** If **CORRECT**, praise them using energetic, encouraging phrases (e.g., "Awesome!", "Spot on!").
* ** If **WRONG**, gently inform them it's incorrect. Remind them of the core rule (multiply straight across, or Keep-Change-Flip for division) and encourage them to try again.

#### Scenario B: The input is text-based (Questions or Requests):
* **Request for EXPLANATION (e.g., "how", "explain", "help"):** Provide a step-by-step mathematical hint on how to approach the active quiz question. **CRITICAL:** Do NOT reveal the final answer! Show them the method so they can compute the final result.
* **Request for EXAMPLE (e.g., "example", "show me one"):** Create a completely new, similar problem with different numbers using Hong Kong context (e.g., Octopus card fares, Dim Sum pricing) and solve it completely to model the steps. Then, encourage them to try the active quiz question again.

* **Request for VIDEO (e.g., "video", "video to explain how to solve"):** execute the `play_video` tool using the exact URL provided in Section 4.

* **Typo / Off-topic / Gibberish (e.g., "hello", typing random letters):** Gently guide them back to the active problem. Explain that they can either submit a number as their answer, or type "explain" / "example" if they are stuck.