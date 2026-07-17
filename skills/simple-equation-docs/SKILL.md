---
name: simple-equation-docs
description: Use this skill to explain the basic concepts of solving two-step simple equations, answer student questions, and provide Hong Kong localized examples when requested.
---

# simple-equations-docs

## Overview
This skill guides the agent on teaching two-step simple equations to primary/early secondary students. It builds on elementary algebra by introducing the concept of undoing operations in the reverse order of BEDMAS/BODMAS (undoing addition/subtraction first, then multiplication/division).

## Instructions

### 1. Section 1: Explain the Core Concept

When introducing the topic, cover these rules simply:
* **The Onion Strategy:** Solving a two-step equation is like peeling an onion. You have to remove the outside layers first before getting to the center (the variable).
* **Constant (常數 - The Outer Layer):** Explain that the **constant** is the standalone number that doesn't change (like the $+ 5$ in $3x + 5 = 20$). Because it is on the very outside of our variable, we must peel (undo) it first!
* **Coefficient (係數 - The Inner Layer):** Explain that the **coefficient** is the number multiplied by or divided by the variable (like the $3$ in $3x$). It is glued tightly to our "mystery box" (variable) and must be peeled (undo) last.
* **Step 1 (Undo Addition/Subtraction):** First, look for any numbers being added to or subtracted from the variable term. Use inverse operations to move them to the other side.
* **Step 2 (Undo Multiplication/Division):** Next, isolate the "mystery box" completely by undoing any multiplication or division attached to the variable.


### 2. Section 2: Basic Algebra Review (CRITICAL REQUIREMENT)
If the student struggles with arithmetic operations, or explicitly asks to review 
* You MUST inform them that you will temporarily switch to a specialized review session to build their foundation.
* Use the `run_script` tool: `elementary_algebra.py`,`fraction_add_sub.py` or `fraction_mult_div.py` depending on the operation they struggle with.


### 3. Section 3: Interactive Q&A and Examples
If the student asks a question or requests an example before the quiz:
* **Buying Bubble Tea (Multiplication & Addition):** "Imagine you bought 3 identical cups of bubble tea and a $5 plastic bag. The total is $65. Let a cup of bubble tea be y. We write: 3y + 5 = 65. First, take away the bag's cost: 65 - 5 = 60. Now we know 3 cups cost $60. Divide by 3: 60 / 3 = 20. Each cup is $20!"
* **Sharing Dim Sum (Division & Subtraction):** Provide a similar step-by-step example using division and subtraction in a Hong Kong context.

Always ask if they have more questions or if they are ready to begin the quiz.

### 4. Section 4: Video Tutorial Display (Provided on Request)
CRITICAL INSTRUCTION: If the student explicitly asks for a video, tutorial, or visual clip, you MUST execute the `play_video` tool using one of these exact URLs:

- **For 2-Steps Equations, concept:** https://www.youtube.com/watch?v=LDIiYKYvvdA&t=4s

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