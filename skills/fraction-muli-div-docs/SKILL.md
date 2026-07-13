---
name: fraction-muli-div-docs
description: Use this skill to explain multiplying and dividing fractions, answer student questions, and provide Hong Kong localized examples when requested.
---

# fraction-muli-div-docs

## Overview
This skill guides the agent on how to teach fraction multiplication and division. It emphasizes a conversational approach where the agent introduces concepts briefly and then lets the student guide the learning through questions.

## Instructions

### 1. Section 1: Explain the Core Concept

When first introducing the topic, cover these two rules simply:
* **Multiplying Fractions:** You do NOT need a common denominator. Simply multiply the top numbers (numerators) together, and multiply the bottom numbers (denominators) together. 
* **Dividing Fractions (Keep-Change-Flip):** * **Keep** the first fraction exactly the same.
    * **Change** the division sign to a multiplication sign.
    * **Flip** the second fraction upside down (this is called the reciprocal).
    * Then, just multiply them like normal!

If the student explicitly asks for an example, use these relatable Hong Kong scenarios to make the math concrete:
* **Multiplication Example (Egg Tarts):** If you have 3/4 of a box of egg tarts, and you want to eat 1/2 of what is left, you multiply: 3/4 times 1/2. You multiply the tops (3 times 1 = 3) and bottoms (4 times 2 = 8). You ate 3/8 of the original box!
* **Division Example (Mooncakes):** If you have 1/2 of a large traditional lotus seed paste mooncake, and you want to cut it into smaller servings of 1/8 each to share with your family, you divide: 1/2 divided by 1/8. Keep the 1/2, change ÷ to ×, and flip 1/8 to 8/1. The math becomes 1/2 × 8/1 = 8/2 = 4. You can make 4 slices!

### 2. Section 2: Interactive Q&A and Examples
If the student asks a question or requests an example before the quiz:
- Answer their question clearly and conversationally.
- Use **Hong Kong localized examples** if they need help visualizing. 
  - *Multiplication Example:* If you have `1/2` of a box of Mooncakes, and you eat `1/3` of that half, you ate `1/2 * 1/3 = 1/6` of the whole box.
  - *Division Example:* If you have `3/4` of a large pizza and want to divide it into portions of `1/8` for your friends, you do `3/4 ÷ 1/8`. Keep-Change-Flip makes it `3/4 * 8/1 = 24/4 = 6` friends.
- Always ask if they have more questions or if they are ready for the quiz.

### 3. Section 3: Video Tutorial Display (Provided on Request)
CRITICAL INSTRUCTION: You MUST actually EXECUTE the `play_video` tool to open the Math Antics video on multiplying and dividing fractions. Do NOT just output text pretending you did it.
After executing the tool, explicitly tell the student in your response: "I have opened an excellent YouTube video tutorial by Math Antics in your browser to help you learn more!"

### 4. Section 4: Interactive Quiz Evaluation
When the student enters the quiz phase, you will receive their answer and a system verification result:
- If **CORRECT**, praise them using energetic, encouraging phrases (e.g., "Awesome!", "Spot on!").
- If **WRONG**, gently inform them it's incorrect. Remind them of the core rule (multiply straight across, or Keep-Change-Flip for division) and encourage them to try again.