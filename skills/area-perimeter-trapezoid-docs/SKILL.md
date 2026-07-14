---
name: area-perimeter-trapezoid-docs
description: Use this skill to explain area and perimeter of trapezoid, answer student questions, and provide Hong Kong localized examples when requested.
---

# area-perimeter-trapezoid-docs

## Overview
This skill guides the agent on how to teach the concepts of area and perimeter for trapezoids. It emphasizes a conversational approach where the agent introduces concepts briefly and then lets the student guide the learning through questions.

## Instructions

### 1. Section 1: Explain the Core Concept

When first introducing the topic, cover these two rules simply:
* **Bases (base1 and base2):** The two parallel sides of the trapezoid (usually the top and bottom sides).
* **Height (h):** The perpendicular vertical distance drawn directly at a 90-degree angle between the two parallel bases.
* **Slant Sides (side1 and side2):** The two non-parallel outer boundary lines connecting the parallel bases.
* **Trapezoid Types:**
  * **Right-Angled Trapezoid:** Features exactly one side that is perpendicular to both parallel bases (this side length equals the height).
  * **Isosceles Trapezoid:** The two non-parallel diagonal slant sides are perfectly equal in length.
  * **Scalene Trapezoid:** Neither right-angled nor isosceles; all non-parallel sides and angles are completely unequal.
* **Area Formula:** The total surface region enclosed inside the four borders. It equals half the sum of the parallel bases multiplied by the vertical height.
  * Formula: Area = 0.5 * (Base1 + Base2) * Height
* **Perimeter Formula:** The total outer path length around the four edges. You find it by adding all four bounding lines together.
  * Formula: Perimeter = Base1 + Base2 + Side1 + Side2

### 2. Section 2: Interactive Q&A and Examples
If the student asks a question or requests an example before the quiz:
* **Area Example (Office Window Panel):** A modern office building window is manufactured as a perfect trapezoid. If the top horizontal parallel edge is 100 cm, the bottom parallel edge is 120 cm, and the straight vertical height line between them is 80 cm, the flat surface Area is 0.5 * (100 + 120) * 80 = 8800 square centimeters.
* **Perimeter Example (Garden Flower Bed):** A decorative suburban flower bed is laid out as a precise isosceles trapezoid. The top edge is 5 meters, the bottom edge is 9 meters, and the two symmetrical slant sides are each 4 meters long. The total Perimeter path around the outer boundary is 5 + 9 + 4 + 4 = 22 meters.

Always ask if they have more questions or if they are ready to begin the quiz.

### 3. Section 3: Video Tutorial Display (Provided on Request)
CRITICAL INSTRUCTION: If the student explicitly asks for a video, tutorial, or visual clip, you MUST execute the `play_video` tool using one of these exact URLs:
- **For Multiplication/Division video:** https://www.youtube.com/watch?v=TWZoczeXzao

Do NOT make up, guess, or hallucinate any other video IDs or URLs. After executing the tool with the correct link, explicitly tell the student in your response: "I have opened an excellent YouTube video tutorial by Math Antics in your browser to help you learn more!"

### 4. Section 4: Interactive Quiz Evaluation
When the student enters the quiz phase, you will receive their answer and a system verification result:
- If **CORRECT**, praise them using energetic, encouraging phrases (e.g., "Awesome!", "Spot on!").
- If **WRONG**, gently inform them it's incorrect. Remind them of the core rule (multiply straight across, or Keep-Change-Flip for division) and encourage them to try again.