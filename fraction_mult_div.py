from pathlib import Path
from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from langgraph.checkpoint.memory import MemorySaver
import webbrowser
import random
import math

import logger_utils
from logger_utils import setup_agent_logging, write_log

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

url = "https://www.youtube.com/watch?v=qeWRewXB91g&t=1s"

def fraction():
    """Generates random numerators, denominators, and an operation (multiply/divide) for a fraction problem."""
    operation = random.choice(["multiply", "divide"])

    den1 = random.randint(2, 10)
    den2 = random.randint(2, 10)

    num1 = random.randint(1, den1 - 1)
    num2 = random.randint(1, den2 - 1)

    return num1, den1, num2, den2, operation

# def get_input(message: str) -> str:
#     """Handles getting textual or numerical input from the student via the terminal."""
#     return input(message)

def check_answer(num1: int, den1: int, num2: int, den2: int, operation: str, student_num: int, student_den: int) -> bool:
    """Checks if the student's input fraction matches the mathematically correct answer."""
    if student_den == 0:
        return False
    
    if operation == "multiply":
        correct_val = (num1 / den1) * (num2 / den2)
    else:
        correct_val = (num1 / den1) / (num2 / den2)

    student_val = student_num / student_den
    
    return math.isclose(correct_val, student_val, rel_tol=1e-5)


checkpointer = MemorySaver()
root_dir = "."
backend = FilesystemBackend(root_dir=root_dir, virtual_mode=True)


agent = create_deep_agent(
    model="ollama:gemma4:cloud",  
    backend=backend,
    tools=[play_video,write_log],
    skills=[str(Path(root_dir) / "skills")],
    interrupt_on={
        "write_file": True,
        "read_file": False,
        "edit_file": True,
    },
    checkpointer=checkpointer,
)


message = (
    f"1. Please introduce the rules for multiplying and dividing fractions briefly. \n"
    f"2. End your message by asking the student if they have any questions or if they need an example before starting the quiz.\n"
    f"3. CRITICAL REQUIREMENT: Keep your entire response extremely concise, direct, and under 120 words to save tokens."
)

print("\n Starting the Fraction Multiplication & Division Tutor...")

result = agent.invoke(
    {"messages": [{"role": "user", "content": message}]},
    config={
        "configurable": {"thread_id": "mult_div_session_001"},
        "recursion_limit": 15
    },
)

print("\n=== Math Tutor Output ===")
print(result["messages"][-1].content)

while True:
    student_q = input("\nAsk a question, or type 'ready' to start the quiz: ")

    if student_q.lower().strip() in ["yes","no question", "ready", "start", "none","nope","no questions","i'm ready","quiz","let's start"]:
        print("\nGreat! Let's move on to the quiz phase.")
        break

    else:
        q_prompt = f"The student asks: '{student_q}'. Please answer their question, provide examples if asked, and ask if they are ready for the quiz."

        result = agent.invoke(
            {"messages": [{"role": "user", "content": q_prompt}]},
            config={
                "configurable": {"thread_id": "mult_div_session_001"},
                "recursion_limit": 15
            },
        )

        print("\n=== Tutor Response ===")
        print(result["messages"][-1].content)


num1, den1, num2, den2, operation = fraction()
if operation == "multiply":
    operation_symbol = "×"
else:
    operation_symbol = "÷"

print("\n--------------------------------------------------")
print(f"📝 Please answer this question：")
print(f"👉 Question: {num1}/{den1} {operation_symbol} {num2}/{den2} = ?")
print("--------------------------------------------------")

while True:
    
    try:
        ans_num_str = input("\nPlease answer the Numerator: ")
        ans_den_str = input("Please answer the Denominator: ")
        ans_num = int(ans_num_str)
        ans_den = int(ans_den_str)
    except ValueError:
        print("Input error! Please ensure you enter integer values.")
        continue

    is_correct = check_answer(num1, den1, num2, den2, operation, ans_num, ans_den)

    feedback_prompt = f"""
    The quiz problem: {num1}/{den1} {operation_symbol} {num2}/{den2} = ?
    The student answered: {ans_num}/{ans_den}
    System Verification Result: {"CORRECT" if is_correct else "WRONG"}.
    
    Please respond directly to the student:
    - If CORRECT: Congratulate them with Hong Kong style energy and confirm they solved it.
    - If WRONG: Gently tell them it's incorrect, guide them on how to find the common denominator if it was an Unlike Denominator problem, and firmly state they must try again now.
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
        user_choice = input("Please enter option (1 or 2): ")

        if user_choice.strip() == "2":
            print("\nReturning to AI Math Tutor main menu...")
            break
        else:
            print("\n==================================================")
            print(f"🎉 Fantastic! It automatically generates the next challenge for you.：")
            
            num1, den1, num2, den2, operation = fraction()
            if operation == "multiply":
                operation_symbol = "×"
            else:
                operation_symbol = "÷"

            print(f"👉 What: {num1}/{den1} {operation_symbol} {num2}/{den2} = ?")
            print("==================================================")

    else:
        print("\nThe answer is not quite right. Don't give up, please recalculate the original problem and enter your answer again!")