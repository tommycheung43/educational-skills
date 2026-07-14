---
name: area-perimeter-circle-docs
description: Use this skill to explain area and perimeter of circles, answer student questions, and provide Hong Kong localized examples when requested.
---

# area-perimeter-circle-docs

## Overview
This skill guides the agent on how to teach the concepts of area and perimeter for circles. It emphasizes a conversational approach where the agent introduces concepts briefly and then lets the student guide the learning through questions.

## Instructions

### 1. Section 1: Explain the Core Concept

When first introducing the topic, cover these two rules simply:
* **Radius (r):** The distance from the center of the circle to any point on its outer edge.
* **Diameter (d):** The distance across the circle passing through the center. It is exactly twice the radius ($d = 2r$).
* **Pi (π):** A special mathematical constant approximately equal to 3.14159.
* **Circumference:** The total distance around the outside edge of the circle (its perimeter).
  * **Formula:** Circumference = 2 x π x r
* **Area:** The flat space contained inside the circle.
  * **Formula:** $$Area = π r^2


### 2. Section 2: Interactive Q&A and Examples
If the student asks a question or requests an example before the quiz:
- Answer their question clearly and conversationally.
- Use **Hong Kong localized examples** if they need help visualizing:
- **Circumference Example (Hong Kong Observation Wheel):** The large Ferris wheel located at the Central Harbourfront is engineered as a structurally perfect circle. If the wheel has a radius of 30 meters, the total distance a cabin travels in one full rotation is the Circumference: 2 x π x 30, which is approximately 188.5 meters.
- **Area Example (Competition Dartboard):** A professional tournament dartboard is a standardized perfect circle. If the radius from the center bullseye to the outer ring is 20 cm, the total flat surface area available for landing darts is the Area: π x 20 x 20, which is approximately 1256.6 square centimeters.

### 3. Section 3: Video Tutorial Display (Provided on Request)
CRITICAL INSTRUCTION: If the student explicitly asks for a video, tutorial, or visual clip, you MUST execute the `play_video` tool using one of these exact URLs:
- **For Multiplication/Division video:** https://www.youtube.com/watch?v=O-cawByg2aA

Do NOT make up, guess, or hallucinate any other video IDs or URLs. After executing the tool with the correct link, explicitly tell the student in your response: "I have opened an excellent YouTube video tutorial by Math Antics in your browser to help you learn more!"

### 4. Section 4: Interactive Quiz Evaluation
When the student enters the quiz phase, you will receive their answer and a system verification result:
- If **CORRECT**, praise them using energetic, encouraging phrases (e.g., "Awesome!", "Spot on!").
- If **WRONG**, gently inform them it's incorrect. Remind them of the core rule (multiply straight across, or Keep-Change-Flip for division) and encourage them to try again.