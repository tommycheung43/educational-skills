---
name: elementary-algebra-docs
description: Use this skill to explain the basic concepts of elementary algebra, solve one-step equations, answer student questions, and provide Hong Kong localized examples when requested.
---

# elementary-algebra-docs

## Overview
This skill guides the agent on elementary algebra (solving one-step equations with variables) to primary students. It explains the concept of variables, balancing equations using inverse operations,and provide Hong Kong localized examples for primary students.

## Instructions

### 1. Section 1: Explain the Core Concept

When introducing the topic, cover these rules simply:
* **The Mystery Box (Variables):** Explain that letters like x or y are just "mystery boxes" hiding a secret number. Our job is to find out what number is inside!
* **The Balancing Scale (Equations):** An equation is like a weighing scale. The equal sign (=) means both sides weigh exactly the same. Whatever you do to one side, you MUST do to the other side!
* **Inverse Operations (Doing the Opposite):** To find the mystery number, we use the opposite magic:
  * If the equation has Addition (+), we Subtract (-).
  * If it has Subtraction (-), we Add (+).
  * If it has Multiplication (x), we Divide (/).
  * If it has Division (/), we Multiply (x).

### 2. Section 2: Basic Decimal Review (CRITICAL REQUIREMENT)
If the student struggles with arithmetic operations (adding, subtracting, multiplying, or dividing), or explicitly asks to review 
* You MUST inform them that you will temporarily switch to a specialized review session to build their foundation.
* For basic decimal representation review, use the `run_script` tool to launch: `fraction_to_decimal.py`.
* For adding and subtracting decimals review, use the `run_script` tool to launch: `decimal_add_sub.py`.
* For Multiplication and Division decimals review, use the `run_script` tool to launch: `decimal_mult_div.py`.
* For Multiplication and Division Fraction review, use the `run_script` tool to launch: `fraction_mult_div`.

### 3. Section 3: Interactive Q&A and Examples
If the student asks a question or requests an example before the quiz:
* **Octopus Card (Addition/Subtraction):** "Imagine you had some money $x$ in your Octopus card. You added $20, and now you have $50. We write: x + 20 = 50. To find x, we do the opposite: 50 - 20 = 30. So, x = 30!"
* **Buying Stationery (Multiplication/Division):** "You bought 4 identical pens, and the total cost is $48. Let the cost of one pen be y. We write: 4y = 48. To find y, we do the opposite: 48 / 4 = 12. So, each pen costs $12!"

Always ask if they have more questions or if they are ready to begin the quiz.

### 4. Section 4: Video Tutorial Display (Provided on Request)
CRITICAL INSTRUCTION: If the student explicitly asks for a video, tutorial, or visual clip, you MUST execute the `play_video` tool using one of these exact URLs:

- **For Basic algebra, equation concept:** https://www.youtube.com/watch?v=NybHckSEQBI
- **For Basic solving algebra, equation:** https://www.youtube.com/watch?v=LDIiYKYvvdA

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