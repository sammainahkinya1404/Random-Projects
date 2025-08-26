import matplotlib.pyplot as plt
import numpy as np

# Create figure with 2x2 subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

# Define colors for each AES
colors = {'AES1': '#1f77b4', 'AES2': '#ff7f0e', 'AES3': '#2ca02c', 'AES4': '#ffb347'}

# Data for each subplot (berth, start_time, end_time, aes_type)
# Subplot (a) - Method #1
data_a = [
    (1, 19, 23, 'AES2'),
    (2, 18.5, 22.5, 'AES3'),
    (3, 18, 19, 'AES1'),
    (3, 20, 23, 'AES4')
]

# Subplot (b) - Method #2  
data_b = [
    (1, 18, 21.5, 'AES2'),
    (1, 21.5, 23, 'AES1'),
    (3, 18, 21, 'AES4'),
    (3, 21, 23, 'AES3')
]

# Subplot (c) - Method #3
data_c = [
    (1, 20.5, 21.5, 'AES1'),
    (2, 20, 22, 'AES2'),
    (3, 18, 20, 'AES4'),
    (3, 21.5, 22.5, 'AES3')
]

# Subplot (d) - Proposed method
data_d = [
    (1, 19, 23, 'AES2'),
    (3, 18, 20.5, 'AES4'),
    (3, 20.5, 22, 'AES3'),
    (3, 22, 23, 'AES1')
]

def plot_berth_allocation(ax, data, title):
    """Plot berth allocation for given data"""
    for berth, start, end, aes in data:
        ax.barh(berth, end - start, left=start, height=0.6, 
               color=colors[aes], alpha=0.8, edgecolor='black', linewidth=0.5)
    
    # Set labels and title
    ax.set_xlabel('Time (h)', fontsize=11)
    ax.set_ylabel('Berths', fontsize=11)
    ax.set_title(f'({title})', fontsize=11, loc='center', y=-0.15)
    
    # Set axis limits and ticks
    ax.set_xlim(17.5, 23.5)
    ax.set_ylim(0.5, 3.5)
    ax.set_xticks(range(18, 24))
    ax.set_yticks([1, 2, 3])
    
    # Add grid
    ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    ax.set_axisbelow(True)
    
    # Invert y-axis to match the original plots
    ax.invert_yaxis()

# Plot each subplot
plot_berth_allocation(ax1, data_a, 'a')
plot_berth_allocation(ax2, data_b, 'b')
plot_berth_allocation(ax3, data_c, 'c')
plot_berth_allocation(ax4, data_d, 'd')

# Create legend
legend_elements = [plt.Rectangle((0,0),1,1, facecolor=colors['AES1'], label='AES1'),
                  plt.Rectangle((0,0),1,1, facecolor=colors['AES2'], label='AES2'),
                  plt.Rectangle((0,0),1,1, facecolor=colors['AES3'], label='AES3'),
                  plt.Rectangle((0,0),1,1, facecolor=colors['AES4'], label='AES4')]

# Add legend at the top
fig.legend(handles=legend_elements, loc='upper center', ncol=4, 
          bbox_to_anchor=(0.5, 0.98), frameon=True, fancybox=True, shadow=True)

# Add main title
fig.suptitle('Fig. 11. Berth allocation of AES under different methods with arrival times\nbetween 18:00 and 20:00: (a) Method #1, (b) Method #2, (c) Method #3, (d)\nProposed method', 
             fontsize=12, y=0.08)

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(top=0.85, bottom=0.25, hspace=0.3, wspace=0.3)

plt.show()