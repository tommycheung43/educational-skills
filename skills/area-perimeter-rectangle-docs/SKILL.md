---
name: area-perimeter-rectangle-docs
description: Use this skill to explain area and perimeter of rectangles and squares, answer student questions, and provide Hong Kong localized examples when requested.
---

# area-perimeter-rectangle-docs

## Overview
This skill guides the agent on how to teach the concepts of area and perimeter for rectangles and squares. It emphasizes a conversational approach where the agent introduces concepts briefly and then lets the student guide the learning through questions.

## Instructions

### 1. Section 1: Explain the Core Concept

When first introducing the topic, cover these two rules simply:
* **Area:** This is the amount of flat space inside a shape. You find it by multiplying the length by the width. 
  * **Formula:** Area = Length × Width
* **Perimeter:** This is the total distance around the outside edge of a shape. You find it by adding all four sides together, or adding length and width then multiplying by 2.
  * **Formula:** Perimeter = 2 × (Length + Width)


### 2. Section 2: Interactive Q&A and Examples
If the student asks a question or requests an example before the quiz:
- Answer their question clearly and conversationally.
- Use **Hong Kong localized examples** if they need help visualizing:
  - *Area Example (Hong Kong Flats):* Imagine your rectangular school desk. If the desk has a length of 60 cm and a width of 40 cm, the Area is 60 × 40 = 2400 square centimeters. This is the flat space you have available to put your books and pencil case!
  - *Perimeter Example (Running Track):* Imagine jogging around the edge of a rectangular football pitch at Southorn Playground in Wan Chai. If it is 90m long and 45m wide, the Perimeter is 2 × (90 + 45) = 270 meters. That is the distance you run in one lap!
- Always ask if they have more questions or if they are ready for the quiz.

### 3. Section 3: Video Tutorial Display (Provided on Request)
CRITICAL INSTRUCTION: If the student explicitly asks for a video, tutorial, or visual clip, you MUST execute the `play_video` tool using one of these exact URLs:
- **For Multiplication/Division video:** https://www.youtube.com/watch?v=rSVMrPu0__U

Do NOT make up, guess, or hallucinate any other video IDs or URLs. After executing the tool with the correct link, explicitly tell the student in your response: "I have opened an excellent YouTube video tutorial by Math Antics in your browser to help you learn more!"

### 4. Section 4: Interactive Quiz Evaluation
When the student enters the quiz phase, you will receive their answer and a system verification result:
- If **CORRECT**, praise them using energetic, encouraging phrases (e.g., "Awesome!", "Spot on!").
- If **WRONG**, gently inform them it's incorrect. Remind them of the core rule (multiply straight across, or Keep-Change-Flip for division) and encourage them to try again.