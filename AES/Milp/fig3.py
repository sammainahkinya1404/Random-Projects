import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
time_points = [10, 11, 12]
x_labels = ['10', '11', '12']

# SOC_a values for each AES at each time point
aes1_values = [0.1, 0.1, 0.42]
aes2_values = [0.1, 0.17, 0.58]
aes3_values = [0.1, 0.17, 0.58]
aes4_values = [0.1, 0.36, 0.65]

# SI values (shown as text on bars)
si_values = [
    [0, 1, 0.89],    # AES1
    [0, 1, 0.53],    # AES2
    [0, 1, 0.53],    # AES3
    [0.5, 1, 0]      # AES4
]

# Set up the figure
fig, ax = plt.subplots(figsize=(10, 6))

# Bar width and positions
bar_width = 0.18
x_pos = np.arange(len(time_points))

# Colors for each AES
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Blue, Orange, Green, Red
labels = ['AES 1', 'AES 2', 'AES 3', 'AES 4']

# Create bars for each AES
bars1 = ax.bar(x_pos - 1.5*bar_width, aes1_values, bar_width, 
               label=labels[0], color=colors[0], edgecolor='black', linewidth=1)
bars2 = ax.bar(x_pos - 0.5*bar_width, aes2_values, bar_width, 
               label=labels[1], color=colors[1], edgecolor='black', linewidth=1)
bars3 = ax.bar(x_pos + 0.5*bar_width, aes3_values, bar_width, 
               label=labels[2], color=colors[2], edgecolor='black', linewidth=1)
bars4 = ax.bar(x_pos + 1.5*bar_width, aes4_values, bar_width, 
               label=labels[3], color=colors[3], edgecolor='black', linewidth=1)

# Add SI values as text on bars
all_bars = [bars1, bars2, bars3, bars4]
for i, bars in enumerate(all_bars):
    for j, bar in enumerate(bars):
        height = bar.get_height()
        if height > 0:  # Only add text if bar has height
            ax.text(bar.get_x() + bar.get_width()/2., height/2, 
                   f'{si_values[i][j]}', ha='center', va='center', 
                   fontweight='bold', fontsize=10)

# Customize the plot
ax.set_xlabel('T_a (h)', fontsize=14)
ax.set_ylabel('SOC_a', fontsize=14)
ax.set_title('Fig. 3. T_a-SOC_a pairs and corresponding SI values for all AES', 
             fontsize=12, pad=20)

# Set x-axis
ax.set_xticks(x_pos)
ax.set_xticklabels(x_labels)
ax.set_xlim(-0.6, 2.6)

# Set y-axis
ax.set_ylim(0, 0.8)
ax.set_yticks(np.arange(0, 0.81, 0.2))

# Add legend
ax.legend(loc='upper left', fontsize=10)

# Add grid
ax.grid(True, alpha=0.3, axis='y')

# Adjust layout
plt.tight_layout()
plt.show()