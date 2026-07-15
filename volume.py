from pathlib import Path
from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from langgraph.checkpoint.memory import MemorySaver
import webbrowser
import random
import math

from main import run_script

def play_video(url: str) -> str:
    """Opens the student's default web browser to play a tutorial video.
    
    Args:
        url: The exact YouTube or video URL to open.
    """
    if not url.startswith("http"):
        return "Error: Invalid URL format."
    
    try:       
        webbrowser.open(url)
        return f"Success: Opened the web browser and started playing the video at {url}."
    except Exception as e:
        return f"Error: Failed to open the browser. Reason: {str(e)}"

url = "https://www.youtube.com/watch?v=qJwecTgce6c"

def shape() -> str:
    """
    Randomly selects a 3D shape for a volume problem.
    """
    shapes = [
        "rectangular_prism", "cylinder", "parallelogram_prism", 
        "trapezoidal_prism", "triangular_prism", "triangular_pyramid", "sphere"
    ]

    # shape = random.choice(shapes)
    shape = "rectangular_prism"  # For testing purposes, you can set a specific shape here.
    return shape

def volume(shape: str):
    """
    Generates parameters for a 3D volume problem.
    Dynamically imports 2D shape functions ONLY when needed.
    """
    height_3d = random.randint(3, 20)
    params = {}

    if shape == "cylinder":
        from area_perimeter_circle import circle
        radius, _ = circle()
        params = {
                    "radius": radius, "height_3d": height_3d
                }
    
    elif shape == "sphere":
        from area_perimeter_circle import circle
        radius, _ = circle()
        params = {
                    "radius": radius
                }

    elif shape == "parallelogram_prism":
        from area_perimeter_parallelogram import parallelogram
        base, height_2d, slant_side, _ = parallelogram()
        params = {
                    "base": base, "height_2d": height_2d, 
                    "slant_side": slant_side, "height_3d": height_3d
                }

    elif shape == "rectangular_prism":
        from area_perimeter_rectangle import rectangle_square
        length, width, _ = rectangle_square()
        params = {
                    "length": length, "width": width, 
                    "height_3d": height_3d
                }
    
    elif shape == "trapezoidal_prism":
        from area_perimeter_trapezoid import trapezoid
        base1, base2, height_2d, side1, side2, trap_type, _ = trapezoid()
        params = {
                    "base1": base1, "base2": base2, 
                    "height_2d": height_2d, "side1": side1, 
                    "side2": side2, "height_3d": height_3d, 
                    "type": trap_type
                }
    
    elif shape in ["triangular_prism", "triangular_pyramid"]:
        from area_perimeter_triangle import triangle
        base, height_2d, hypotenuse, is_right, _ = triangle()
        params = {
                    "base": base, "height_2d": height_2d, 
                    "hypotenuse": hypotenuse, "is_right": is_right, 
                    "height_3d": height_3d
                }
        
    return params


def get_input(message: str) -> str:
    """Handles getting textual or numerical input from the student via the terminal."""
    return input(message)

def volume_answer(shape: str, params: dict, student_result: float):
    """Checks if the student's input matches the mathematically correct answer."""
    base_area = 0
    correct_vol = 0

    if shape == "cylinder":
        from area_perimeter_circle import circle_answer
        base_area = circle_answer(params["radius"], "area", 0)[0]
        correct_vol = base_area * params["height_3d"]

    elif shape == "sphere":
        correct_vol = (4 / 3) * math.pi * (params["radius"] ** 3)

    elif shape == "parallelogram_prism":
        from area_perimeter_parallelogram import parallelogram_answer
        base_area = parallelogram_answer(params["base"], params["height_2d"], params["slant_side"], "area", 0)[0]
        correct_vol = base_area * params["height_3d"]

    elif shape == "rectangular_prism":
        from area_perimeter_rectangle import rectangle_square_answer
        base_area = rectangle_square_answer(params["length"], params["width"], "area", 0)[0]
        correct_vol = base_area * params["height_3d"]

    is_correct = math.isclose(correct_vol, student_result, abs_tol=0.1)
    return is_correct


def question(shape: str, params: dict) -> str:
    """Helper to format the math problem string dynamically."""
    if shape == "rectangular_prism":
        return f"A rectangular prism has a base of {params['length']}cm by {params['width']}cm, and a height of {params['height_3d']}cm."
    
    elif shape == "cylinder":
        return f"A cylinder has a base radius of {params['radius']}cm and a height of {params['height_3d']}cm."
    
    elif shape == "sphere":
        return f"A sphere has a radius of {params['radius']}cm."

    elif shape == "parallelogram_prism":
        return f"A parallelogram prism has a base length of {params['base']}cm and base height of {params['height_2d']}cm, with a 3D height of {params['height_3d']}cm."
    
    elif shape == "trapezoidal_prism":
        return f"A {params['type']} trapezoidal prism has bases of {params['base1']}cm and {params['base2']}cm, a 2D height of {params['height_2d']}cm, and a 3D height of {params['height_3d']}cm."
    
    elif shape == "triangular_prism":
        type_str = "right-angled" if params['is_right'] else "non-right-angled"
        return f"A {type_str} triangular prism has a base length of {params['base']}cm, a 2D height of {params['height_2d']}cm, and a 3D height of {params['height_3d']}cm."
    
    elif shape == "triangular_pyramid":
        return f"A triangular pyramid has a triangle base (length {params['base']}cm, 2D height {params['height_2d']}cm) and a 3D height of {params['height_3d']}cm."
    
    
    return ""


checkpointer = MemorySaver()
root_dir = "."
backend = FilesystemBackend(root_dir=root_dir, virtual_mode=True)

agent = create_deep_agent(
    model="ollama:gemma4:cloud",  
    backend=backend,
    tools=[play_video,run_script],
    skills=[str(Path(root_dir) / "skills")],
    interrupt_on={
        "write_file": True,
        "read_file": False,
        "edit_file": True,
    },
    checkpointer=checkpointer,
)


message = (
    f"1. Please introduce the concept of Volume following the volume-docs skill. \n"
    f"2. End your message by asking the student if they have any questions, if they need an example, or if they are ready to start.\n"
    f"3. CRITICAL REQUIREMENT: Keep your entire response extremely concise, direct, and under 120 words to save tokens."
)

print("\n Starting the Volume Tutor...")

result = agent.invoke(
    {"messages": [{"role": "user", "content": message}]},
    config={
        "configurable": {"thread_id": "volume_session_001"},
        "recursion_limit": 15
    },
)

print("\n=== Math Tutor Output ===")
print(result["messages"][-1].content)

while True:
    student_q = get_input("\nAsk a question, request a 2D area review (e.g., 'review circle'), or type 'ready' to start:")

    if student_q.lower().strip() in ["yes","no question", "ready", "start", "none","nope","no questions","i'm ready","quiz","let's start"]:
        print("\nGreat! Let's move on to the quiz phase.")
        break

    else:
        q_prompt = f"The student asks: '{student_q}'. Answer their question based on volume-docs. If they need to review a 2D shape, USE the run_script tool to launch the correct .py file. Ask if they are ready for the quiz."

        result = agent.invoke(
            {"messages": [{"role": "user", "content": q_prompt}]},
            config={
                "configurable": {"thread_id": "volume_session_001"},
                "recursion_limit": 15
            },
        )

        print("\n=== Tutor Response ===")
        print(result["messages"][-1].content)

shape_choice = shape()
params = volume(shape_choice)


print("\n--------------------------------------------------")
print(f" Please answer this question:")
print(f" {question(shape_choice, params)}")
print(f" What is the Volume of this shape? (If decimals, round to 2 decimal places)")
print("--------------------------------------------------")

while True:
    
    try:
        ans_str = get_input(f"\nPlease answer the Volume: ")
        ans_val = float(ans_str)
    except ValueError:
        print("Input error! Please ensure you enter a valid number.")
        continue

    is_correct = volume_answer(shape_choice, params, ans_val)

    feedback_prompt = f"""
    The quiz problem: {question(shape_choice, params)} Find the Volume.
    The student answered: {ans_val}
    System Verification Result: {"CORRECT" if is_correct else "WRONG"}.
    
    Please respond directly to the student:
    - If CORRECT: Congratulate them with Hong Kong style energy and confirm they solved it.
    - If WRONG: Gently tell them it's incorrect, guide them on the formula for {volume} and firmly state they must try again now.
    """

    result = agent.invoke(
        {"messages": [{"role": "user", "content": feedback_prompt}]},
        config={
            "configurable": {"thread_id": "quiz_session_001"},
            "recursion_limit": 15
        },
    )

    print("\n=== Tutor Feedback ===")
    print(result["messages"][-1].content)

    if is_correct:
        print("\nCongratulations! You solved it!")

        print("\n==================================================")
        print("What would you like to do next?")
        print("1. Keep practicing another question")
        print("2. Move to another topic ")
        print("==================================================")
        user_choice = get_input("Please enter option (1 or 2): ")

        if user_choice.strip() == "2":
            import os
            print("\nReturning to AI Math Tutor main menu...")

            if os.environ.get("LAUNCHED_FROM_MAIN") != "True":
                run_script("main.py")
            break
        else:
            print("\n==================================================")
            print(f" Fantastic! It automatically generates the next challenge for you.：")
            
            shape_choice = shape()
            params = volume(shape_choice)

            print(f" {question(shape_choice, params)}")
            print(f" What is the Volume of this shape? (If decimals, round to 2 decimal places)")

            print("==================================================")

    else:
        print("\nThe answer is not quite right. Don't give up, please recalculate the original problem and enter your answer again!")