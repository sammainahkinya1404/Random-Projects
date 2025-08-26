import matplotlib.pyplot as plt
import numpy as np

# Create figure with 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 12))

# Time data
time = np.arange(0, 25, 1)

# Colors for each method
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d4af37']  # Blue, Orange, Green, Gold
methods = ['Method #1', 'Method #2', 'Method #3', 'Proposed']

# --- SUBPLOT (a): OLTC Tap positions ---
# Create step-like data for tap positions
method1_tap = np.zeros(25)
method1_tap[10:20] = 2
method1_tap[20:] = 1

method2_tap = np.zeros(25)
method2_tap[4:8] = -1
method2_tap[10:] = 0

method3_tap = np.zeros(25)
method3_tap[15:] = 2

proposed_tap = np.zeros(25)
proposed_tap[4:8] = -1
proposed_tap[20:] = -1

# Plot tap positions with step plots
ax1.step(time, method1_tap, where='post', color=colors[0], linewidth=2, label=methods[0])
ax1.step(time, method2_tap, where='post', color=colors[1], linewidth=2, label=methods[1])
ax1.step(time, method3_tap, where='post', color=colors[2], linewidth=2, label=methods[2])
ax1.step(time, proposed_tap, where='post', color=colors[3], linewidth=2, label=methods[3])

# Customize subplot (a)
ax1.set_xlim(0, 25)
ax1.set_ylim(-2, 2)
ax1.set_ylabel('Tap', fontsize=12)
ax1.set_yticks([-1, 0, 1, 2])
ax1.grid(True, alpha=0.3)
ax1.legend(loc='upper right', fontsize=10)
ax1.text(0.02, 0.9, '(a)', transform=ax1.transAxes, fontsize=12, weight='bold')
ax1.set_xticks(np.arange(0, 26, 5))

# --- SUBPLOT (b): Reactive power of PV 4 ---
# Create reactive power data with annotations
method1_q = np.full(25, 8.0)
method1_q[10:12] = [5, 0]
method1_q[12:15] = [-5, -10, -15]

method2_q = np.full(25, 8.0)
method2_q[10:13] = [0, -5, -10]

method3_q = np.full(25, 8.0)
method3_q[9:14] = [15, 25, 20, 10, 5]

proposed_q = np.full(25, 8.0)
proposed_q[9:14] = [10, 8, 12, 15, 10]

# Plot reactive power
ax2.plot(time, method1_q, color=colors[0], linewidth=2, label=methods[0])
ax2.plot(time, method2_q, color=colors[1], linewidth=2, label=methods[1])
ax2.plot(time, method3_q, color=colors[2], linewidth=2, label=methods[2])
ax2.plot(time, proposed_q, color=colors[3], linewidth=2, label=methods[3])

# Add annotations
ax2.annotate('Provide extra Q to mitigate\nvoltage drop', 
             xy=(11, 20), xytext=(16, 22),
             arrowprops=dict(arrowstyle='->', color='black', lw=1),
             fontsize=10, ha='center')

ax2.annotate('Absorb Q to reduce voltages', 
             xy=(12.5, -10), xytext=(16, -8),
             arrowprops=dict(arrowstyle='->', color='black', lw=1),
             fontsize=10, ha='center')

# Customize subplot (b)
ax2.set_xlim(0, 25)
ax2.set_ylim(-15, 30)
ax2.set_ylabel('Q (kVar)', fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.legend(loc='upper left', fontsize=10)
ax2.text(0.02, 0.9, '(b)', transform=ax2.transAxes, fontsize=12, weight='bold')
ax2.set_xticks(np.arange(0, 26, 5))

# --- SUBPLOT (c): Charging power of AES ---
# Create charging power profiles
method1_power = np.zeros(25)
method1_power[10:17] = [0, 50, 150, 200, 180, 100, 0]

method2_power = np.zeros(25)
method2_power[9:16] = [50, 120, 180, 160, 140, 80, 20]

method3_power = np.zeros(25)
method3_power[10:17] = [100, 200, 260, 200, 160, 80, 0]

proposed_power = np.zeros(25)
proposed_power[9:17] = [80, 160, 200, 180, 190, 160, 100, 20]

# Plot charging power
ax3.plot(time, method1_power, color=colors[0], linewidth=2, label=methods[0])
ax3.plot(time, method2_power, color=colors[1], linewidth=2, label=methods[1])
ax3.plot(time, method3_power, color=colors[2], linewidth=2, label=methods[2])
ax3.plot(time, proposed_power, color=colors[3], linewidth=2, label=methods[3])

# Add annotation
ax3.annotate('Trade-off between Method\n#1 and Method #2', 
             xy=(13, 180), xytext=(18, 220),
             arrowprops=dict(arrowstyle='->', color='black', lw=1),
             fontsize=10, ha='center')

# Customize subplot (c)
ax3.set_xlim(0, 25)
ax3.set_ylim(0, 300)
ax3.set_xlabel('Time (h)', fontsize=12)
ax3.set_ylabel('P (kW)', fontsize=12)
ax3.grid(True, alpha=0.3)
ax3.legend(loc='upper left', fontsize=10)
ax3.text(0.02, 0.9, '(c)', transform=ax3.transAxes, fontsize=12, weight='bold')
ax3.set_xticks(np.arange(0, 26, 5))

# Add main title
fig.suptitle('Fig. 9. Dispatch of OLTC, PVs and AES in seaport microgrids under different\nmethods: (a) OLTC, (b) Reactive power of PV 4, (c) Charging power of AES', 
             fontsize=12, y=0.02, ha='center')

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(bottom=0.15)
plt.show()