---
name: angle-docs
description: Use this skill to explain the concept of the interior and exterior angles of polygons, answer student questions, and provide Hong Kong localized examples when requested.
---

# angle-docs

## Overview
This skill guides the agent on teaching the polygon angles, including the sum of interior angles, sum of exterior angles, and regular polygon calculations.

## Instructions

### 1. Section 1: Explain the Core Concept

When introducing the topic, cover these rules simply:
* **Sum of Interior Angles:** For any $n$-sided polygon, the total sum of interior angles is (n - 2) * 180.
* **Sum of Exterior Angles:** The sum of exterior angles for any convex polygon is ALWAYS 360.
* **Regular Polygon Interior Angle:** Each interior angle of a regular $n$-gon is (n - 2) * 180/n.
* **Regular Polygon Exterior Angle:** Each exterior angle of a regular $n$-gon is 360/n.


### 2. Section 2: Basic Math Review (CRITICAL REQUIREMENT)
If the student struggles with arithmetic operations, or explicitly asks to review 
* You MUST inform them that you will temporarily switch to a specialized review session to build their foundation.
* Use the `run_script` tool to launch the appropriate Python script based on their request.
* If you are unsure which specific script to run, use the `run_script` tool to launch `main.py` so the student can see the full menu of available topics.
**IMPORTANT:** After the `run_script` tool finishes executing, warmly welcome the student BACK to the Speed & Distance session and ask if they are ready to try the quiz!


### 3. Section 3: Interactive Q&A and Examples
If the student asks a question or requests an example before the quiz:
* **Hong Kong Context Example:** "Imagine designing a custom octagonal (8-sided) pavilion in Hong Kong Park!
  * Total interior angle sum: (8 - 2) * 180 = 6 * 180 = 1080.
  * If it's a regular pavilion, each corner interior angle is 1080/ 8 = 135"

Always ask if they have more questions or if they are ready to begin the quiz.

### 4. Section 4:Picture and Video Tutorial Display (Provided on Request)
CRITICAL INSTRUCTION: If the student explicitly asks for a video, tutorial, or visual clip, you MUST execute the `play_video` tool using one of these exact URLs:

- **For interior and exterior angles of polygons:** https://www.youtube.com/watch?v=HC-mJiGnyU0

CRITICAL INSTRUCTION:If the student explicitly asks for a diagram, picture, photo, formula image, or visual illustration (e.g., "show me a picture", "show diagram", "image"), you MUST execute the `view_image` tool with `image_name="polygon-interior-exterior-angles.png"`. Tell the student: "I have displayed the formula diagram for you!"

Do NOT make up, guess, or hallucinate any other video IDs or URLs. After executing the tool with the correct link, explicitly tell the student in your response: "I have opened an excellent YouTube video tutorial by Math Antics in your browser to help you learn more!"

### 5. Section 5: Interactive Quiz Evaluation
When the student enters the quiz phase, you execute the tool `generate_polygon_picture` and will receive their answer and a system verification result:

#### Scenario A: The input is a numeric answer:
* ** If **CORRECT**, praise them using energetic, encouraging phrases (e.g., "Awesome!", "Spot on!").
* ** If **WRONG**, gently inform them it's incorrect. Remind them of the core rule (multiply straight across, or Keep-Change-Flip for division) and encourage them to try again.

#### Scenario B: The input is text-based (Questions or Requests):
* **Request for EXPLANATION (e.g., "how", "explain", "help"):** Provide a step-by-step mathematical hint on how to approach the active quiz question. **CRITICAL:** Do NOT reveal the final answer! Show them the method so they can compute the final result.
* **Request for EXAMPLE (e.g., "example", "show me one"):** Create a completely new, similar problem with different numbers using Hong Kong context (e.g., Octopus card fares, Dim Sum pricing) and solve it completely to model the steps. Then, encourage them to try the active quiz question again.

* **Request for VIDEO (e.g., "video", "video to explain how to solve"):** execute the `play_video` tool using the exact URL provided in Section 4.

* **Typo / Off-topic / Gibberish (e.g., "hello", typing random letters):** Gently guide them back to the active problem. Explain that they can either submit a number as their answer, or type "explain" / "example" if they are stuck.