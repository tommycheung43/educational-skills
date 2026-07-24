from ast import If
from pathlib import Path
from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from langgraph.checkpoint.memory import MemorySaver
import webbrowser
import random
import math

from main import run_script
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

url = "https://www.youtube.com/watch?v=PnwLv6khwk8"

def decimal_add_sub():
    """
    Generates two random decimals with 1 or 2 decimal places,
    and randomly chooses between addition (+) and subtraction (-).
    """
    num1 = round(random.uniform(5.0, 50.0), random.choice([1, 2]))
    num2 = round(random.uniform(1.0, 20.0), random.choice([1, 2]))
    operation = random.choice(["+", "-"])
    
    if operation == "-" and num1 < num2:
        num1, num2 = num2, num1
    
    return num1, num2, operation


# def get_input(message: str) -> str:
#     """Handles getting textual or numerical input from the student via the terminal."""
#     return input(message)

def decimal_add_sub_answer(num1: float, num2: float, operation: str, student_result: float):
    """
    Checks if the student's input matches the mathematically correct answer.
    """
    
    if operation == "+":
        decimal_add_sub_correct_answer = num1 + num2
    else:
        decimal_add_sub_correct_answer = num1 - num2

    is_correct = math.isclose(decimal_add_sub_correct_answer, student_result, abs_tol=0.01)
    return is_correct, decimal_add_sub_correct_answer

if __name__ == "__main__":
    checkpointer = MemorySaver()
    root_dir = "."
    backend = FilesystemBackend(root_dir=root_dir, virtual_mode=True)

    agent = create_deep_agent(
        model="ollama:gemma4:cloud",  
        backend=backend,
        tools=[play_video,run_script,write_log],
        skills=[str(Path(root_dir) / "skills")],
        interrupt_on={
            "write_file": True,
            "read_file": False,
            "edit_file": True,
        },
        checkpointer=checkpointer,
    )

    message = (
        f"1. Introduce the concept of Decimal Addition and Subtraction using the decimal-add-sub-docs skill.\n"
        f"2. Emphasize aligning decimal points and using zero placeholders.\n"
        f"3. Ask the student if they want an example, have questions, or are ready to start the quiz.\n"
        f"4. CRITICAL REQUIREMENT: Keep your response extremely concise (under 120 words)."
    )

    print("\n Starting the Decimal Addition and Subtraction Tutor...")

    result = agent.invoke(
        {"messages": [{"role": "user", "content": message}]},
        config={
            "configurable": {"thread_id": "decimal_add_sub_session_001"},
            "recursion_limit": 15
        },
    )

    print("\n=== Math Tutor Output ===")
    print(result["messages"][-1].content)

    while True:
        student_q = input("\nAsk a question, request a review of basic decimals, or type 'ready' to start:")

        if student_q.lower().strip() in ["yes","no question", "ready", "start", "none","nope","no questions","i'm ready","quiz","let's start"]:
            print("\nGreat! Let's move on to the quiz phase.")
            break

        else:
            q_prompt = (f"The student asks: '{student_q}'. Answer their question based on decimal-add-sub-docs."
                        f"If they need to review basic decimals, USE the `run_script` tool to launch 'fraction_to_decimal.py'."
                        f"Ask if they are ready for the quiz."
            )

            result = agent.invoke(
                {"messages": [{"role": "user", "content": q_prompt}]},
                config={
                    "configurable": {"thread_id": "decimal_add_sub_session_001"},
                    "recursion_limit": 15
                },
            )

            print("\n=== Tutor Response ===")
            print(result["messages"][-1].content)

    num1, num2, operation = decimal_add_sub()

    print("\n--------------------------------------------------")
    print(f" Please answer this question:")
    print(f" {num1} {operation} {num2} = ?")
    print("--------------------------------------------------")

    while True:
        
        try:
            ans_str = input(f"\nPlease answer: ")
            ans_val = float(ans_str)
        except ValueError:
            print("Input error! Please ensure you enter a valid number.")
            continue

        is_correct, decimal_add_sub_correct_answer = decimal_add_sub_answer(num1, num2, operation, ans_val)

        feedback_prompt = f"""
        The quiz problem: {num1} {operation} {num2}
        The student answered: {ans_val}
        System Verification Result: {"CORRECT" if is_correct else "WRONG"}.
        
        Please respond directly to the student:
        - If CORRECT: Congratulate them with Hong Kong style energy and confirm they solved it.
        - If WRONG: Gently tell them it's incorrect, 
            Remind them to align decimal points and try again WITHOUT giving away the correct answer, 
            and firmly state they must try again now.
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
                import os
                print("\nReturning to AI Math Tutor main menu...")

                if os.environ.get("LAUNCHED_FROM_MAIN") != "True":
                    run_script("main.py")
                break
            else:
                print("\n==================================================")
                print(f" Fantastic! It automatically generates the next challenge for you.:")
                num1, num2, operation = decimal_add_sub()
                print(f" {num1} {operation} {num2} = ?")
                print("==================================================")

        else:
            print("\nThe answer is not quite right. Don't give up, please recalculate the original problem and enter your answer again!")