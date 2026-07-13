from pathlib import Path
from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from langgraph.checkpoint.memory import MemorySaver

def percentage(part: float, total: float) -> str:
    """Calculates the percentage when a student inputs a part and a total whole value.
    
    Args:
        part: The score or portion obtained (e.g., 35 marks).
        total: The maximum possible score or whole value (e.g., 40 marks).
    """

    if total == 0:
        return "Error: The total value cannot be zero."
    result = (part / total) * 100
    return f"{part} out of {total} is {result:.2f}%"

checkpointer = MemorySaver()
root_dir = "."
backend = FilesystemBackend(root_dir=root_dir, virtual_mode=True)

agent = create_deep_agent(
    model="ollama:gemma4:cloud",
    backend=backend,
    tools=[percentage],
    skills=[str(Path(root_dir) / "skills")],
    interrupt_on={
        "write_file": True,
        "read_file": False,
        "edit_file": True,
    },
    checkpointer=checkpointer,
)

student_part = input("Enter your score/part (e.g., 35): ")
student_total = input("Enter the total score (e.g., 40): ")

message = (
    f"1. Briefly explain what percentage is with one simple example.\n"
    f"2. Provide a short documentation snippet.\n"
    f"3. Calculate the percentage for {student_part} out of {student_total} using your tool.\n"
    f"CRITICAL REQUIREMENT: Keep your entire response extremely concise, direct, and under 120 words to save tokens."
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": message}]},
    config={"configurable": {"thread_id": "1"},
            "recursion_limit": 15
    },
)


print(result["messages"][-1].content)