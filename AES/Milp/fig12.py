import matplotlib.pyplot as plt
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(10, 6))

# Define time points (0 to 25 hours)
time = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

# Define voltage data for each method (approximate values from the plot)
method1_voltage = np.array([0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 1.025, 1.025, 1.025, 1.015, 1.025, 1.025, 1.025, 1.035, 1.035, 1.02, 0.95, 0.92, 0.945, 0.93, 0.95, 0.95, 0.99, 0.99])

method2_voltage = np.array([0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 1.005, 1.02, 1.018, 1.025, 1.03, 1.035, 1.035, 1.035, 1.02, 0.95, 0.95, 0.95, 0.95, 0.99, 0.99])

method3_voltage = np.array([0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 1.005, 1.015, 1.018, 1.025, 1.035, 1.035, 1.005, 1.035, 1.035, 0.95, 0.95, 0.95, 0.95, 0.99, 0.99])

proposed_voltage = np.array([0.985, 0.985, 0.985, 0.985, 0.985, 0.98, 0.98, 0.98, 0.98, 1.025, 1.025, 1.01, 1.025, 1.025, 1.025, 1.025, 1.025, 1.025, 1.025, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.99])

# Plot the lines
ax.plot(time, method1_voltage, color='blue', linewidth=2, label='Method #1')
ax.plot(time, method2_voltage, color='red', linewidth=2, label='Method #2') 
ax.plot(time, method3_voltage, color='green', linewidth=2, label='Method #3')
ax.plot(time, proposed_voltage, color='orange', linewidth=2, label='Proposed')

# Add horizontal dashed line at 0.95
ax.axhline(y=0.95, color='black', linestyle='--', linewidth=1.5)

# Set axis labels
ax.set_xlabel('Time (h)', fontsize=14)
ax.set_ylabel('V (p.u.)', fontsize=14)

# Set axis limits
ax.set_xlim(0, 25)
ax.set_ylim(0.92, 1.04)

# Set tick marks
ax.set_xticks([0, 5, 10, 15, 20, 25])
ax.set_yticks([0.92, 0.94, 0.96, 0.98, 1.00, 1.02, 1.04])

# Add grid
ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)

# Add legend
ax.legend(loc='lower left', fontsize=12, frameon=True, fancybox=True, shadow=True)

# Set title
plt.figtext(0.5, 0.02, 'Fig. 12. Minimum voltages at bus 15 under different methods with AES\narrival times between 18:00 and 20:00', 
           ha='center', fontsize=12)

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(bottom=0.15)

# Set background color to white
ax.set_facecolor('white')
fig.patch.set_facecolor('white')

plt.show()