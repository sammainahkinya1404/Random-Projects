import matplotlib.pyplot as plt
import numpy as np

# Create figure with 2x2 subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

# Colors for each AES
colors = {
    'AES 1': '#1f77b4',  # Blue
    'AES 2': '#ff7f0e',  # Orange
    'AES 3': '#2ca02c',  # Green
    'AES 4': '#d4af37'   # Gold
}

# Define berth allocation data for each method
# Each entry is (start_time, end_time, berth, aes)

# Method #1 - subplot (a)
method1_data = [
    (10, 12, 1, 'AES 1'),
    (11, 15, 2, 'AES 2'),
    (10, 12, 3, 'AES 4'),
    (12, 15, 3, 'AES 3')
]

# Method #2 - subplot (b)
method2_data = [
    (12, 15, 1, 'AES 2'),
    (10, 11, 3, 'AES 4'),
    (11, 13, 3, 'AES 1'),
    (13, 15, 3, 'AES 3')
]

# Method #3 - subplot (c)
method3_data = [
    (11, 15, 1, 'AES 2'),
    (12, 13.5, 2, 'AES 1'),
    (10, 12, 3, 'AES 4'),
    (12, 15, 3, 'AES 3')
]

# Proposed method - subplot (d)
proposed_data = [
    (11, 15, 1, 'AES 3'),
    (10, 12, 3, 'AES 4'),
    (12, 14, 3, 'AES 2'),
    (14, 15, 3, 'AES 1')
]

def plot_berth_allocation(ax, data, title):
    """Plot berth allocation for one method"""
    
    for start, end, berth, aes in data:
        duration = end - start
        ax.barh(berth, duration, left=start, height=0.6, 
                color=colors[aes], edgecolor='black', linewidth=1.5, alpha=0.8)
    
    # Customize the subplot
    ax.set_xlim(10, 15)
    ax.set_ylim(0.5, 3.5)
    ax.set_xlabel('Time (h)', fontsize=11)
    ax.set_ylabel('Berths', fontsize=11)
    ax.set_title(title, fontsize=11, fontweight='bold')
    
    # Set ticks
    ax.set_xticks([10, 11, 12, 13, 14, 15])
    ax.set_yticks([1, 2, 3])
    
    # Add grid
    ax.grid(True, alpha=0.3, linewidth=0.5)
    ax.set_axisbelow(True)

# Plot each method
plot_berth_allocation(ax1, method1_data, '(a)')
plot_berth_allocation(ax2, method2_data, '(b)')
plot_berth_allocation(ax3, method3_data, '(c)')
plot_berth_allocation(ax4, proposed_data, '(d)')

# Create a shared legend at the top
legend_elements = [plt.Rectangle((0, 0), 1, 1, facecolor=colors[aes], 
                                edgecolor='black', linewidth=1, label=aes) 
                  for aes in ['AES 1', 'AES 2', 'AES 3', 'AES 4']]

fig.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, 0.95), 
          ncol=4, fontsize=11, frameon=True)

# Add main title
fig.suptitle('Fig. 7. Berth allocation results of four AES under different methods: (a)\nMethod #1, (b) Method #2, (c) Method #3, (d) Proposed method', 
             fontsize=12, y=0.02, ha='center')

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(top=0.82, bottom=0.18)
plt.show()