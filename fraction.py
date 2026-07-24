from pathlib import Path
from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from langgraph.checkpoint.memory import MemorySaver
import math
import matplotlib.pyplot as plt
from PIL import Image

import logger_utils
from logger_utils import setup_agent_logging, write_log

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
    tools=[fraction,view_image,write_log],
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

message = (
    f"1. What is fraction?"
    f"2. What are numerators and denominators?"
    f"3. Can you give me examples?"
    f"4. Can you provide me with the relevant documentation?"
    f"5. Please calculate the fraction for {numberA} and {numberB}."
    f"6. Crucially, you MUST use your view_image tool to display 'cake.png' to me right now."
    f"CRITICAL REQUIREMENT: Keep your entire response extremely concise, direct, and under 120 words to save tokens."
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": message}]},
    config={
        "configurable": {"thread_id": "1"},
        "recursion_limit": 15
    },
)


print(result["messages"][-1].content)