import statistics as stats

import numpy as np
import multiprocessing


def generate_graph(data: list, title: str = "Dataset Visualization") -> str:
    """
    Generates and displays a horizontal Box Plot for a dataset, 
    highlighting Min, Q1, Median, Q3, Max, and Interquartile Range (IQR).
    
    Args:
        data: The list of numbers from the dataset.
        title: A title for the graph.
    """

    import matplotlib.pyplot as plt
    
    try:
        fig, ax = plt.subplots(figsize=(10, 5))
            
        box = ax.boxplot(
            data, 
            vert=False,
            patch_artist=True,
            boxprops=dict(facecolor='#E8D8C8', color='black', linewidth=2),
            medianprops=dict(color='red', linewidth=3),
            whiskerprops=dict(color='black', linewidth=2),
            capprops=dict(color='green', linewidth=3),
            flierprops=dict(marker='o', color='red', alpha=0.5)
        )

        d_min = float(np.min(data))
        d_max = float(np.max(data))
        q1 = float(np.percentile(data, 25))
        median = float(np.median(data))
        q3 = float(np.percentile(data, 75))
        iqr = q3 - q1

        y_label_pos = 1.28
        ax.text(d_min, y_label_pos, f"Min\n{d_min:g}", horizontalalignment='center', color='green', fontweight='bold')
        ax.text(q1, y_label_pos, f"Q1\n{q1:g}", horizontalalignment='center', color='blue', fontweight='bold')
        ax.text(median, y_label_pos, f"Median\n{median:g}", horizontalalignment='center', color='red', fontweight='bold')
        ax.text(q3, y_label_pos, f"Q3\n{q3:g}", horizontalalignment='center', color='darkorange', fontweight='bold')
        ax.text(d_max, y_label_pos, f"Max\n{d_max:g}", horizontalalignment='center', color='green', fontweight='bold')

        ax.text(
                (q1 + q3) / 2, 0.62, 
                f"Interquartile Range (IQR) = Q3 - Q1 = iqr", 
                horizontalalignment='center', 
                color='purple', fontsize=11, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.4", fc="#F0E6FF", ec="purple", lw=1.5)
        )

        ax.set_title(title, fontsize=14, fontweight='bold', pad=25)
        ax.set_xlabel("Values", fontsize=12)
        ax.set_yticks([])
        ax.set_ylim(0.4, 1.5)

        plt.tight_layout()
        print("\n[System: Box plot window opened. Close the window to continue...]")
        plt.show() 
        return "Success: The box plot graph has been displayed to the student."
    except Exception as e:
        return f"Error displaying graph: {e}"

def safe_generate_graph(data: list, title: str = "Dataset Visualization") -> str:
    """
    Safely runs generate_graph in a separate process to avoid Matplotlib thread/GUI errors.
    Use this tool when the student agrees to see a visual graph of their dataset.
    
    Args:
        data: The list of numbers from the dataset.
        title: A title for the graph.
    """
    try:
        process = multiprocessing.Process(target=generate_graph, args=(data, title))
        process.start()
        process.join()
        return "Success: The graph window was opened and closed cleanly."
    except Exception as e:
        return f"Error executing graph process: {e}"
