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

url = "https://www.youtube.com/watch?v=guBVW5PiHLs"

def fraction_to_decimal():
    """
    Generates a fraction suitable for primary students to convert to a decimal.
    We pick denominators that result in clean, non-repeating decimals mostly.
    """
    denominator = random.randint(2, 20)
    
    # Ensure numerator is smaller than denominator so it's < 1
    numerator = random.randint(1, denominator - 1)
    
    return numerator, denominator


# def get_input(message: str) -> str:
#     """Handles getting textual or numerical input from the student via the terminal."""
#     return input(message)

def fraction_to_decimal_answer(numerator: int, denominator: int, student_result: float):
    """
    Checks if the student's input matches the mathematically correct answer.
    Accepts:
    1. The exact decimal representation (with 0.001 tolerance).
    2. Standard school rounding to 2 decimal places (half-up, e.g., 1/3 -> 0.33, 2/3 -> 0.67, 1/8 -> 0.13).
    3. Banker's rounding to 2 decimal places (Python default, e.g., 1/8 -> 0.12).
    """
    
    fraction_to_decimal_correct_answer = numerator / denominator

    is_correct = math.isclose(fraction_to_decimal_correct_answer, student_result, abs_tol=0.01)
    return is_correct, fraction_to_decimal_correct_answer

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
        f"1. Please introduce the concept of converting Fractions to Decimals following the fraction-to-decimal-docs skill. \n"
        f"2. End your message by asking the student if they have any questions, if they need an example, or if they are ready to start.\n"
        f"3. CRITICAL REQUIREMENT: Keep your entire response extremely concise, direct, and under 120 words to save tokens."
    )

    print("\n Starting the Fraction to Decimal Tutor...")

    result = agent.invoke(
        {"messages": [{"role": "user", "content": message}]},
        config={
            "configurable": {"thread_id": "fraction_decimal_session_001"},
            "recursion_limit": 15
        },
    )

    print("\n=== Math Tutor Output ===")
    print(result["messages"][-1].content)

    while True:
        student_q = input("\nAsk a question, request a review of basic fractions, or type 'ready' to start:")

        if student_q.lower().strip() in ["yes","no question", "ready", "start", "none","nope","no questions","i'm ready","quiz","let's start"]:
            print("\nGreat! Let's move on to the quiz phase.")
            break

        else:
            q_prompt = f"The student asks: '{student_q}'. Answer their question based on fraction-to-decimal-docs. If they need to review basic fractions, USE the run_script tool to launch 'fraction.py'. Ask if they are ready for the quiz."

            result = agent.invoke(
                {"messages": [{"role": "user", "content": q_prompt}]},
                config={
                    "configurable": {"thread_id": "fraction_decimal_session_001"},
                    "recursion_limit": 15
                },
            )

            print("\n=== Tutor Response ===")
            print(result["messages"][-1].content)

    numerator, denominator = fraction_to_decimal()

    print("\n--------------------------------------------------")
    print(f" Please answer this question:")
    print(f" Convert this fraction into a decimal: {numerator}/{denominator}")
    print(" (If the decimal is a repeating or long decimal, you may round it to 2 decimal places!)")
    print("--------------------------------------------------")

    while True:
        
        try:
            ans_str = input(f"\nPlease answer the decimal value: ")
            ans_val = float(ans_str)
        except ValueError:
            print("Input error! Please ensure you enter a valid number.")
            continue

        is_correct,fraction_to_decimal_correct_answer = fraction_to_decimal_answer(numerator, denominator, ans_val)

        feedback_prompt = f"""
        The quiz problem: Convert {numerator}/{denominator} to a decimal.
        The student answered: {ans_val}
        System Verification Result: {"CORRECT" if is_correct else "WRONG"}.
        
        Please respond directly to the student:
        - If CORRECT: Congratulate them with Hong Kong style energy and confirm they solved it.
        - If WRONG: Gently tell them it's incorrect, 
            guide them on the formula (Numerator ÷ Denominator) WITHOUT giving away the exact correct decimal answer, 
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
                numerator, denominator = fraction_to_decimal()
                print(f" Convert this fraction into a decimal: {numerator}/{denominator}")
                print(" (If the decimal is a repeating or long decimal, you may round it to 2 decimal places!)")
                print("==================================================")

        else:
            print("\nThe answer is not quite right. Don't give up, please recalculate the original problem and enter your answer again!")