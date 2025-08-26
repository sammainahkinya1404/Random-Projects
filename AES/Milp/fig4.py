import matplotlib.pyplot as plt
import numpy as np

# Create the figure
fig, ax = plt.subplots(figsize=(12, 6))

# Define beta_k positions
beta_positions = [0, 0.25, 0.5, 0.75, 1.0]

# Define colors for each AES
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d4af37']  # Blue, Orange, Green, Gold
aes_labels = ['AES 1', 'AES 2', 'AES 3', 'AES 4']

# Bar width for the horizontal bars
bar_width = 0.015
bar_height = 0.03

# Data for each beta_k position - showing which AES systems have acceptable arrival times
# at specific time points (10.1, 11.1, 12.0 approximately)

# Beta_k = 0: All AES systems active at multiple times
for j, color in enumerate(colors):
    # Time around 10.1
    ax.barh(10.1, bar_width, height=bar_height, left=0-bar_width/2, 
           color=color, edgecolor='black', linewidth=0.5, alpha=0.8)
    # Time around 11.1  
    ax.barh(11.1, bar_width, height=bar_height, left=0-bar_width/2, 
           color=color, edgecolor='black', linewidth=0.5, alpha=0.8)
    # Time around 12.0
    ax.barh(12.0, bar_width, height=bar_height, left=0-bar_width/2, 
           color=color, edgecolor='black', linewidth=0.5, alpha=0.8)

# Beta_k = 0.25: Fewer systems, mostly at 11.1 and 12.0
for j, color in enumerate(colors[:3]):  # Only first 3 AES
    ax.barh(11.1, bar_width, height=bar_height, left=0.25-bar_width/2, 
           color=color, edgecolor='black', linewidth=0.5, alpha=0.8)
    ax.barh(12.0, bar_width, height=bar_height, left=0.25-bar_width/2, 
           color=color, edgecolor='black', linewidth=0.5, alpha=0.8)
# AES 4 only at 10.1
ax.barh(10.1, bar_width, height=bar_height, left=0.25-bar_width/2, 
       color=colors[3], edgecolor='black', linewidth=0.5, alpha=0.8)

# Beta_k = 0.5: Similar pattern
for j, color in enumerate(colors[:3]):  # Only first 3 AES
    ax.barh(11.1, bar_width, height=bar_height, left=0.5-bar_width/2, 
           color=color, edgecolor='black', linewidth=0.5, alpha=0.8)
    ax.barh(12.0, bar_width, height=bar_height, left=0.5-bar_width/2, 
           color=color, edgecolor='black', linewidth=0.5, alpha=0.8)
# AES 4 only at 10.1
ax.barh(10.1, bar_width, height=bar_height, left=0.5-bar_width/2, 
       color=colors[3], edgecolor='black', linewidth=0.5, alpha=0.8)

# Beta_k = 0.75: Only first 3 AES systems
for j, color in enumerate(colors[:3]):  
    ax.barh(11.1, bar_width, height=bar_height, left=0.75-bar_width/2, 
           color=color, edgecolor='black', linewidth=0.5, alpha=0.8)
    ax.barh(12.0, bar_width, height=bar_height, left=0.75-bar_width/2, 
           color=color, edgecolor='black', linewidth=0.5, alpha=0.8)

# Beta_k = 1.0: Only AES 1 (blue)
ax.barh(12.0, bar_width, height=bar_height, left=1.0-bar_width/2, 
       color=colors[0], edgecolor='black', linewidth=0.5, alpha=0.8)

# Customize the plot
ax.set_xlabel('β_k', fontsize=14)
ax.set_ylabel('T_a (h)', fontsize=14) 
ax.set_title('Fig. 4. Sensitivity analysis of acceptable vessel arrival times to β_k', 
             fontsize=12, pad=20)

# Set axis limits and ticks
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(9.9, 12.3)

# X-axis ticks
ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
ax.set_xticklabels(['0', '0.25', '0.5', '0.75', '1'])

# Y-axis ticks  
ax.set_yticks([10, 11, 12])
ax.set_yticklabels(['10', '11', '12'])

# Create legend
from matplotlib.patches import Rectangle
legend_elements = []
for i, (aes, color) in enumerate(zip(aes_labels, colors)):
    legend_elements.append(Rectangle((0, 0), 1, 1, facecolor=color, 
                                   edgecolor='black', linewidth=0.5, label=aes))

ax.legend(handles=legend_elements, loc='upper right', fontsize=11,
         bbox_to_anchor=(1.0, 1.0))

# Add subtle grid
ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)

# Clean up spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()