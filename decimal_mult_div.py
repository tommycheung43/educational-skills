from ast import If
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

# url = "https://www.youtube.com/watch?v=PnwLv6khwk8"

def decimal_mult_div():
    """
    Generates two random decimals with 1 or 2 decimal places,
    Ensures division results in clean, non-infinite repeating decimals.
    """
    operation = random.choice(["*", "/"])

    if operation == "*":
        
        num1 = round(random.uniform(1.1, 10.0), random.choice([1, 2]))
        num2 = round(random.uniform(1.1, 5.0), random.choice([1, 2]))
        return num1, num2, operation
    else:
        
        divisor = round(random.uniform(1.1, 5.0), random.choice([1, 2]))
        quotient = round(random.uniform(1.1, 6.0), random.choice([1, 2]))
        dividend = round(divisor * quotient, 4) # mathematically perfect
    
        return dividend, divisor, operation


def get_input(message: str) -> str:
    """Handles getting textual or numerical input from the student via the terminal."""
    return input(message)

def decimal_mult_div_answer(num1: float, num2: float, operation: str, student_result: float):
    """
    Checks if the student's input matches the mathematically correct answer.
    """
    
    if operation == "*":
        decimal_mult_div_correct_answer = num1 * num2
    else:
        decimal_mult_div_correct_answer = num1 / num2

    is_correct = math.isclose(decimal_mult_div_correct_answer, student_result, abs_tol=0.01)
    return is_correct, decimal_mult_div_correct_answer

if __name__ == "__main__":
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
        f"1. Please introduce the concept of Decimal Multiplication and Division following the decimal-mult-div-docs skill. \n"
        f"2. Mention the counting rules for multiplication and shifting rules for division.\n"
        f"3. End your message by asking the student if they have any questions, if they need an example, or if they are ready to start.\n"
        f"4. CRITICAL REQUIREMENT: Keep your response extremely concise (under 120 words)."
    )

    print("\n Starting the Decimal Multiplication And Division Tutor...")

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
        student_q = get_input("\nAsk a question, request a review of basic decimals, or type 'ready' to start:")

        if student_q.lower().strip() in ["yes","no question", "ready", "start", "none","nope","no questions","i'm ready","quiz","let's start"]:
            print("\nGreat! Let's move on to the quiz phase.")
            break

        else:
            q_prompt = (f"The student asks: '{student_q}'. Answer their question based on decimal-mult-div-docs. "
                        f"If they need to review basic decimal/addition, USE the `run_script` tool to launch launch the appropriate file."
                        f"Ask if they are ready for the quiz."
            )

            result = agent.invoke(
                {"messages": [{"role": "user", "content": q_prompt}]},
                config={
                    "configurable": {"thread_id": "decimal_mult_div_session_001"},
                    "recursion_limit": 15
                },
            )

            print("\n=== Tutor Response ===")
            print(result["messages"][-1].content)

    num1, num2, operation = decimal_mult_div()

    print("\n--------------------------------------------------")
    print(f" Please answer this question:")
    print(f" {num1} {operation} {num2} = ?")
    print(" (If the decimal is long, you may round it to 2 decimal places!)")
    print("--------------------------------------------------")

    while True:
        
        try:
            ans_str = get_input(f"\nPlease answer: ")
            ans_val = float(ans_str)
        except ValueError:
            print("Input error! Please ensure you enter a valid number.")
            continue

        is_correct, decimal_mult_div_correct_answer = decimal_mult_div_answer(num1, num2, operation, ans_val)

        feedback_prompt = f"""
        The quiz problem: {num1} {operation} {num2}
        The student answered: {ans_val}
        System Verification Result: {"CORRECT" if is_correct else "WRONG"}.
        
        Please respond directly to the student:
        - If CORRECT: Congratulate them with Hong Kong style energy and confirm they solved it.
        - If WRONG: Gently tell them it's incorrect, 
            Remind them on the rule (counting places for multiplication or shifting for division) and try again WITHOUT giving away the correct answer, 
            and firmly state they must try again now.
        """

        result = agent.invoke(
            {"messages": [{"role": "user", "content": feedback_prompt}]},
            config={
                "configurable": {"thread_id": "decimal_mult_div_quiz_001"},
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
                print(f" Fantastic! It automatically generates the next challenge for you.:")
                num1, num2, operation = decimal_mult_div()
                print(f" {num1} {operation} {num2} = ?")
                print("==================================================")

        else:
            print("\nThe answer is not quite right. Don't give up, please recalculate the original problem and enter your answer again!")