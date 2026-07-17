import os
import subprocess
import sys
from pathlib import Path
from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from langgraph.checkpoint.memory import MemorySaver

def run_script(script_name: str) -> str:
    """Runs a specific student script using 'uv run'."""
    script_path = Path(script_name)
    if not script_path.exists():
        return f"Error: {script_name} not found."
    
    try:
        env = os.environ.copy()
        env["LAUNCHED_FROM_MAIN"] = "True"
        
        subprocess.run(["uv", "run", str(script_path)], check=True)
        return f"Successfully executed {script_name}."
    except Exception as e:
        return f"Error running {script_name}: {str(e)}"
    

checkpointer = MemorySaver()
root_dir = "."
backend = FilesystemBackend(root_dir=root_dir, virtual_mode=True)

agent = create_deep_agent(
    model="ollama:gemma4:cloud",
    backend=backend,
    tools=[run_script],
    skills=[str(Path(root_dir) / "skills")],
    interrupt_on={
        "write_file": True,
        "read_file": False,
        "edit_file": True,
    },
    checkpointer=checkpointer,
)

def main():
    print("Welcome to the Hong Kong AI Math Tutor!")
    print("I can help you with:")
    print("  - Percentages (percentage.py)")
    print("  - Ratios & Proportions (ratio.py)")
    print("  - Basic Fractions (fraction.py)")
    print("  - Adding & Subtracting Fractions (fraction_add_sub.py)")
    print("  - Multiplying & Dividing Fractions (fraction_muli_div.py)")
    print("  - Area and Perimeter of Rectangles and Squares (area_perimeter_rectangle.py)")
    print("  - Area and Perimeter of Circles (area_perimeter_circle.py)")
    print("  - Area and Perimeter of Parallelograms (area_perimeter_parallelogram.py)")
    print("  - Area and Perimeter of Triangles (area_perimeter_triangle.py)")
    print("  - Area and Perimeter of Trapezoids (area_perimeter_trapezoid.py)")
    print("  - Volume of different shapes (volume.py)")
    print("  - Decimals (fraction_to_decimal.py)")
    print("  - Decimals Adding & Subtracting (decimal_add_sub.py)")
    print("  - Decimals Multiplication & Division (decimal_mult_div.py)")
    print("  - Basic Equation Concept (elementary_algebra.py)")
    print("  - Simple Equation (simple_equation.py)")


    while True:
        user_input = input("\n👉 What topic would you like to learn today? (or 'quit'): ")
        
        if user_input.lower() in ['quit', 'exit']:
            print("Class dismissed! See you next time.")
            break
            
        # The agent decides which file to run
        response = agent.invoke(
            {"messages": [{"role": "user", "content": f"The student wants to learn: {user_input}. Please identify the correct file and use the run_script tool to start it."}]},
            config={"configurable": {"thread_id": "master_session_001"}},
        )
        print(response["messages"][-1].content)

if __name__ == "__main__":
    main()