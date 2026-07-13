from pathlib import Path
from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from langgraph.checkpoint.memory import MemorySaver
import math
import matplotlib.pyplot as plt
from PIL import Image

def fraction(numerator: float, denominator: float) -> str:
    """Calculates the fraction when a student inputs a numerator and a denominator.
    
    Args:
        numerator: The top number of the fraction (parts chosen / numerator).
        denominator: The bottom number of the fraction (total parts / denominator).
    """

    if denominator == 0 :
        return "Error: The denominator must be greater than zero."
    
    if numerator.is_integer() and denominator.is_integer():
        num = int(numerator)
        den = int(denominator)

        gcd_value = math.gcd(num, den)

        simplified_num = num // gcd_value
        simplified_den = den // gcd_value
        return f"The fraction {num}/{den} simplified to its lowest terms is {simplified_num}/{simplified_den}."
    else:
        # Fallback handling for decimal inputs
        decimal_result = numerator / denominator
        return f"The fraction of {numerator}/{denominator} is equivalent to the decimal value {decimal_result:.4f}."

def view_image(image_name: str) -> str:
    """Opens and displays an image file (like 'cake.png' or 'fraction_visual.jpg') directly on the student's screen.
    
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

checkpointer = MemorySaver()
root_dir = "."
backend = FilesystemBackend(root_dir=root_dir, virtual_mode=True)

agent = create_deep_agent(
    model="ollama:gemma4:cloud",
    backend=backend,
    tools=[fraction,view_image],
    skills=[str(Path(root_dir) / "skills")],
    interrupt_on={
        "write_file": True,
        "read_file": False,
        "edit_file": True,
    },
    checkpointer=checkpointer,
)

numberA = input("Enter the numerator (e.g., 35): ")
numberB = input("Enter the denominator (e.g., 40): ")

message = (f"""What is fraction?
            What are numerators and denominators?
            Can you give me examples?
            Can you provide me with the relevant documentation?
            Please calculate the fraction for {numberA} and {numberB}.
            Crucially, you MUST use your view_image tool to display 'cake.png' to me right now.
            """
           )

result = agent.invoke(
    {"messages": [{"role": "user", "content": message}]},
    config={"configurable": {"thread_id": "1"}},
)


print(result["messages"][-1].content)