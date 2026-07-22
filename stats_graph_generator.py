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

def generate_sd_graph(data: list, title: str = "Standard Deviation Bell Curve") -> str:
    """
        Generates and displays a Standard Deviation Bell Curve matching empirical 
            rule distribution proportions (34.1%, 13.6%, 2.1%, 0.1%).
            
            Args:
                data: The list of numbers from the dataset.
                title: A title for the graph.
    """
    import matplotlib.pyplot as plt

    try:
        fig, ax = plt.subplots(figsize=(10, 5.5))
        mean_val = float(stats.mean(data))
        sd_val = float(stats.stdev(data))

        x = np.linspace(mean_val - 3.5 * sd_val, mean_val + 3.5 * sd_val, 1000)
        y = (1 / (sd_val * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean_val) / sd_val) ** 2)

        ax.plot(x, y, color='black', linewidth=1.5, zorder=3)

        c_inner = '#004C87'
        c_mid   = '#2B8CBE'
        c_outer = '#7BCCC4'
        c_tail  = '#BDD7E7'

        ax.fill_between(x, y, where=(x < mean_val - 3 * sd_val).tolist(), color=c_tail)
        ax.fill_between(x, y, where=(x > mean_val + 3 * sd_val).tolist(), color=c_tail)

        ax.fill_between(x, y, where=((x >= mean_val - 3 * sd_val) & (x < mean_val - 2 * sd_val)).tolist(), color=c_outer)
        ax.fill_between(x, y, where=((x > mean_val + 2 * sd_val) & (x <= mean_val + 3 * sd_val)).tolist(), color=c_outer)

        ax.fill_between(x, y, where=((x >= mean_val - 2 * sd_val) & (x < mean_val - 1 * sd_val)).tolist(), color=c_mid)
        ax.fill_between(x, y, where=((x > mean_val + 1 * sd_val) & (x <= mean_val + 2 * sd_val)).tolist(), color=c_mid)

        ax.fill_between(x, y, where=((x >= mean_val - 1 * sd_val) & (x <= mean_val + 1 * sd_val)).tolist(), color=c_inner)

        sd_offsets = [-2, -1, 0, 1, 2]
        for offset in sd_offsets:
            x_pos = mean_val + offset * sd_val
            y_max_at_x = (1 / (sd_val * np.sqrt(2 * np.pi))) * np.exp(-0.5 * (offset ** 2))
            ax.vlines(x=x_pos, ymin=0, ymax=y_max_at_x, color='white', linewidth=1.8, zorder=4)

        max_y = 1 / (sd_val * np.sqrt(2 * np.pi))

        ax.text(mean_val - 0.5 * sd_val, max_y * 0.45, "34.1%", color='white', fontsize=12, fontweight='bold', ha='center', zorder=5)
        ax.text(mean_val + 0.5 * sd_val, max_y * 0.45, "34.1%", color='white', fontsize=12, fontweight='bold', ha='center', zorder=5)

        ax.text(mean_val - 1.5 * sd_val, max_y * 0.20, "13.6%", color='white', fontsize=11, fontweight='bold', ha='center', zorder=5)
        ax.text(mean_val + 1.5 * sd_val, max_y * 0.20, "13.6%", color='white', fontsize=11, fontweight='bold', ha='center', zorder=5)

        ax.text(mean_val - 2.5 * sd_val, max_y * 0.12, "2.1%", color='black', fontsize=10, fontweight='bold', ha='center', zorder=5)
        ax.text(mean_val + 2.5 * sd_val, max_y * 0.12, "2.1%", color='black', fontsize=10, fontweight='bold', ha='center', zorder=5)

        ax.text(mean_val - 3.2 * sd_val, max_y * 0.08, "0.1%", color='black', fontsize=9, ha='center', zorder=5)
        ax.text(mean_val + 3.2 * sd_val, max_y * 0.08, "0.1%", color='black', fontsize=9, ha='center', zorder=5)

        ticks = [mean_val + i * sd_val for i in range(-3, 4)]
        tick_labels = [
            f"{ticks[0]:.1f}\n(-3σ)",
            f"{ticks[1]:.1f}\n(-2σ)",
            f"{ticks[2]:.1f}\n(-1σ)",
            f"{ticks[3]:.1f}\n(0)",
            f"{ticks[4]:.1f}\n(1σ)",
            f"{ticks[5]:.1f}\n(2σ)",
            f"{ticks[6]:.1f}\n(3σ)"
        ]
        ax.set_xticks(ticks)
        ax.set_xticklabels(tick_labels, fontsize=10)

        ax.set_yticks([])

        ax.set_title(f"{title}\nMean (μ) = {mean_val:.2f} | SD (σ) = {sd_val:.2f}", fontsize=13, fontweight='bold', pad=15)
        ax.set_ylim(bottom=0, top=max_y * 1.1)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        plt.tight_layout()
        print("\n[System: Standard Deviation Bell Curve window opened. Close the window to continue...]")
        plt.show()
        return "Success: The standard deviation bell curve graph has been displayed to the student."

    except Exception as e:
            return f"Error displaying standard deviation graph: {e}"


def safe_generate_graph(data: list, title: str = "Dataset Visualization", graph_type: str = "box") -> str:
    """
    Safely runs generate_graph in a separate process to avoid Matplotlib thread/GUI errors.
    Supports both Box Plot ('box') and Standard Deviation ('sd') plots.
    
    Args:
        data: The list of numbers from the dataset.
        title: A title for the graph.
        graph_type: Type of graph to generate - 'box' for Box Plot / IQR, 'sd' for Standard Deviation.
    """
    try:
        if str(graph_type).lower() in ["sd", "standard deviation", "stdev", "variance"]:
            target_graph = generate_sd_graph
        else:
            target_graph = generate_graph

        process = multiprocessing.Process(target=target_graph, args=(data, title))
        process.start()
        process.join()
        return "Success: The graph window was opened and closed cleanly."
    except Exception as e:
        return f"Error executing graph process: {e}"
