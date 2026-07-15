from pathlib import Path
from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from langgraph.checkpoint.memory import MemorySaver
import webbrowser
import random
import math


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

url = "https://www.youtube.com/watch?v=TWZoczeXzao"

def trapezoid():
    """Generates random base1, base2, height, calculated side lengths and operation for a trapezoid area or perimeter problem."""
    trapezoid_type = random.choice(["right_angle", "isosceles", "scalene"])
    operation = random.choice(["area", "perimeter"])

    base1 = random.randint(3, 20)
    height = random.randint(3, 20)

    if trapezoid_type == "right_angle":
        base2 = random.randint(base1 + 2, base1 + 20)
        side1 = height
        side2 = round(math.sqrt((base2 - base1)**2 + height**2))

    elif trapezoid_type == "isosceles":
        diff = random.randint(1, 10) * 2
        base2 = base1 + diff
        half_diff = diff / 2
        side1 = round(math.sqrt(half_diff**2 + height**2))
        side2 = side1

    else:
        diff = random.randint(4, 20)
        base2 = base1 + diff

        x1 = random.randint(1, diff - 1)
        while x1 == diff - x1 or x1 == 0 or (diff - x1) == 0:
            x1 = random.randint(1, diff - 1)
        x2 = diff - x1

        side1 = round(math.sqrt(x1**2 + height**2))
        side2 = round(math.sqrt(x2**2 + height**2))

    return base1, base2, height, side1, side2, trapezoid_type, operation

def get_input(message: str) -> str:
    """Handles getting textual or numerical input from the student via the terminal."""
    return input(message)

def trapezoid_answer(base1: int, base2: int, 
                     height: int, side1: int, 
                     side2: int, operation: str, 
                     student_result: float):
    """Checks if the student's input matches the mathematically correct answer."""
    if operation == "area":
        trapezoid_correct_result = (base1 + base2) * height / 2
    else:
        trapezoid_correct_result = base1 + base2 + side1 + side2

    if math.isclose(trapezoid_correct_result, student_result, abs_tol=0.1):
        is_correct = True
    else:
        is_correct = False

    return trapezoid_correct_result, is_correct

if __name__ == "__main__":
    checkpointer = MemorySaver()
    root_dir = "."
    backend = FilesystemBackend(root_dir=root_dir, virtual_mode=True)

    agent = create_deep_agent(
        model="ollama:gemma4:cloud",  
        backend=backend,
        tools=[play_video],
        skills=[str(Path(root_dir) / "skills")],
        interrupt_on={
            "write_file": True,
            "read_file": False,
            "edit_file": True,
        },
        checkpointer=checkpointer,
    )


    message = (
        f"1. Please introduce the rules for calculating the area and perimeter of trapezoids. \n"
        f"2. End your message by asking the student if they have any questions or if they need an example before starting the quiz.\n"
        f"3. CRITICAL REQUIREMENT: Keep your entire response extremely concise, direct, and under 120 words to save tokens."
    )

    print("\n Starting the Trapezoid Area & Perimeter Tutor...")

    result = agent.invoke(
        {"messages": [{"role": "user", "content": message}]},
        config={
            "configurable": {"thread_id": "trapezoid_session_001"},
            "recursion_limit": 15
        },
    )

    print("\n=== Math Tutor Output ===")
    print(result["messages"][-1].content)

    while True:
        student_q = get_input("\nAsk a question, or type 'ready' to start the quiz: ")

        if student_q.lower().strip() in ["yes","no question", "ready", "start", "none","nope","no questions","i'm ready","quiz","let's start"]:
            print("\nGreat! Let's move on to the quiz phase.")
            break

        else:
            q_prompt = f"The student asks: '{student_q}'. Please answer their question, provide examples if asked, and ask if they are ready for the quiz."

            result = agent.invoke(
                {"messages": [{"role": "user", "content": q_prompt}]},
                config={
                    "configurable": {"thread_id": "trapezoid_session_001"},
                    "recursion_limit": 15
                },
            )

            print("\n=== Tutor Response ===")
            print(result["messages"][-1].content)


    base1, base2, height, side1, side2,trapezoid_type, operation = trapezoid()
    if operation == "area":
        operation_display = "Area"
    else:
        operation_display = "Perimeter"

    print("\n--------------------------------------------------")
    print(f" Please answer this question:")
    print(f" A {trapezoid_type} trapezoid has bases of {base1}cm and {base2}cm, a height of {height}cm, and sides of {side1}cm and {side2}cm.")
    print(f" What is the {operation_display} of this shape?")
    print("--------------------------------------------------")

    while True:
        
        try:
            ans_str = get_input(f"\nPlease answer the {operation_display}: ")
            ans_val = float(ans_str)
        except ValueError:
            print("Input error! Please ensure you enter a valid number.")
            continue

        trapezoid_correct_result, is_correct = trapezoid_answer(base1, base2, height, side1, side2, operation, ans_val)

        feedback_prompt = f"""
        The quiz problem: A trapezoid with bases={base1} and {base2}, height={height}, sides={side1} and {side2}. Find the {operation_display}.
        The student answered: {ans_val}
        System Verification Result: {"CORRECT" if is_correct else "WRONG"}.
        
        Please respond directly to the student:
        - If CORRECT: Congratulate them with Hong Kong style energy and confirm they solved it.
        - If WRONG: Gently tell them it's incorrect, guide them on the formula for {operation} and firmly state they must try again now.
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
                from main import run_script
                import os
                print("\nReturning to AI Math Tutor main menu...")
                if os.environ.get("LAUNCHED_FROM_MAIN") != "True":
                    run_script("main.py")
                break
            else:
                print("\n==================================================")
                print(f" Fantastic! It automatically generates the next challenge for you.：")
                
                base1, base2, height, side1, side2,trapezoid_type, operation = trapezoid()
                if operation == "area":
                    operation_display = "Area"
                else:
                    operation_display = "Perimeter"

                print(f" What: A {trapezoid_type} trapezoid with bases={base1} and {base2}, height={height}, sides={side1} and {side2}. Find the {operation_display}.")
                print("==================================================")

        else:
            print("\nThe answer is not quite right. Don't give up, please recalculate the original problem and enter your answer again!")