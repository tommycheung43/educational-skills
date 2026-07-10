import webbrowser
from pathlib import Path
from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from langgraph.checkpoint.memory import MemorySaver


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


video_link = "https://www.youtube.com/watch?v=XsW8HJutIgM"


message = f"""What are the rules for adding and subtracting fractions with the same denominator?
Can you give me everyday examples in Hong Kong?
Crucially, you MUST execute your play_add_sub_video tool to open this exact link for me right now: {video_link}
"""

print("Agent is thinking and preparing to open the video...")

result = agent.invoke(
    {"messages": [{"role": "user", "content": message}]},
    config={"configurable": {"thread_id": "band_session_001"}},
)


print("\n=== Math Tutor Output ===")
print(result["messages"][-1].content)