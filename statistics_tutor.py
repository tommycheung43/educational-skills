from pathlib import Path
from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from langgraph.checkpoint.memory import MemorySaver
import webbrowser
import random
import math
import statistics as stats
import numpy as np
import os

from main import run_script
from main import menu_mapping
from stats_graph_generator import safe_generate_graph

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


def statistics():
    """
    Generates only the statistics problem parameters (question type and dataset).
    """
    topics = [
        "mean", "median", "mode", "range", 
        "variance", "standard deviation", "interquartile range"
    ]
    
    question_type = random.choice(topics)

    n = random.randint(7, 20)
    base_data = [random.randint(10, 50) for _ in range(n - 1)]
    mode_value = random.choice(base_data)

    m = random.randint(2,4)
    data = base_data + [mode_value] * m
    
    random.shuffle(data)

    return {
        "question_type": question_type,
        "data": data
    }

def statistics_question_text(agent, stats_dict: dict):
    """Uses the AI Agent to generate localized word problems."""
    prompt = f"""
    Based on statistics-docs, please generate a creative and localized Hong Kong word problem using these EXACT details:
    - Target to solve for: {stats_dict['question_type'].upper()}
    - Data set (list of numbers): {stats_dict['data']}
    
    Requirements:
    1. Use Hong Kong contexts (e.g., Dim Sum prices, Octopus card balances, temperatures, hiking trail lengths).
    2. Clearly ask the student to calculate the target ({stats_dict['question_type']}) for the provided data set.
    3. Keep it under 3 sentences and directly state the problem to the student.
    """

    result = agent.invoke(
        {"messages": [{"role": "user", "content": prompt}]},
        config={
            "configurable": {"thread_id": "stats_quiz_gen_001"},
            "recursion_limit": 15
        },
    )

    return result["messages"][-1].content


def get_input(message: str) -> str:
    """Handles getting textual or numerical input from the student via the terminal."""
    return input(message)

def statistics_check_answer(question_type: str,data: list, student_result: float):
    """
    Calculates the mathematically correct answer dynamically based on question_type and data,
    then checks if the student's input matches it within acceptable tolerance.
    """
    statistics_correct_answer = ""
    if question_type == "mean":
        statistics_correct_answer = stats.mean(data)
    elif question_type == "median":
        statistics_correct_answer = stats.median(data)
    elif question_type == "mode":
        statistics_correct_answer = stats.mode(data)
    elif question_type == "range":
        statistics_correct_answer = max(data) - min(data)
    elif question_type == "variance":
        statistics_correct_answer = stats.variance(data)
    elif question_type == "standard deviation":
        statistics_correct_answer = stats.stdev(data)
    elif question_type == "interquartile range":
        q3 = np.percentile(data,75)
        q1 = np.percentile(data, 25)
        statistics_correct_answer = q3 - q1
    else:
        return False, 0

    is_correct = math.isclose(statistics_correct_answer, student_result, abs_tol=0.01)
    return is_correct,statistics_correct_answer

if __name__ == "__main__":
    checkpointer = MemorySaver()
    root_dir = "."
    backend = FilesystemBackend(root_dir=root_dir, virtual_mode=True)

    agent = create_deep_agent(
        model="ollama:gemma4:cloud",  
        backend=backend,
        tools=[play_video,run_script,safe_generate_graph],
        skills=[str(Path(root_dir) / "skills")],
        interrupt_on={
            "write_file": True,
            "read_file": False,
            "edit_file": True,
        },
        checkpointer=checkpointer,
    )

    message = (
        f"1. Please introduce the concept of Statistics (Mean, Median, Mode, Range) following the statistics-docs skill.\n"
        f"2. Mention briefly that there are advanced tools like Variance, Standard Deviation, and IQR to measure how spread out numbers are.\n"
        f"3. End your message by asking the student if they have any questions, if they need an example, or if they are ready to start.\n"
        f"4. CRITICAL REQUIREMENT: Keep your response extremely concise (under 120 words)."
    )

    print("\n Starting the Statistics Tutor...")

    result = agent.invoke(
        {"messages": [{"role": "user", "content": message}]},
        config={
            "configurable": {"thread_id": "stats_session_001"},
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
            q_prompt = (f"The student asks: '{student_q}'. Answer their question based on statistics-docs. "
                        f"If they need to review ANY math topic, USE the `run_script` tool to launch the appropriate python file from this list:\n"
                        f"{menu_mapping}\n"
                        f"AFTER the review tool executes, welcome them back to Statistics and ask if they are ready for the quiz."
                        f"Ask if they are ready for the quiz."
            )

            result = agent.invoke(
                {"messages": [{"role": "user", "content": q_prompt}]},
                config={
                    "configurable": {"thread_id": "stats_session_001"},
                    "recursion_limit": 15
                },
            )

            print("\n=== Tutor Response ===")
            print(result["messages"][-1].content)

    stats_dict = statistics()
    stats_question = statistics_question_text(agent, stats_dict)

    print("\n--------------------------------------------------")
    print(f" Please answer this question:")
    print(f" {stats_question} ")
    print(f" (The data set is: {stats_dict['data']})")
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
            is_correct,statistics_correct_answer = statistics_check_answer(
                stats_dict["question_type"], 
                stats_dict["data"], 
                ans_val
            )

            feedback_prompt = f"""
            The quiz problem: Solve {stats_question} with data {stats_dict['data']}
            The student answered: {ans_val}
            System Verification Result: {"CORRECT" if is_correct else "WRONG"}.
            
            Please respond directly to the student:
            - If CORRECT: Congratulate them with Hong Kong style energy and confirm they solved it.
            - If WRONG: Gently tell them it's incorrect, 
                Remind them on the formulas and try again WITHOUT giving away the correct answer, 
                and firmly state they must try again now.
            """
        else:

            is_correct = False
            feedback_prompt = f"""
            The quiz problem is: Solve {stats_question}
            The student did not enter a numeric answer. Instead, they wrote: "{ans_str}"
            
            Please evaluate the student's input according to statistics-docs:
            1. Did the student ask for an explanation (e.g., "explain", "how to do this", "help")?
            2. Did the student ask for an example (e.g., "give me an example", "show me a different one")?
            3. Did the student ask for an video (e.g., "give me an video", "show me a vide example")?
            4. Did the student enter a wrong input format, typo, or off-topic statement?
            5. Did the student ask to review another topic? If so, use `run_script` to launch the appropriate python file from this list:{menu_mapping}, and welcome them back to this statistics question once finished.

            Based on this evaluation, please respond directly to the student:
            - If EXPLANATION: Gently explain the mathematical steps to solve {stats_question} but DO NOT give away the final answer! Keep the challenge active.
            - If EXAMPLE: Provide a brand-new, step-by-step localized Hong Kong example of a similar calculation and solve it fully. Then encourage them to try the active quiz problem using that same method.
            - If VIDEO: Provide a video using the `play_video` tool.
            - If WRONG/INVALID/Off-topic: Politely guide them back, explaining that they should either enter a numerical answer or ask a math question if they are stuck.
            - If REVIEW ANOTHER TOPIC: Call the `run_script` tool to launch that topic's file (e.g., `decimal_mult_div.py`). After returning, welcome them back and ask them to solve the current statistics question: {stats_question}.
            """

        result = agent.invoke(
            {"messages": [{"role": "user", "content": feedback_prompt}]},
            config={
                "configurable": {"thread_id": "stats_quiz_001"},
                "recursion_limit": 15
            },
        )

        print("\n=== Tutor Feedback ===")
        print(result["messages"][-1].content)

        if is_numeric and is_correct:
            print("\nCongratulations! You solved it!")

            print("\nWould you like to see a visual graph for this dataset to understand it better?")
            graph_ans = get_input("Your answer (e.g., 'yes' or 'no'): ")
                        
            graph_prompt = f"""
            The student was asked if they want to see a graph for the dataset: {stats_dict['data']}.
            The current question type is: {stats_dict['question_type']}.
            The student's reply is: "{graph_ans}".
                        
            Based on statistics-graph-docs:
            1. Evaluate if the student means "YES" or "NO".
            2. If YES: 
                - Call the `safe_generate_graph` tool with data {stats_dict['data']} and a suitable title.
                - If question type is "standard deviation" or "variance", pass graph_type="sd".
                - Otherwise, pass graph_type="box".
            Then say: "I have generated the graph for you! Please close the graph window to continue."
            3. If NO: Politely say "No problem, let's move on!"
            """

            graph_result = agent.invoke(
                {"messages": [{"role": "user", "content": graph_prompt}]},
                config={
                    "configurable": {"thread_id": "stats_graph_001"},
                    "recursion_limit": 15
                },
            )

            print("\n=== Tutor Response ===")
            print(graph_result["messages"][-1].content)

            print("\n==================================================")
            print("What would you like to do next?")
            print("1. Keep practicing another question")
            print("2. Move to another topic ")
            print("==================================================")
            user_choice = get_input("Please enter option (1 or 2): ")

            if user_choice.strip() == "2":
                
                print("\nReturning to AI Math Tutor main menu...")

                if os.environ.get("LAUNCHED_FROM_MAIN") != "True":
                    run_script("main.py")
                break
            else:
                print("\n==================================================")
                print(f" Fantastic! It automatically generates the next challenge for you.:")
                stats_dict = statistics()
                stats_question = statistics_question_text(agent, stats_dict)
                print(f" {stats_question} ")
                print(f" (The data set is: {stats_dict['data']})")
                print("==================================================")

        elif is_numeric and not is_correct:
            print("\nThe answer is not quite right. Don't give up, please recalculate the original problem and enter your answer again!")