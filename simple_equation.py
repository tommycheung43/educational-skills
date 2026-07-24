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


def simple_equation():
    """
    Generates a 2-steps equation (e.g., 2x + 5 = 15 or 15 = 2x + 5).
    Ensures the correct answer is a clean integer.
    """
    operation = random.choice(["+","-"])
    var = random.choice(['x', 'y', 'm', 'k', 'a'])
    is_var_on_lhs = random.choice([True, False])

    two_steps_equation_ans = random.randint(2, 20)
    coef = random.randint(2, 20)
    const = random.randint(1, 20)
    
    lhs = ""
    rhs = "" 
    two_steps_equation = ""

    if operation == '+':
        total = coef * two_steps_equation_ans + const
        equation_part = f"{coef}{var} + {const}"
    else:
        total = coef * two_steps_equation_ans - const
        equation_part = f"{coef}{var} - {const}"

    if is_var_on_lhs:
        two_steps_equation = f"{equation_part} = {total}"
    else:
        two_steps_equation = f"{total} = {equation_part}"

    return two_steps_equation, var, float(two_steps_equation_ans)


# def get_input(message: str) -> str:
#     """Handles getting textual or numerical input from the student via the terminal."""
#     return input(message)

def two_steps_equation_answer(two_steps_equation_ans: float, student_result: float):
    """
    Checks if the student's input matches the mathematically correct answer.
    """

    is_correct = math.isclose(two_steps_equation_ans, student_result, abs_tol=0.01)
    return is_correct

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
        f"1. Please introduce the concept of Simple Equation (solving 2-steps equations) following the simple-equation-docs skill. \n"
        f"2. Mention the idea of peeling the onion (undoing + or - first, then * or /).\n"
        f"3. End your message by asking the student if they have any questions, if they need an example, or if they are ready to start.\n"
        f"4. CRITICAL REQUIREMENT: Keep your response extremely concise (under 120 words)."
    )

    print("\n Starting the Simple Equation Tutor...")

    result = agent.invoke(
        {"messages": [{"role": "user", "content": message}]},
        config={
            "configurable": {"thread_id": "two_step_equation_session_001"},
            "recursion_limit": 15
        },
    )

    print("\n=== Math Tutor Output ===")
    print(result["messages"][-1].content)

    while True:
        student_q = input("\nAsk a question, request a basic review, or type 'ready' to start:")

        if student_q.lower().strip() in ["yes","no question", "ready", "start", "none","nope","no questions","i'm ready","quiz","let's start"]:
            print("\nGreat! Let's move on to the quiz phase.")
            break

        else:
            q_prompt = (f"The student asks: '{student_q}'. Answer their question based on simple-equation-docs. "
                        f"If they need to review basic calculation review, USE the `run_script` tool to launch launch the appropriate file."
                        f"Ask if they are ready for the quiz."
            )

            result = agent.invoke(
                {"messages": [{"role": "user", "content": q_prompt}]},
                config={
                    "configurable": {"thread_id": "two_step_equation_session_001"},
                    "recursion_limit": 15
                },
            )

            print("\n=== Tutor Response ===")
            print(result["messages"][-1].content)

    two_steps_equation, var, two_steps_equation_ans = simple_equation()

    print("\n--------------------------------------------------")
    print(f" Please answer this question:")
    print(f" {two_steps_equation} ")
    print(" (If the decimal is long, you may round it to 2 decimal places!)")
    print(" (If you are stuck, you can type 'explain' or 'example' or 'video'!)")
    print("--------------------------------------------------")

    while True:
        
        ans_str = input(f"\nWhat is the value of {var}? (or ask a question / request an example) ").strip()

        if ans_str.lower() in ["quit", "exit"]:
            print("Exiting quiz...")
            break
        is_numeric = False

        try:
            ans_val = float(ans_str)
            is_numeric = True

        except ValueError:
            is_numeric = False

        if is_numeric:
            is_correct = two_steps_equation_answer(two_steps_equation_ans, ans_val)

            feedback_prompt = f"""
            The quiz problem: {two_steps_equation}
            The student answered: {ans_val}
            System Verification Result: {"CORRECT" if is_correct else "WRONG"}.
            
            Please respond directly to the student:
            - If CORRECT: Congratulate them with Hong Kong style energy and confirm they solved it.
            - If WRONG: Gently tell them it's incorrect, 
                Remind them on the rule Inverse Operations to isolate the variable and try again WITHOUT giving away the correct answer, 
                and firmly state they must try again now.
            """
        else:
            # Student typed text (Could be: explanation request, example request, typo, or off-topic)
            is_correct = False
            feedback_prompt = f"""
            The quiz problem is: Solve {two_steps_equation}
            The student did not enter a numeric answer. Instead, they wrote: "{ans_str}"
            
            Please evaluate the student's input according to simple-equation-docs:
            1. Did the student ask for an explanation (e.g., "explain", "how to do this", "help")?
            2. Did the student ask for an example (e.g., "give me an example", "show me a different one")?
            3. Did the student ask for an video (e.g., "give me an video", "show me a vide example")?
            4. Did the student enter a wrong input format, typo, or off-topic statement?
            
            Based on this evaluation, please respond directly to the student:
            - If EXPLANATION: Gently explain the mathematical steps to solve {two_steps_equation} but DO NOT give away the final answer! Keep the challenge active.
            - If EXAMPLE: Provide a brand-new, step-by-step localized Hong Kong example of a similar calculation and solve it fully. Then encourage them to try the active quiz problem using that same method.
            - If VIDEO: Provide a video using the `play_video` tool.
            - If WRONG/INVALID/Off-topic: Politely guide them back, explaining that they should either enter a numerical answer or ask a math question if they are stuck.
            """

        result = agent.invoke(
            {"messages": [{"role": "user", "content": feedback_prompt}]},
            config={
                "configurable": {"thread_id": "two_steps_equation_quiz_001"},
                "recursion_limit": 15
            },
        )

        print("\n=== Tutor Feedback ===")
        print(result["messages"][-1].content)

        if is_numeric and is_correct:
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
                two_steps_equation, var, two_steps_equation_ans = simple_equation()
                print(f" {two_steps_equation} ")
                print("==================================================")

        elif is_numeric and not is_correct:
            print("\nThe answer is not quite right. Don't give up, please recalculate the original problem and enter your answer again!")