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

url = "https://www.youtube.com/watch?v=JCWJihpZ-Lo"

def triangle():
    """Generates random base, height, hypotenuse, right-angle status and operation for a triangle area or perimeter problem."""
    is_right = random.choice([True, False])
    operation = random.choice(["area", "perimeter"])

    base = random.randint(3, 20)
    height = random.randint(3, 20)

    if is_right:
        hypotenuse = round(
                            math.sqrt(base**2 + height**2)
                    )
    else:
        hypotenuse = round(
                            math.sqrt((base / 2)**2 + height**2)
                    )

    return base, height, hypotenuse,is_right, operation

def get_input(message: str) -> str:
    """Handles getting textual or numerical input from the student via the terminal."""
    return input(message)

def check_answer(base: int, height: int, hypotenuse: int,is_right: bool, operation: str, student_result: float) -> bool:
    """Checks if the student's input matches the mathematically correct answer."""
    if operation == "area":
        correct_result = base * height * 0.5
    else:
        if is_right:
            correct_result = base + height + hypotenuse
        else:
            correct_result = base + 2 * hypotenuse

    return math.isclose(correct_result, student_result, rel_tol=1e-5)


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
    f"1. Please introduce the rules for calculating the area and perimeter of triangles. \n"
    f"2. End your message by asking the student if they have any questions or if they need an example before starting the quiz.\n"
    f"3. CRITICAL REQUIREMENT: Keep your entire response extremely concise, direct, and under 120 words to save tokens."
)

print("\n Starting the Triangle Area & Perimeter Tutor...")

result = agent.invoke(
    {"messages": [{"role": "user", "content": message}]},
    config={
        "configurable": {"thread_id": "triangle_session_001"},
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
                "configurable": {"thread_id": "triangle_session_001"},
                "recursion_limit": 15
            },
        )

        print("\n=== Tutor Response ===")
        print(result["messages"][-1].content)


base, height, hypotenuse,is_right, operation = triangle()
if operation == "area":
    operation_display = "Area"
else:
    operation_display = "Perimeter"

if is_right:
    triangle_type = "Right-Angled Triangle"
else:
    triangle_type = "Non-Right-Angled Triangle"

print("\n--------------------------------------------------")
print(f" Please answer this question:")
print(f" A {triangle_type} has a base of {base}cm, a height of {height}cm, and a hypotenuse of {hypotenuse}cm.")
print(f" What is the {operation_display} of this shape?")
print("--------------------------------------------------")

while True:
    
    try:
        ans_str = get_input(f"\nPlease answer the {operation_display}: ")
        ans_val = float(ans_str)
    except ValueError:
        print("Input error! Please ensure you enter a valid number.")
        continue

    is_correct = check_answer(base, height, hypotenuse,is_right, operation, ans_val)

    feedback_prompt = f"""
    The quiz problem: A triangle with base={base}, height={height}, hypotenuse={hypotenuse}. Find the {operation_display}.
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
            print("\nReturning to AI Math Tutor main menu...")
            break
        else:
            print("\n==================================================")
            print(f" Fantastic! It automatically generates the next challenge for you.：")
            
            base, height, hypotenuse, is_right, operation = triangle()
            if operation == "area":
                operation_display = "Area"
            else:
                operation_display = "Perimeter"

            if is_right:
                triangle_type = "Right-Angled Triangle"
            else:
                triangle_type = "Non-Right-Angled Triangle"

            print(f" What: A {triangle_type} with base={base}, height={height}, hypotenuse={hypotenuse}. Find the {operation_display}.")
            print("==================================================")

    else:
        print("\nThe answer is not quite right. Don't give up, please recalculate the original problem and enter your answer again!")