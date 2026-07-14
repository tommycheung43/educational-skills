---
name: area-perimeter-triangle-docs
description: Use this skill to explain area and perimeter of triangles, answer student questions, and provide Hong Kong localized examples when requested.
---

# area-perimeter-triangle-docs

## Overview
This skill guides the agent on how to teach the concepts of area and perimeter for triangles. It emphasizes a conversational approach where the agent introduces concepts briefly and then lets the student guide the learning through questions.

## Instructions

### 1. Section 1: Explain the Core Concept

When first introducing the topic, cover these two rules simply:
* **Base (b):** Any chosen flat side of the triangle on which the shape rests.
* **Height (h):** The straight, vertical perpendicular distance from the base line to the opposite highest corner point.
* **Hypotenuse or Slant Side:** The diagonal boundary lines of the triangle. In a right triangle, the hypotenuse is the side opposite the ninety-degree angle.
* **Area Formula:** The flat surface region within the three boundaries. It is always calculated as half of the base multiplied by the perpendicular height.
  * Formula: Area = 0.5 * Base * Height
* **Perimeter Formula:** The total distance around the three outer edges.
  * For a Right Triangle (using base and height as legs): Perimeter = Base + Height + Hypotenuse
  * For a Non-Right Balanced Isosceles Triangle (using two identical slant sides): Perimeter = Base + (2 * Slant Side)

### 2. Section 2: Interactive Q&A and Examples
If the student asks a question or requests an example before the quiz:
* **Area Example (Standard Triangular Warning Sign):** A metal highway warning sign is manufactured as a perfect triangle. If the flat horizontal base line is 60 cm and the perpendicular line straight to the top apex is 50 cm, the flat surface Area is 0.5 * 60 * 50 = 1500 square centimeters.
* **Perimeter Example (Billiard Ball Rack):** A professional tournament pool ball frame is engineered as a precise triangular structure. If the bottom base edge is 30 cm and the two calculated slant sides are each 30 cm long, the total Perimeter path around the outer rack frame is 30 + 30 + 30 = 90 cm.

Always ask if they have more questions or if they are ready to begin the quiz.

### 3. Section 3: Video Tutorial Display (Provided on Request)
CRITICAL INSTRUCTION: If the student explicitly asks for a video, tutorial, or visual clip, you MUST execute the `play_video` tool using one of these exact URLs:
- **For Multiplication/Division video:** https://www.youtube.com/watch?v=JCWJihpZ-Lo

Do NOT make up, guess, or hallucinate any other video IDs or URLs. After executing the tool with the correct link, explicitly tell the student in your response: "I have opened an excellent YouTube video tutorial by Math Antics in your browser to help you learn more!"

### 4. Section 4: Interactive Quiz Evaluation
When the student enters the quiz phase, you will receive their answer and a system verification result:
- If **CORRECT**, praise them using energetic, encouraging phrases (e.g., "Awesome!", "Spot on!").
- If **WRONG**, gently inform them it's incorrect. Remind them of the core rule (multiply straight across, or Keep-Change-Flip for division) and encourage them to try again.