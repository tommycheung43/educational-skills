from pathlib import Path
from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from langgraph.checkpoint.memory import MemorySaver
import webbrowser
import random
import math


def play_add_sub_video(url: str) -> str:
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

url = "https://www.youtube.com/watch?v=xNsyNwAkqfk"

def fraction():
    """Generates random numerators, denominators, and an operation (add/subtract) for a fraction problem."""
    operation = random.choice(["add", "subtract"])
    is_like_denominator = random.choice([True, False])

    den1 = random.randint(2, 10)
    if is_like_denominator:
        den2 = den1
    else:
        den2 = random.randint(2, 10)
        while den2 == den1:
            den2 = random.randint(2, 10)

    num1 = random.randint(1, den1 - 1)
    num2 = random.randint(1, den2 - 1)

    if operation == "subtract" and (num1 / den1 < num2 / den2):
        num1, den1, num2, den2 = num2, den2, num1, den1

    return num1, den1, num2, den2, operation

def get_input(message: str) -> str:
    """Handles getting textual or numerical input from the student via the terminal."""
    return input(message)

def check_answer(num1: int, den1: int, num2: int, den2: int, operation: str, student_num: int, student_den: int) -> bool:
    """Checks if the student's input fraction matches the mathematically correct answer."""
    if student_den == 0:
        return False
    
    if operation == "add":
        correct_val = (num1 / den1) + (num2 / den2)
    else:
        correct_val = (num1 / den1) - (num2 / den2)

    student_val = student_num / student_den
    
    return math.isclose(correct_val, student_val, rel_tol=1e-5)


checkpointer = MemorySaver()
root_dir = "."
backend = FilesystemBackend(root_dir=root_dir, virtual_mode=True)


agent = create_deep_agent(
    model="ollama:gemma4:cloud",  
    backend=backend,
    tools=[play_add_sub_video],
    skills=[str(Path(root_dir) / "skills")],
    interrupt_on={
        "write_file": True,
        "read_file": False,
        "edit_file": True,
    },
    checkpointer=checkpointer,
)


message = f"""What are the rules for adding and subtracting fractions with the same denominator?
Can you give me everyday examples in Hong Kong?
Crucially, you MUST execute your play_add_sub_video tool to open this exact link for me right now: {url}
"""

print("Agent is thinking and preparing to open the video...")

result = agent.invoke(
    {"messages": [{"role": "user", "content": message}]},
    config={"configurable": {"thread_id": "band_session_001"}},
)

print("\n=== Math Tutor Output ===")
print(result["messages"][-1].content)

num1, den1, num2, den2, operation = fraction()
if operation == "add":
    operation_symbol = "+"
else:
    operation_symbol = "-"

print("\n--------------------------------------------------")
print(f"📝 Please answer this question：")
print(f"👉 Question: {num1}/{den1} {operation_symbol} {num2}/{den2} = ?")
print("--------------------------------------------------")

while True:
    try:
        ans_num_str = get_input("\n Please answer the Numerator: ")
        ans_den_str = get_input("Please answer the Denominator: ")
        ans_num = int(ans_num_str)
        ans_den = int(ans_den_str)
    except ValueError:
        print("❌ Input error! Please ensure you enter integer values.")
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
        config={"configurable": {"thread_id": "quiz_session_001"}},
    )

    print("\n=== Tutor Feedback ===")
    print(result["messages"][-1].content)

    if is_correct:
        print("\nCongratulations! You've successfully passed this quiz!")
        break
    else:
        print("\nThe answer is not quite right. Don't give up, please recalculate the original problem and enter your answer again!")