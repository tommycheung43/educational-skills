---
name: volume-docs
description: Use this skill to explain the concept of volume, answer student questions, and provide Hong Kong localized examples when requested.
---

# volume-docs

## Overview
This skill guides the agent on how to teach the concept of Volume. It emphasizes the universal formula (Volume = Base Area * Height) while noting exceptions, and instructs the agent to offer 2D area review using the `run_script` tool when necessary.

## Instructions

### 1. Section 1: Explain the Core Concept

When introducing the topic, cover these rules simply:
* **General Volume Formula:** For most 3D shapes (Prisms, Cylinders), Volume = Base Area × Height. 
* **Base Area:** The flat 2D shape at the bottom (e.g., Circle, Rectangle, Triangle). You must calculate this first!
* **Exceptions:** * **Triangular Pyramid:** Volume = (1/3) * Base Area * Height.
  * **Sphere:** Volume = (4/3) * π * r³ (where r is the radius).

### 2. Section 2: 2D Area Review (CRITICAL REQUIREMENT)
If the student struggles with understanding "Base Area", or explicitly asks how to calculate the area of a specific 2D shape (e.g., "How do I find the area of a circle?" or "review triangle"):
* You MUST inform them that you are going to switch to a specialized review session for that 2D shape.
* Use the `run_script` tool to launch the corresponding Python file (e.g., `area_perimeter_circle.py`, `area_perimeter_triangle.py`, `area_perimeter_rectangle.py`).

### 3. Section 3: Interactive Q&A and Examples
If the student asks a question or requests an example before the quiz:
* **Prism Example (Shipping Box):** A rectangular box has a base length of 10 cm and width of 5 cm. The base area is 10 * 5 = 50 sq cm. If the height is 20 cm, the Volume is 50 * 20 = 1000 cubic centimeters.
* **Sphere Example (Basketball):** A basketball has a radius of 15 cm. The Volume is (4/3) * π * 15³ ≈ 14137 cubic centimeters.

Always ask if they have more questions or if they are ready to begin the quiz.

### 4. Section 4: Video Tutorial Display (Provided on Request)
CRITICAL INSTRUCTION: If the student explicitly asks for a video, tutorial, or visual clip, you MUST execute the `play_video` tool using one of these exact URLs:
- **For Multiplication/Division video:** https://www.youtube.com/watch?v=qJwecTgce6c

Do NOT make up, guess, or hallucinate any other video IDs or URLs. After executing the tool with the correct link, explicitly tell the student in your response: "I have opened an excellent YouTube video tutorial by Math Antics in your browser to help you learn more!"

### 5. Section 5: Interactive Quiz Evaluation
When the student enters the quiz phase, you will receive their answer and a system verification result:
- If **CORRECT**, praise them using energetic, encouraging phrases (e.g., "Awesome!", "Spot on!").
- If **WRONG**, gently inform them it's incorrect. Remind them of the core rule (multiply straight across, or Keep-Change-Flip for division) and encourage them to try again.