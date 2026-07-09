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
    model="ollama:devstral-2:123b-cloud",
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

message = ("What is percentage?",
           "Can you give me examples?",
           "Can you provide me with the relevant documentation?",
           f"Also, if I got {student_part} out of {student_total} marks in my quiz, can you calculate the percentage for me?"
           )

result = agent.invoke(
    {"messages": [{"role": "user", "content": message}]},
    config={"configurable": {"thread_id": "1"}},
)


print(result["messages"][-1].content)