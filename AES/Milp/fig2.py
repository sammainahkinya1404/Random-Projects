import matplotlib.pyplot as plt
import numpy as np

#Changed step size from 1 to 0.1 to match data array lengths
time = np.arange(0, 2.5, 0.1)

# PV data (blue line with diamond markers)
pv_data = [0.02, 0.02, 0.02, 0.04, 0.04, 0.02, 0.22, 0.67, 0.89, 0.63, 0.78, 0.97, 0.93, 1.0, 0.56, 0.54, 0.12, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02]

# Load data (orange line with square markers) 
load_data = [0.75, 0.72, 0.71, 0.70, 0.71, 0.72, 0.78, 0.79, 0.77, 0.79, 0.78, 0.80, 0.85, 0.95, 1.0, 0.92, 0.86, 0.79, 0.78, 0.79]

# Extend load data to match time array length
load_extended = load_data + [0.78] * (len(time) - len(load_data))

# Create the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot PV data on left y-axis
ax1.plot(time, pv_data, 'b-D', linewidth=2, markersize=6, label='PV')
ax1.set_xlabel('Time (h)', fontsize=12)
ax1.set_ylabel('P_PV/P_PV', fontsize=12, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_ylim(0, 1)
ax1.grid(True, alpha=0.3)

# Create second y-axis for Load data
ax2 = ax1.twinx()
# load_data and full time array
ax2.plot(time, load_extended, 'r-s', linewidth=2, markersize=6, label='Load', color='orange')
ax2.set_ylabel('P_LT^max, Q_L/Q_max', fontsize=12, color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
ax2.set_ylim(0.7, 1)

# Set x-axis limits and ticks
ax1.set_xlim(0, 2.5)
# 0.5 for appropriate x-axis tick spacing
ax1.set_xticks(np.arange(0, 2.6, 0.5))

# Add legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# Adjust layout and display
plt.tight_layout()
plt.show()