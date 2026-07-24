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


def negative():
    """
    Generates an arithmetic problem involving negative numbers.
    Covers addition, subtraction, multiplication, and division.
    Ensures that at least one negative number is involved and division is clean.
    
    Returns:
        tuple: (question_string, correct_answer_float)
    """
    operation = random.choice(["+","-","*","/"])

    num1 = random.randint(1,20)
    num2 = random.randint(-20,-1)
    neg_first = random.choice([True,False])
    negative_question_answer = 0
    negative_question = ""
    if neg_first:
        num1,num2 = num2,num1

    if operation == "+":
        negative_question_answer = num1 + num2
    elif operation == "-":
            negative_question_answer = num1 - num2
    elif operation == "*":
        negative_question_answer = num1 * num2
    elif operation == "/":
        negative_question_answer = num1/num2
    
    negative_question = f"({num1}{operation}{num2})"

    return negative_question, negative_question_answer


# def get_input(message: str) -> str:
#     """Handles getting textual or numerical input from the student via the terminal."""
#     return input(message)

def negative_check_answer(negative_question_answer: float, student_result: float):
    """
    Checks if the student's input matches the mathematically correct answer.
    """

    is_correct = math.isclose(negative_question_answer, student_result, abs_tol=0.01)
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
        f"1. Please introduce the concept of negative numbers and their arithmetic following the negative-number-arithmetic-docs skill.\n"
        f"2. Mention the intuitive idea of cash vs debt or underground floors to help them visualize.\n"
        f"3. End your message by asking the student if they have any questions, if they need an example, or if they are ready to start.\n"
        f"4. CRITICAL REQUIREMENT: Keep your response extremely concise (under 120 words)."
    )

    print("\n Starting the Negative Number Arithmetic Tutor...")

    result = agent.invoke(
        {"messages": [{"role": "user", "content": message}]},
        config={
            "configurable": {"thread_id": "negative_arithmetic_session_001"},
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
            q_prompt = (f"The student asks: '{student_q}'. Answer their question based on negative-number-arithmetic-docs. "
                        f"If they need to review basic calculation review, USE the `run_script` tool to launch launch the appropriate file."
                        f"Ask if they are ready for the quiz."
            )

            result = agent.invoke(
                {"messages": [{"role": "user", "content": q_prompt}]},
                config={
                    "configurable": {"thread_id": "negative_arithmetic_session_001"},
                    "recursion_limit": 15
                },
            )

            print("\n=== Tutor Response ===")
            print(result["messages"][-1].content)

    negative_question, negative_question_answer = negative()

    print("\n--------------------------------------------------")
    print(f" Please answer this question:")
    print(f" {negative_question} ")
    print(" (If the decimal is long, you may round it to 2 decimal places!)")
    print(" (If you are stuck, you can type 'explain' or 'example' or 'video'!)")
    print("--------------------------------------------------")

    while True:
        
        ans_str = input(f"\nWhat is the answer? (or ask a question / request an example) ").strip()

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
            is_correct = negative_check_answer(negative_question_answer, ans_val)

            feedback_prompt = f"""
            The quiz problem: Solve {negative_question}
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
            The quiz problem is: Solve {negative_question}
            The student did not enter a numeric answer. Instead, they wrote: "{ans_str}"
            
            Please evaluate the student's input according to negative-number-arithmetic-docs:
            1. Did the student ask for an explanation (e.g., "explain", "how to do this", "help")?
            2. Did the student ask for an example (e.g., "give me an example", "show me a different one")?
            3. Did the student ask for an video (e.g., "give me an video", "show me a vide example")?
            4. Did the student enter a wrong input format, typo, or off-topic statement?
            
            Based on this evaluation, please respond directly to the student:
            - If EXPLANATION: Gently explain the mathematical steps to solve {negative_question} but DO NOT give away the final answer! Keep the challenge active.
            - If EXAMPLE: Provide a brand-new, step-by-step localized Hong Kong example of a similar calculation and solve it fully. Then encourage them to try the active quiz problem using that same method.
            - If VIDEO: Provide a video using the `play_video` tool.
            - If WRONG/INVALID/Off-topic: Politely guide them back, explaining that they should either enter a numerical answer or ask a math question if they are stuck.
            """

        result = agent.invoke(
            {"messages": [{"role": "user", "content": feedback_prompt}]},
            config={
                "configurable": {"thread_id": "negative_arithmetic_quiz_001"},
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
                negative_question, negative_question_answer = negative()
                print(f" {negative_question} ")
                print("==================================================")

        elif is_numeric and not is_correct:
            print("\nThe answer is not quite right. Don't give up, please recalculate the original problem and enter your answer again!")