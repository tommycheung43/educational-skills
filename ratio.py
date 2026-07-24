from pathlib import Path
from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from langgraph.checkpoint.memory import MemorySaver
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import logger_utils
from logger_utils import setup_agent_logging, write_log

def ratio(numberA: float, numberB: float) -> str:
    """Calculates the ratio when a student inputs two values (numberA:numberB).
    
    Args:
        numberA: The first number obtained (e.g., 35 boys).
        numberB: The second number obtained (e.g., 40 girls).
    """

    if numberA <= 0 or numberB <= 0:
        return "Error: The value must be greater than zero."
    
    if numberA.is_integer() and numberB.is_integer():
        int_a = int(numberA)
        int_b = int(numberB)
        gcd_value = math.gcd(int_a, int_b)
        simplified_a = int_a // gcd_value
        simplified_b = int_b // gcd_value
        return f"The mathematical ratio of {int_a}:{int_b} simplified to its lowest terms is {simplified_a}:{simplified_b}."
    else:
        # Fallback handling for decimal inputs
        decimal_ratio = numberA / numberB
        return f"The decimal ratio of {numberA}:{numberB} is equivalent to {decimal_ratio:.2f}:1."

def generate_ratio_chart(numberA: float, numberB: float) -> str:
    """Generates and saves an educational visual diagram (JPG) comparing two quantities for the ratio.
    
    Args:
        numberA: Numerical count for the first group (Item A).
        numberB: Numerical count for the second group (Item B).
    """
    
    fig, ax = plt.subplots(figsize=(6, 4))
    categories = [numberA, numberB]
    values = [numberA, numberB]
    colors = ['#3498db', '#e74c3c']  
    
    bars = ax.bar(categories, values, color=colors, width=0.4)
    ax.set_ylabel('Amounts / Units')
    ax.set_title(f'Visualizing the Ratio: {numberA} vs {numberB}')
    

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    output_filename = "ratio_visual.jpg"
    plt.savefig(output_filename, dpi=150, bbox_inches='tight')
    plt.close()
    return f"Success: Visual diagram generated and saved to file path: '{output_filename}'."

checkpointer = MemorySaver()
root_dir = "."
backend = FilesystemBackend(root_dir=root_dir, virtual_mode=True)

agent = create_deep_agent(
    model="ollama:gemma4:cloud",
    backend=backend,
    tools=[ratio, generate_ratio_chart,write_log],
    skills=[str(Path(root_dir) / "skills")],
    interrupt_on={
        "write_file": True,
        "read_file": False,
        "edit_file": True,
    },
    checkpointer=checkpointer,
)

numberA = input("Enter the first number (e.g., 35): ")
numberB = input("Enter the second number (e.g., 40): ")

message = (
    f"1. Briefly explain what ratio and proportion are with examples.\n"
    f"2. Generate the visual helper chart using your tool for {numberA} and {numberB}.\n"
    f"3. Calculate the simplified ratio for {numberA} and {numberB} using your tool.\n"
    f"CRITICAL REQUIREMENT: Do NOT look for external web tools. Rely ONLY on your skill files. "
    f"Keep the total response under 150 words to save tokens." 
    )

result = agent.invoke(
    {"messages": [{"role": "user", "content": message}]},
    config={
        "configurable": {"thread_id": "1"},
        "recursion_limit": 15
    },
)


print(result["messages"][-1].content)