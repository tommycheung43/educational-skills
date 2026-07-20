from pathlib import Path
from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from langgraph.checkpoint.memory import MemorySaver
import webbrowser
import random
import math

from main import run_script
from main import menu_mapping

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


def speed():
    """
    Generates a physics/math problem involving Speed, Distance, and Time.
    Randomly selects which variable the student needs to find.
    
    Returns:
        tuple: (speed_question, speed_correct_answer_float)
    """
    question_type = random.choice(["speed", "distance", "time"])
    speed = random.randint(10, 200)
    time = random.randint(2, 10)
    distance = speed * time
    
    if question_type == "speed":
        speed_question = f"A car travels a distance of {distance} km in {time} hours. What is its average speed (in km/h)?"
        speed_correct_answer_float = float(speed)
    elif question_type == "distance":
        speed_question = f"A train travels at a speed of {speed} km/h for {time} hours. What is the total distance traveled (in km)?"
        speed_correct_answer_float = float(distance)
    else:
        speed_question = f"A bus needs to travel {distance} km. If its speed is {speed} km/h, how many hours will it take?"
        speed_correct_answer_float = float(time)

    return speed_question, speed_correct_answer_float


def get_input(message: str) -> str:
    """Handles getting textual or numerical input from the student via the terminal."""
    return input(message)

def speed_check_answer(speed_correct_answer_float: float, student_result: float):
    """
    Checks if the student's input matches the mathematically correct answer.
    """
    is_correct = math.isclose(speed_correct_answer_float, student_result, abs_tol=0.01)
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
        f"1. Please introduce the concept of Speed, Distance, and Time following the speed-docs skill.\n"
        f"2. Mention the intuitive idea of the Magic Triangle (DST) to help them visualize.\n"
        f"3. End your message by asking the student if they have any questions, if they need an example, or if they are ready to start.\n"
        f"4. CRITICAL REQUIREMENT: Keep your response extremely concise (under 120 words)."
    )

    print("\n Starting the Speed & Distance Tutor...")

    result = agent.invoke(
        {"messages": [{"role": "user", "content": message}]},
        config={
            "configurable": {"thread_id": "speed_session_001"},
            "recursion_limit": 15
        },
    )

    print("\n=== Math Tutor Output ===")
    print(result["messages"][-1].content)

    while True:
        student_q = get_input("\nAsk a question, request a basic review, or type 'ready' to start:")

        if student_q.lower().strip() in ["yes","no question", "ready", "start", "none","nope","no questions","i'm ready","quiz","let's start"]:
            print("\nGreat! Let's move on to the quiz phase.")
            break

        else:
            q_prompt = (f"The student asks: '{student_q}'. Answer their question based on speed-docs. "
                        f"If they need to review ANY math topic, USE the `run_script` tool to launch the appropriate python file from this list:\n"
                        f"{menu_mapping}\n"
                        f"AFTER the review tool executes, welcome them back to Speed & Distance and ask if they are ready for the quiz."
                        f"Ask if they are ready for the quiz."
            )

            result = agent.invoke(
                {"messages": [{"role": "user", "content": q_prompt}]},
                config={
                    "configurable": {"thread_id": "speed_session_001"},
                    "recursion_limit": 15
                },
            )

            print("\n=== Tutor Response ===")
            print(result["messages"][-1].content)

    speed_question, speed_correct_answer_float = speed()

    print("\n--------------------------------------------------")
    print(f" Please answer this question:")
    print(f" {speed_question} ")
    print(" (If the decimal is long, you may round it to 2 decimal places!)")
    print(" (If you are stuck, you can type 'explain' or 'example' or 'video'!)")
    print("--------------------------------------------------")

    while True:
        
        ans_str = get_input(f"\nWhat is the answer? (or ask a question / request an example) ").strip()

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
            is_correct = speed_check_answer(speed_correct_answer_float, ans_val)

            feedback_prompt = f"""
            The quiz problem: Solve {speed_question}
            The student answered: {ans_val}
            System Verification Result: {"CORRECT" if is_correct else "WRONG"}.
            
            Please respond directly to the student:
            - If CORRECT: Congratulate them with Hong Kong style energy and confirm they solved it.
            - If WRONG: Gently tell them it's incorrect, 
                Remind them on the formulas and try again WITHOUT giving away the correct answer, 
                and firmly state they must try again now.
            """
        else:
            # Student typed text (Could be: explanation request, example request, typo, or off-topic)
            is_correct = False
            feedback_prompt = f"""
            The quiz problem is: Solve {speed_question}
            The student did not enter a numeric answer. Instead, they wrote: "{ans_str}"
            
            Please evaluate the student's input according to speed-docs:
            1. Did the student ask for an explanation (e.g., "explain", "how to do this", "help")?
            2. Did the student ask for an example (e.g., "give me an example", "show me a different one")?
            3. Did the student ask for an video (e.g., "give me an video", "show me a vide example")?
            4. Did the student enter a wrong input format, typo, or off-topic statement?
            5. Did the student ask to review another topic? If so, use `run_script` to launch that topic's file, and welcome them back to this Speed question once finished.

            Based on this evaluation, please respond directly to the student:
            - If EXPLANATION: Gently explain the mathematical steps to solve {speed_question} but DO NOT give away the final answer! Keep the challenge active.
            - If EXAMPLE: Provide a brand-new, step-by-step localized Hong Kong example of a similar calculation and solve it fully. Then encourage them to try the active quiz problem using that same method.
            - If VIDEO: Provide a video using the `play_video` tool.
            - If WRONG/INVALID/Off-topic: Politely guide them back, explaining that they should either enter a numerical answer or ask a math question if they are stuck.
            - If REVIEW ANOTHER TOPIC: Call the `run_script` tool to launch that topic's file (e.g., `decimal_mult_div.py`). After returning, welcome them back and ask them to solve the current Speed question: {speed_question}.
            """

        result = agent.invoke(
            {"messages": [{"role": "user", "content": feedback_prompt}]},
            config={
                "configurable": {"thread_id": "speed_quiz_001"},
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
                speed_question, speed_correct_answer_float = speed()
                print(f" {speed_question} ")
                print("==================================================")

        elif is_numeric and not is_correct:
            print("\nThe answer is not quite right. Don't give up, please recalculate the original problem and enter your answer again!")