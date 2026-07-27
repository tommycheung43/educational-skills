import os
import builtins

from datetime import datetime

filename = "dialogue_history.txt"
last_tutor_message = ""


def get_skill_name() -> str:
    """Retrieves the name of the currently executed Skill (default is PYTHAGOREAN)."""
    return os.environ.get("CURRENT_SKILL_NAME", "MAIN")

original_print = builtins.print

def write_log(role: str, text: str):
    """
    Writes a structured log entry into dialogue_history.txt.
    Use this tool to log critical system events, evaluations, or prompt generated questions.
    
    Args:
        role: The entity performing the action ("SYSTEM", "TUTOR", or "STUDENT").
        text: The message content or event description to log.
    """
    if not text or not str(text).strip():
        return "Empty log ignored."
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    skill_name = get_skill_name().upper()
    formatted_log = f"[{timestamp}] [{skill_name}] {role.upper()}: {str(text).strip()}\n"
    
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(formatted_log)
            return f"Successfully recorded log: {formatted_log.strip()}"
    except Exception as e:
        original_print(f"[Logger Error] Failed to write log: {e}")

original_input = builtins.input

def logged_input(prompt: str = "") -> str:
    user_entry = original_input(prompt)
    write_log("STUDENT", user_entry)
    return user_entry

builtins.input = logged_input

def logged_print(*args, **kwargs):
    global last_tutor_message

    original_print(*args, **kwargs)

    text = " ".join(str(a) for a in args).strip()
    if not text:
        return

    if text == last_tutor_message:
        last_tutor_message = "" 
        return

    if text.startswith("===") or text.startswith("---"):
        return

    write_log("AGENT", text)

builtins.print = logged_print

def setup_agent_logging(agent):
    """Package the agent so that each agent.invoke call automatically records the AI's response."""
    original_invoke = agent.invoke

    def logged_invoke(input_data, config=None):
        global last_tutor_message
        response = original_invoke(input_data, config=config)
        if "messages" in response and response["messages"]:
            last_message = response["messages"][-1].content
            last_tutor_message = last_message.strip()
            write_log("AGENT", last_message)
        return response

    agent.invoke = logged_invoke
    return agent

