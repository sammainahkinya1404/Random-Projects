import matplotlib.pyplot as plt
import numpy as np

# Create figure with 2 subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Time data
time = np.arange(0, 25, 1)

# --- SUBPLOT (a): Box plots for all buses with proposed method ---
# Generate sample data for box plots (representing voltage distribution across all buses)
np.random.seed(42)  # For reproducibility

box_data = []
outliers_x = []
outliers_y = []

for t in time:
    if t < 8:
        # Low variability period
        data = np.random.normal(0.99, 0.008, 50)
        # Add some outliers
        if t == 1:
            outliers_x.extend([t] * 2)
            outliers_y.extend([1.005, 0.995])
    elif 8 <= t <= 16:
        # High variability period (daytime)
        if t == 9:
            data = np.random.normal(1.005, 0.012, 50)
            outliers_x.extend([t] * 3)
            outliers_y.extend([1.05, 1.03, 0.97])
        elif t == 10:
            data = np.random.normal(1.01, 0.015, 50)
            outliers_x.extend([t] * 2)
            outliers_y.extend([1.05, 0.97])
        elif 11 <= t <= 15:
            data = np.random.normal(1.00, 0.015, 50)
            if t in [12, 14, 15]:
                outliers_x.extend([t] * 2)
                outliers_y.extend([1.025, 0.97])
        else:
            data = np.random.normal(0.99, 0.010, 50)
    else:
        # Return to low variability
        data = np.random.normal(0.99, 0.008, 50)
    
    box_data.append(data)

# Create box plot
bp = ax1.boxplot(box_data, positions=time, widths=0.6, patch_artist=True,
                 boxprops=dict(facecolor='lightblue', alpha=0.7),
                 medianprops=dict(color='red', linewidth=1.5),
                 whiskerprops=dict(color='black', linewidth=1),
                 capprops=dict(color='black', linewidth=1),
                 flierprops=dict(marker='o', markerfacecolor='red', markersize=4, alpha=0.7))

# Add manual outliers
ax1.scatter(outliers_x, outliers_y, color='red', marker='+', s=50, zorder=10)

# Customize subplot (a)
ax1.set_xlim(0, 25)
ax1.set_ylim(0.95, 1.05)
ax1.set_xlabel('Time (h)', fontsize=12)
ax1.set_ylabel('V (p.u.)', fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.text(0.02, 0.95, '(a)', transform=ax1.transAxes, fontsize=12, weight='bold')
ax1.set_xticks(np.arange(0, 26, 5))

# --- SUBPLOT (b): Line plots for minimum voltage at bus 15 ---
# Colors for each method
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d4af37']  # Blue, Orange, Green, Gold
methods = ['Method #1', 'Method #2', 'Method #3', 'Proposed']

# Sample data for minimum voltage profiles
method1_voltage = [0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 
                   1.005, 1.01, 0.955, 0.97, 0.98, 1.035, 1.04, 1.01, 
                   1.00, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99]

method2_voltage = [0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99,
                   0.98, 0.975, 0.96, 0.985, 1.01, 0.97, 0.975, 0.99,
                   0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99]

method3_voltage = [0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99,
                   0.965, 1.035, 0.955, 0.965, 0.98, 1.03, 1.00, 0.995,
                   0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99]

proposed_voltage = [0.99, 0.99, 0.985, 0.98, 0.98, 0.99, 0.99, 0.99,
                    1.025, 1.03, 0.97, 0.975, 0.98, 1.005, 1.01, 0.98,
                    0.98, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99]

# Plot voltage profiles
ax2.plot(time, method1_voltage, color=colors[0], linewidth=2, label=methods[0])
ax2.plot(time, method2_voltage, color=colors[1], linewidth=2, label=methods[1])
ax2.plot(time, method3_voltage, color=colors[2], linewidth=2, label=methods[2])
ax2.plot(time, proposed_voltage, color=colors[3], linewidth=2, label=methods[3])

# Customize subplot (b)
ax2.set_xlim(0, 25)
ax2.set_ylim(0.95, 1.05)
ax2.set_xlabel('Time (h)', fontsize=12)
ax2.set_ylabel('V (p.u.)', fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.legend(loc='upper right', fontsize=10)
ax2.text(0.02, 0.95, '(b)', transform=ax2.transAxes, fontsize=12, weight='bold')
ax2.set_xticks(np.arange(0, 26, 5))

# Add main title
fig.suptitle('Fig. 8. Voltage profiles in seaport microgrids under different methods: (a)\nVoltage of all buses with the proposed method, (b) Minimum voltage at bus\n15 under different methods', 
             fontsize=12, y=0.02, ha='center')

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(bottom=0.20)
plt.show()