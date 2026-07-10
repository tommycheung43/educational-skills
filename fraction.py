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

# def generate_fraction_chart(numerator: float, denominator: float) -> str:
#     """
#     Generates and saves an educational pie chart or visual diagram (JPG) representing the fraction.
    
#     """
    
#     if denominator <= 0 or numerator < 0 or not numerator.is_integer() or not denominator.is_integer():
        
#         fig, ax = plt.subplots(figsize=(5, 5))
#         ax.text(0.5, 0.5, f"Visualizing: {numerator} / {denominator}", ha='center', va='center', fontsize=14)
#         ax.axis('off')
    
#     else:
#         num = int(numerator)
#         den = int(denominator)

#         if num <= den:
#             fig, ax = plt.subplots(figsize=(5, 5))
#             sizes = [num, den - num] if den > num else [num]
#             colors = ['#3498db', '#ecf0f1'] if den > num else ['#3498db']
#             labels = ['Selected Parts', 'Remaining'] if den > num else ['Whole']

#             ax.pie(sizes, labels=labels, autopct=lambda p: '{:.0f} parts'.format(p * den / 100) if p > 0 else '',
#                    colors=colors, startangle=90, wedgeprops={'edgecolor': 'black'})
#             ax.set_title(f"Visualizing Fraction: {num}/{den}")
            
#         else:
           
#             fig, ax = plt.subplots(figsize=(6, 4))
#             ax.bar(['Numerator (Parts)', 'Denominator (Whole)'], [num, den], color=['#3498db', '#e74c3c'], width=0.4)
#             ax.set_ylabel('Values')
#             ax.set_title(f"Improper Fraction Visual: {num}/{den}")

#     output_filename = "fraction_visual.jpg"
#     plt.savefig(output_filename, dpi=150, bbox_inches='tight')
#     plt.close()
#     return f"Success: Visual diagram generated and saved to file path: '{output_filename}'."

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