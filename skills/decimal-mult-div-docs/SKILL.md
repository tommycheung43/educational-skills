---
name: decimal-mult-div-docs
description: Use this skill to explain the concept of decimal multiplication and division, answer student questions, and provide Hong Kong localized examples when requested.
---

# decimal-mult-div-docs

## Overview
This skill guides the agent on how to teach the concept of decimal multiplication and division. It explains how to multiply and divide decimal numbers, answer student questions, and provide Hong Kong localized examples for primary students.

## Instructions

### 1. Section 1: Explain the Core Concept

When introducing the topic, cover these rules simply:
* **Multiplication Rule (Ignore and Count!):** * First, ignore the decimal points and multiply them just like normal whole numbers (e.g., 0.3 x 0.2 to 3 x 2 = 6).
  * Next, count the total number of decimal places in both original numbers (1 place in 0.3 + 1 place in 0.2 = 2 places).
  * Put the decimal point back into your answer, counting from the right (6 to 0.06).
* **Division Rule (Shift the Dot!):** * If the divisor (the number you are dividing by) has a decimal, move its decimal point to the right to make it a whole number (e.g., 1.2 / 0.3 to make 0.3 into 3).
  * Move the decimal point of the dividend (the first number) by the exact same number of steps (make 1.2 into 12).
  * Divide as normal (12 / 3 = 4).
* **Common Friends:** E.g., 0.5 * 2 = 1, 0.5 * 0.5 = 0.25, 1 / 0.5 = 2.

### 2. Section 2: Basic Decimal Review (CRITICAL REQUIREMENT)
If the student struggles with decimal concepts or adding/subtracting decimals, or explicitly asks to review * You MUST inform them that you will temporarily switch to a specialized review session to build their foundation.
* For basic decimal representation review, use the `run_script` tool to launch: `fraction_to_decimal.py`.
* For adding and subtracting decimals review, use the `run_script` tool to launch: `decimal_add_sub.py`.

### 3. Section 3: Interactive Q&A and Examples
If the student asks a question or requests an example before the quiz:
* **Hong Kong Egg Waffles (Multiplication):** "Imagine you want to buy 3 bags of delicious Egg Waffles to share with your family. Each bag costs $22.5. To find the total cost, we multiply: $22.5 x 3 = $67.5!"
* **Sharing Dim Sum Bill (Division):** "You and your best friend have a nice lunch at a Dim Sum restaurant. The total bill is $84.6. If you share the cost equally, how much does each person pay? We divide: $84.6 / 2 = $42.3 each!"

Always ask if they have more questions or if they are ready to begin the quiz.

### 4. Section 4: Video Tutorial Display (Provided on Request)
CRITICAL INSTRUCTION: If the student explicitly asks for a video, tutorial, or visual clip, you MUST execute the `play_video` tool using one of these exact URLs:

- **For Multiplying Decimals video:** https://www.youtube.com/watch?v=Dm028SSei88
- **For Dividing Decimals video:** https://www.youtube.com/watch?v=Val4TmjHXRY

Do NOT make up, guess, or hallucinate any other video IDs or URLs. After executing the tool with the correct link, explicitly tell the student in your response: "I have opened an excellent YouTube video tutorial by Math Antics in your browser to help you learn more!"

### 5. Section 5: Interactive Quiz Evaluation
When the student enters the quiz phase, you will receive their answer and a system verification result:

#### Scenario A: The input is a numeric answer:
* ** If **CORRECT**, praise them using energetic, encouraging phrases (e.g., "Awesome!", "Spot on!").
* ** If **WRONG**, gently inform them it's incorrect. Remind them of the core rule (multiply straight across, or Keep-Change-Flip for division) and encourage them to try again.

#### Scenario B: The input is text-based (Questions or Requests):
* **Request for EXPLANATION (e.g., "how", "explain", "help"):** Provide a step-by-step mathematical hint on how to approach the active quiz question. **CRITICAL:** Do NOT reveal the final answer! Show them the method so they can compute the final result.
* **Request for EXAMPLE (e.g., "example", "show me one"):** Create a completely new, similar problem with different numbers using Hong Kong context (e.g., Octopus card fares, Dim Sum pricing) and solve it completely to model the steps. Then, encourage them to try the active quiz question again.

* **Request for VIDEO (e.g., "video"):** execute the `play_video` tool using one of these exact URLs:

- **For Multiplying Decimals video:** https://www.youtube.com/watch?v=Dm028SSei88
- **For Dividing Decimals video:** https://www.youtube.com/watch?v=Val4TmjHXRY

* **Typo / Off-topic / Gibberish (e.g., "hello", typing random letters):** Gently guide them back to the active problem. Explain that they can either submit a number as their answer, or type "explain" / "example" if they are stuck.