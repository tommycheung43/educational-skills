from pathlib import Path
from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from langgraph.checkpoint.memory import MemorySaver
import webbrowser
import random
import math
import os

from main import run_script
from main import menu_mapping
from stats_graph_generator import safe_generate_graph

import logger_utils
from logger_utils import setup_agent_logging, write_log

from PIL import Image,ImageDraw


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

def view_image(image_name: str) -> str:
    """Opens and displays an image file directly on the student's screen.
    
    Args:
        image_name: The filename of the image to look at and display.
    """
    file_path = Path('res') / image_name
    if not file_path.exists():
        return f"Error: The image file '{image_name}' does not exist in the project folder."
    
    try:
        
        img = Image.open(file_path)
        img.show()

        return f"Success: Successfully opened and popped up the image '{image_name}' on the screen."
    except Exception as e:
        return f"Error: Failed to display the image due to: {str(e)}"

def angle():
    """
    Generatesthe parameters for a polygon angle question.
    """
    n = random.randint(3,10)
    polygon_names = {
            3: "Triangle", 4: "Quadrilateral", 5: "Pentagon",
            6: "Hexagon", 7: "Heptagon", 8: "Octagon",
            9: "Nonagon", 10: "Decagon"
        }
    name = polygon_names[n]
    q_type = random.choice(["total_interior", "each_interior_regular", "each_exterior_regular"])

    return {
        "n": n,
        "name":name,
        "q_type":q_type
    }

def angle_question_text(agent, angle_dict: dict):
    """Uses the AI Agent to generate localized word problems."""
    prompt = f"""
    Based on angles-docs, please generate a creative problem using these EXACT details:
    - Shape: Regular {angle_dict['name']} ({angle_dict['n']}-sided polygon).
    - Question Type: {angle_dict['q_type']}
    
    Requirements:
    1. Clearly ask the student for the numeric angle in degrees.
    2. Keep it under 3 sentences and directly state the problem to the student.
    """

    result = agent.invoke(
        {"messages": [{"role": "user", "content": prompt}]},
        config={
            "configurable": {"thread_id": "angle_quiz_gen_001"},
            "recursion_limit": 15
        },
    )

    return result["messages"][-1].content

def generate_polygon_picture(n: int, filename: str = "polygon_shape.jpg"):
    """Generates a JPG image of a regular n-sided polygon using Pillow (PIL) and displays it.
        
    Args:
        n_sides: The number of sides of the polygon (e.g., 3 for triangle, 5 for pentagon).
        filename: Output filename in the res folder (default: polygon_shape.jpg).
    """
    try:
        res_dir = Path("res")
        res_dir.mkdir(parents=True, exist_ok=True)
        file_path = res_dir / filename
    
        img_size = 500
        center = img_size // 2
        radius = 180
    
        img = Image.new("RGB", (img_size, img_size), "white")
        draw = ImageDraw.Draw(img)
    
        points = []
        for i in range(n):
            angle = 2 * math.pi * i / n - math.pi / 2
            x = center + radius * math.cos(angle)
            y = center + radius * math.sin(angle)
            points.append((x, y))
    
        draw.polygon(points, outline="#1E88E5", fill="#E3F2FD", width=4)
    
        for x, y in points:
            draw.ellipse([x - 5, y - 5, x + 5, y + 5], fill="#D81B60")
    
        img.save(file_path, "JPEG")
        img.show()
    
        return f"Success: Dynamically generated and opened the {n}-sided polygon image at '{file_path}'."
    except Exception as e:
        return f"Error generating polygon image: {str(e)}"


# def get_input(message: str) -> str:
#     """
#     Handles getting textual or numerical input from the student via the terminal.
#     Log the input
#     """
#     student_input = input(message)
#     return student_input

def angle_check_answer(n:int, q_type:str, student_result: float):
    """
    Calculates the mathematically correct answer dynamically,
    then checks if the student's input matches it within acceptable tolerance.
    """
    angle_correct_answer = 0
    if q_type == "total_interior":
        angle_correct_answer = (n - 2) * 180
    elif q_type == "each_interior_regular":
        angle_correct_answer = ((n - 2) * 180) / n
    elif q_type == "each_exterior_regular":
        angle_correct_answer = 360 / n

    is_correct = math.isclose(angle_correct_answer, student_result, abs_tol=0.01)
    return is_correct,angle_correct_answer

if __name__ == "__main__":
    checkpointer = MemorySaver()
    root_dir = "."
    backend = FilesystemBackend(root_dir=root_dir, virtual_mode=True)

    agent = create_deep_agent(
        model="ollama:gemma4:cloud",  
        backend=backend,
        tools=[play_video,run_script, write_log, view_image,generate_polygon_picture],
        skills=[str(Path(root_dir) / "skills")],
        interrupt_on={
            "write_file": True,
            "read_file": False,
            "edit_file": True,
        },
        checkpointer=checkpointer,
    )

    setup_agent_logging(agent)

    message = (
        f"1. Please introduce the concept of Polygon Interior and Exterior Angles following the angle-docs skill.\n"
        f"2. End your message by asking the student if they have any questions, if they need an example, or if they are ready to start.\n"
        f"3. CRITICAL REQUIREMENT: Keep your response extremely concise (under 120 words)."
    )

    print("\n Starting the Angle Tutor...")

    result = agent.invoke(
        {"messages": [{"role": "user", "content": message}]},
        config={
            "configurable": {"thread_id": "angle_session_001"},
            "recursion_limit": 15
        },
    )

    tutor_intro = result["messages"][-1].content
    print("\n=== Math Tutor Output ===")
    print(tutor_intro)

    while True:
        student_q = input("\nAsk a question, request a basic review/diagram explaination, or type 'ready' to start:")

        if student_q.lower().strip() in ["yes","no question", "ready", "start", "none","nope","no questions","i'm ready","quiz","let's start"]:
            print("\nGreat! Let's move on to the quiz phase.")
            break

        else:
            q_prompt = (f"The student asks: '{student_q}'. Answer their question based on angle-docs. "
                        f"If they need to review ANY math topic, USE the `run_script` tool to launch the appropriate python file from this list:\n"
                        f"{menu_mapping}\n"
                        f"AFTER the review tool executes, welcome them back to angle and ask if they are ready for the quiz."
                        f"If they ask to see a picture/diagram/shape, USE the `generate_polygon_picture` tool with a polygon.\n"
                        f"Ask if they are ready for the quiz."
            )

            result = agent.invoke(
                {"messages": [{"role": "user", "content": q_prompt}]},
                config={
                    "configurable": {"thread_id": "angle_session_001"},
                    "recursion_limit": 15
                },
            )

            tutor_resp = result["messages"][-1].content
            print("\n=== Tutor Response ===")
            print(tutor_resp)

    angle_dict = angle()
    angle_question = angle_question_text(agent, angle_dict)

    print("\n--------------------------------------------------")
    print(f" Please answer this question:")
    print(f" {angle_question} ")
    print(" (If the decimal is long, you may round it to 2 decimal places!)")
    print(" (If you are stuck, you can type 'explain' or 'example' or 'video'!)")
    print(" (Hint: You can ask for 'picture' to view the polygon shape!)")
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
            is_correct,angle_correct_answer = angle_check_answer(
                angle_dict["n"],
                angle_dict["q_type"],
                ans_val
            )

            feedback_prompt = f"""
            The quiz problem: Solve {angle_question}
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
            The quiz problem is: Solve {angle_question}
            The student did not enter a numeric answer. Instead, they wrote: "{ans_str}"
            
            Please evaluate the student's input according to angle-docs:
            1. Did the student ask for an explanation (e.g., "explain", "how to do this", "help")?
            2. Did the student ask for an example (e.g., "give me an example", "show me a different one")?
            3. Did the student ask for an video (e.g., "give me an video", "show me a vide example")?
            4. Did the student enter a wrong input format, typo, or off-topic statement?
            5. Did the student ask to review another topic? If so, use `run_script` to launch the appropriate python file from this list:{menu_mapping}, and welcome them back to this angle question once finished.
            6. Did the student ask for a picture/diagram/shape? IF YES: USE `generate_polygon_picture` tool with n={angle_dict['n']}.

            Based on this evaluation, please respond directly to the student:
            - If EXPLANATION: Gently explain the mathematical steps to solve {angle_question} but DO NOT give away the final answer! Keep the challenge active.
            - If EXAMPLE: Provide a brand-new, step-by-step localized Hong Kong example of a similar calculation and solve it fully. Then encourage them to try the active quiz problem using that same method.
            - If VIDEO: Provide a video using the `play_video` tool.
            - If WRONG/INVALID/Off-topic: Politely guide them back, explaining that they should either enter a numerical answer or ask a math question if they are stuck.
            - If REVIEW ANOTHER TOPIC: Call the `run_script` tool to launch that topic's file (e.g., `decimal_mult_div.py`). After returning, welcome them back and ask them to solve the current angle question: {angle_question}.
            """

        result = agent.invoke(
            {"messages": [{"role": "user", "content": feedback_prompt}]},
            config={
                "configurable": {"thread_id": "angle_quiz_001"},
                "recursion_limit": 15
            },
        )

        tutor_feedback = result["messages"][-1].content

        print("\n=== Tutor Feedback ===")
        print(tutor_feedback)

        if is_numeric and is_correct:
            print("\nCongratulations! You solved it!")

            print("\n==================================================")
            print("What would you like to do next?")
            print("1. Keep practicing another question")
            print("2. Move to another topic ")
            print("==================================================")
            user_choice = input("Please enter option (1 or 2): ")

            if user_choice.strip() == "2":

                print("\nReturning to AI Math Tutor main menu...")

                if os.environ.get("LAUNCHED_FROM_MAIN") != "True":
                    run_script("main.py")
                break
            else:
                print("\n==================================================")
                print(f" Fantastic! It automatically generates the next challenge for you.:")
                angle_dict = angle()
                angle_question = angle_question_text(agent, angle_dict)
                print(f" {angle_question} ")
                print("==================================================")

        elif is_numeric and not is_correct:
            print("\nThe answer is not quite right. Don't give up, please recalculate the original problem and enter your answer again!")