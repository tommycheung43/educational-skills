---
name: speed-docs
description: Use this skill to explain the concept of Speed, Distance, and Time, answer student questions, and provide Hong Kong localized examples when requested.
---

# speed-docs

## Overview
This skill guides the agent on teaching the foundational concept of relationship between Speed, Distance, and Time. It helps students understand the formula and how to apply it in everyday Hong Kong scenarios.

## Instructions

### 1. Section 1: Explain the Core Concept

When introducing the topic, cover these rules simply:
* **The Magic Triangle (DST):** Introduce the Distance-Speed-Time triangle. Distance is at the top, Speed and Time are at the bottom.
* **Finding Speed:** Speed = Distance ÷ Time. (e.g., How fast is the MTR moving?)
* **Finding Distance:** Distance = Speed × Time. (e.g., How far can a minibus travel?)
* **Finding Time:** Time = Distance ÷ Speed. (e.g., How long does it take to walk to school?)
* **Units:** Remind them to pay attention to units (e.g., km/h, m/s).


### 2. Section 2: Basic Math Review (CRITICAL REQUIREMENT)
If the student struggles with arithmetic operations, or explicitly asks to review 
* You MUST inform them that you will temporarily switch to a specialized review session to build their foundation.
* Use the `run_script` tool to launch the appropriate Python script based on their request.
* If you are unsure which specific script to run, use the `run_script` tool to launch `main.py` so the student can see the full menu of available topics.
**IMPORTANT:** After the `run_script` tool finishes executing, warmly welcome the student BACK to the Speed & Distance session and ask if they are ready to try the quiz!


### 3. Section 3: Interactive Q&A and Examples
If the student asks a question or requests an example before the quiz:
* **Red Minibus (Hong Kong Context):** "Imagine you are taking a Red Minibus from Mong Kok to Tai Po. The distance is about 24 kilometers. The minibus travels at a speed of 48 km/h. How long will it take?
  * Formula: Time = Distance ÷ Speed
  * Calculation: 24 ÷ 48 = 0.5 hours.
  * Conclusion: It takes half an hour (30 minutes) to reach Tai Po!"

Always ask if they have more questions or if they are ready to begin the quiz.

### 4. Section 4: Video Tutorial Display (Provided on Request)
CRITICAL INSTRUCTION: If the student explicitly asks for a video, tutorial, or visual clip, you MUST execute the `play_video` tool using one of these exact URLs:

- **For Negative Numbers Basics:** https://www.youtube.com/watch?v=7fz-4BUDyqg

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