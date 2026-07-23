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
        
        subprocess.run(["uv", "run", str(script_path)],env=env, check=True)
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

menu_mapping = """
  - Percentages (percentage.py)
  - Ratios & Proportions (ratio.py)
  - Basic Fractions (fraction.py)
  - Adding & Subtracting Fractions (fraction_add_sub.py)
  - Multiplying & Dividing Fractions (fraction_muli_div.py)
  - Rectangles and Squares Area and Perimeter (area_perimeter_rectangle.py)
  - Circles Area and Perimeter (area_perimeter_circle.py)
  - Parallelograms Area and Perimeter (area_perimeter_parallelogram.py)
  - Triangles Area and Perimeter (area_perimeter_triangle.py)
  - Trapezoids Area and Perimeter (area_perimeter_trapezoid.py)
  - Volume of different shapes (volume.py)
  - Decimals Basic Concept (fraction_to_decimal.py)
  - Decimals Adding & Subtracting (decimal_add_sub.py)
  - Decimals Multiplication & Division (decimal_mult_div.py)
  - Equation Basic Concept (elementary_algebra.py)
  - Simple Equation (simple_equation.py)
  - Equation Addition and Subtraction (Equation Arithmetic) (equation_arithmetic_operations.py)
  - Negative Numbers (negative_number_arithmetic.py)
  - Speed (speed.py)
  - Statistics (statistics_tutor.py)
  - Pythagorean (Triangle Hypotenuse) (pythagorean.py)
"""

def main():
   
    print("Welcome to the Hong Kong AI Math Tutor!")
    

    while True:
        print("\n==================================================")
        print("I can help you with:")
        print(menu_mapping.strip())
        print("==================================================")

        user_input = input("\n What topic would you like to learn today? (or 'quit'): ")
        
        if user_input.lower() in ['quit', 'exit']:
            print("Class dismissed! See you next time.")
            break
            
        prompt_content = (
            f"Here is the list of available topics and their corresponding Python files:\n"
            f"{menu_mapping}\n\n"
            f"The student wants to learn: '{user_input}'. "
            f"Please identify the correct file from the list above and use the run_script tool to start it."
        )

        response = agent.invoke(
            {"messages": [{"role": "user", "content": prompt_content}]},
            config={"configurable": {"thread_id": "master_session_001"}},
        )
        print(response["messages"][-1].content)

if __name__ == "__main__":
    main()