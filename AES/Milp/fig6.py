import matplotlib.pyplot as plt
import numpy as np

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# Colors for each method
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d4af37']  # Blue, Orange, Green, Gold
methods = ['Method #1', 'Method #2', 'Method #3', 'Proposed']

# Time points for each AES (8, 9, 10, 11 for each AES section)
time_base = np.array([8, 9, 10, 11])

# Bar width and positions
bar_width = 0.2
x_positions = np.arange(len(time_base))

# --- SUBPLOT (a): DSGs Data ---
# AES 1 - DSGs
dsg_aes1_method1 = [120, 110, 120, 110]
dsg_aes1_method2 = [130, 130, 130, 130]
dsg_aes1_method3 = [100, 90, 100, 90]
dsg_aes1_proposed = [90, 80, 90, 80]

# AES 2 - DSGs  
dsg_aes2_method1 = [150, 140, 150, 140]
dsg_aes2_method2 = [160, 160, 160, 160]
dsg_aes2_method3 = [130, 120, 130, 120]
dsg_aes2_proposed = [120, 110, 120, 110]

# AES 3 - DSGs
dsg_aes3_method1 = [140, 130, 140, 130]
dsg_aes3_method2 = [150, 150, 150, 150]
dsg_aes3_method3 = [120, 110, 120, 110]
dsg_aes3_proposed = [110, 100, 110, 100]

# AES 4 - DSGs
dsg_aes4_method1 = [180, 320, 400, 180]
dsg_aes4_method2 = [190, 300, 390, 190]
dsg_aes4_method3 = [170, 310, 380, 170]
dsg_aes4_proposed = [160, 290, 370, 160]

# Plot DSGs data
aes_sections = [
    (dsg_aes1_method1, dsg_aes1_method2, dsg_aes1_method3, dsg_aes1_proposed),
    (dsg_aes2_method1, dsg_aes2_method2, dsg_aes2_method3, dsg_aes2_proposed),
    (dsg_aes3_method1, dsg_aes3_method2, dsg_aes3_method3, dsg_aes3_proposed),
    (dsg_aes4_method1, dsg_aes4_method2, dsg_aes4_method3, dsg_aes4_proposed)
]

for aes_idx, (m1, m2, m3, prop) in enumerate(aes_sections):
    x_offset = aes_idx * 4
    x_pos = x_positions + x_offset
    
    ax1.bar(x_pos - 1.5*bar_width, m1, bar_width, color=colors[0], 
            edgecolor='black', linewidth=0.5, label=methods[0] if aes_idx == 0 else "")
    ax1.bar(x_pos - 0.5*bar_width, m2, bar_width, color=colors[1], 
            edgecolor='black', linewidth=0.5, label=methods[1] if aes_idx == 0 else "")
    ax1.bar(x_pos + 0.5*bar_width, m3, bar_width, color=colors[2], 
            edgecolor='black', linewidth=0.5, label=methods[2] if aes_idx == 0 else "")
    ax1.bar(x_pos + 1.5*bar_width, prop, bar_width, color=colors[3], 
            edgecolor='black', linewidth=0.5, label=methods[3] if aes_idx == 0 else "")

# --- SUBPLOT (b): ESS Data ---
# AES 1 - ESS
ess_aes1_method1 = [32, 35, 30, 40]
ess_aes1_method2 = [15, 18, 12, 25]
ess_aes1_method3 = [10, 12, 8, 20]
ess_aes1_proposed = [8, 10, 6, 18]

# AES 2 - ESS
ess_aes2_method1 = [45, 42, 48, 40]
ess_aes2_method2 = [20, 22, 18, 25]
ess_aes2_method3 = [15, 17, 13, 20]
ess_aes2_proposed = [12, 14, 10, 18]

# AES 3 - ESS  
ess_aes3_method1 = [48, 45, 42, 40]
ess_aes3_method2 = [18, 20, 15, 22]
ess_aes3_method3 = [12, 15, 10, 18]
ess_aes3_proposed = [10, 12, 8, 15]

# AES 4 - ESS
ess_aes4_method1 = [45, 60, 95, 40]
ess_aes4_method2 = [25, 65, 90, 35]
ess_aes4_method3 = [20, 58, 85, 30]
ess_aes4_proposed = [18, 55, 80, 25]

# Plot ESS data
ess_sections = [
    (ess_aes1_method1, ess_aes1_method2, ess_aes1_method3, ess_aes1_proposed),
    (ess_aes2_method1, ess_aes2_method2, ess_aes2_method3, ess_aes2_proposed),
    (ess_aes3_method1, ess_aes3_method2, ess_aes3_method3, ess_aes3_proposed),
    (ess_aes4_method1, ess_aes4_method2, ess_aes4_method3, ess_aes4_proposed)
]

for aes_idx, (m1, m2, m3, prop) in enumerate(ess_sections):
    x_offset = aes_idx * 4
    x_pos = x_positions + x_offset
    
    ax2.bar(x_pos - 1.5*bar_width, m1, bar_width, color=colors[0], 
            edgecolor='black', linewidth=0.5, label=methods[0] if aes_idx == 0 else "")
    ax2.bar(x_pos - 0.5*bar_width, m2, bar_width, color=colors[1], 
            edgecolor='black', linewidth=0.5, label=methods[1] if aes_idx == 0 else "")
    ax2.bar(x_pos + 0.5*bar_width, m3, bar_width, color=colors[2], 
            edgecolor='black', linewidth=0.5, label=methods[2] if aes_idx == 0 else "")
    ax2.bar(x_pos + 1.5*bar_width, prop, bar_width, color=colors[3], 
            edgecolor='black', linewidth=0.5, label=methods[3] if aes_idx == 0 else "")

# Add vertical dashed lines to separate AES sections
for ax in [ax1, ax2]:
    ax.axvline(x=3.5, color='black', linestyle='--', linewidth=1)
    ax.axvline(x=7.5, color='black', linestyle='--', linewidth=1)
    ax.axvline(x=11.5, color='black', linestyle='--', linewidth=1)

# Add AES section labels with arrows
arrow_props = dict(arrowstyle='<->', color='black', lw=1.5)

for ax in [ax1, ax2]:
    # AES labels
    ax.text(1.5, ax.get_ylim()[1]*0.95, 'AES 1', ha='center', fontsize=11, weight='bold')
    ax.text(5.5, ax.get_ylim()[1]*0.95, 'AES 2', ha='center', fontsize=11, weight='bold')
    ax.text(9.5, ax.get_ylim()[1]*0.95, 'AES 3', ha='center', fontsize=11, weight='bold')
    ax.text(13.5, ax.get_ylim()[1]*0.95, 'AES 4', ha='center', fontsize=11, weight='bold')
    
    # Arrows
    y_arrow = ax.get_ylim()[1]*0.88
    ax.annotate('', xy=(3.5, y_arrow), xytext=(-0.5, y_arrow), arrowprops=arrow_props)
    ax.annotate('', xy=(7.5, y_arrow), xytext=(3.5, y_arrow), arrowprops=arrow_props)
    ax.annotate('', xy=(11.5, y_arrow), xytext=(7.5, y_arrow), arrowprops=arrow_props)
    ax.annotate('', xy=(15.5, y_arrow), xytext=(11.5, y_arrow), arrowprops=arrow_props)

# Customize subplot (a) - DSGs
ax1.set_ylabel('P (kW)', fontsize=12)
ax1.set_ylim(0, 400)
ax1.set_xticks(np.arange(16))
ax1.set_xticklabels(['8', '9', '10', '11'] * 4)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, alpha=0.3)
ax1.text(0.02, 0.95, '(a)', transform=ax1.transAxes, fontsize=12, weight='bold')

# Customize subplot (b) - ESS  
ax2.set_xlabel('Time (h)', fontsize=12)
ax2.set_ylabel('P (kW)', fontsize=12)
ax2.set_ylim(0, 100)
ax2.set_xticks(np.arange(16))
ax2.set_xticklabels(['8', '9', '10', '11'] * 4)
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(True, alpha=0.3)
ax2.text(0.02, 0.95, '(b)', transform=ax2.transAxes, fontsize=12, weight='bold')

# Add main title
fig.suptitle('Fig. 6. Generation scheduling of AES during the voyage scheduling under\ndifferent methods: (a) DSGs, (b) ESS', 
             fontsize=12, y=0.02)

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)
plt.show()