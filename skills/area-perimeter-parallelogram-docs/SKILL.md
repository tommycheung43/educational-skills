---
name: area-perimeter-parallelogram-docs
description: Use this skill to explain area and perimeter of parallelograms, answer student questions, and provide Hong Kong localized examples when requested.
---

# area-perimeter-parallelogram-docs

## Overview
This skill guides the agent on how to teach the concepts of area and perimeter for parallelograms. It emphasizes a conversational approach where the agent introduces concepts briefly and then lets the student guide the learning through questions.

## Instructions

### 1. Section 1: Explain the Core Concept

When first introducing the topic, cover these two rules simply:
* **Base (b):** Any of the parallel horizontal top or bottom sides of the shape.
* **Slant Side (s):** The diagonal side connecting the top base line to the bottom base line.
* **Height (h):** The straight, perpendicular distance drawn at a 90-degree angle between the top and bottom base lines. It is never equal to the slant side unless the shape is a rectangle.
* **Area Rule:** The flat space inside a parallelogram. You find it by multiplying the base by the straight vertical height. 
  * **Formula:** Area = Base * Height
* **Perimeter Rule:** The total path around the outside edge. You find it by adding the two bases and the two slant sides together.
  * **Formula:** Perimeter = 2 * (Base + Slant Side)

### 2. Section 2: Interactive Q&A and Examples
If the student asks a question or requests an example before the quiz:
* **Area Example (Geometric Floor Tile):** Consider a decorative diamond-style marble floor tile manufactured as a precise parallelogram. If the horizontal base edge of the tile is 30 cm and its vertical perpendicular height is 20 cm, the flat surface Area is 30 * 20 = 600 square centimeters.
* **Perimeter Example (Angled Parking Space):** Consider an angled street parking slot painted on a roadway. The painted boundary lines form a geometrically perfect parallelogram. If the front entrance width base line is 3 meters and the painted diagonal slant line is 6 meters, the total Perimeter surrounding the boundaries of the parking space is 2 * (3 + 6) = 18 meters.

Always ask if they have more questions or if they are ready to begin the quiz.

### 3. Section 3: Video Tutorial Display (Provided on Request)
CRITICAL INSTRUCTION: If the student explicitly asks for a video, tutorial, or visual clip, you MUST execute the `play_video` tool using one of these exact URLs:
- **For Multiplication/Division video:** https://www.youtube.com/watch?v=ZcbK_ZLPHi0

Do NOT make up, guess, or hallucinate any other video IDs or URLs. After executing the tool with the correct link, explicitly tell the student in your response: "I have opened an excellent YouTube video tutorial by Math Antics in your browser to help you learn more!"

### 4. Section 4: Interactive Quiz Evaluation
When the student enters the quiz phase, you will receive their answer and a system verification result:
- If **CORRECT**, praise them using energetic, encouraging phrases (e.g., "Awesome!", "Spot on!").
- If **WRONG**, gently inform them it's incorrect. Remind them of the core rule (multiply straight across, or Keep-Change-Flip for division) and encourage them to try again.