import matplotlib.pyplot as plt
import numpy as np

# Create the figure
fig, ax = plt.subplots(figsize=(14, 6))

# Time data for each AES section (8-11 hours for each)
time_aes1 = np.array([8, 9, 10, 11])
time_aes2 = np.array([8, 9, 10, 11])  
time_aes3 = np.array([8, 9, 10, 11])
time_aes4 = np.array([8, 9, 10, 11])

# Velocity data for each method in each AES
# AES 1
method1_aes1 = np.array([17, 17, 17, 17])
method2_aes1 = np.array([10, 10.5, 0, 10])
method3_aes1 = np.array([7.5, 7, 8, 10])
proposed_aes1 = np.array([7.5, 7, 9.5, 10.5])

# AES 2  
method1_aes2 = np.array([17, 17, 17, 17])
method2_aes2 = np.array([10, 10.5, 0, 10])
method3_aes2 = np.array([7.5, 7.5, 7, 8.5])
proposed_aes2 = np.array([7.5, 7.5, 10.5, 0])

# AES 3
method1_aes3 = np.array([17, 17, 17, 17])
method2_aes3 = np.array([10, 10.5, 0, 10])
method3_aes3 = np.array([8, 7.5, 7, 9])
proposed_aes3 = np.array([7.5, 7, 7.5, 8])

# AES 4
method1_aes4 = np.array([10.5, 10.5, 10.5, 0])
method2_aes4 = np.array([16, 15.5, 0, 0])
method3_aes4 = np.array([16, 15, 0, 0])
proposed_aes4 = np.array([10.5, 10.5, 0, 0])

# Colors for each method
colors = {
    'method1': '#1f77b4',    # Blue
    'method2': '#ff7f0e',    # Orange  
    'method3': '#2ca02c',    # Green
    'proposed': '#d4af37'    # Gold
}

# Line styles
linestyles = {
    'method1': '-',
    'method2': '-', 
    'method3': '-',
    'proposed': '-'
}

# Plot data for each AES
# AES 1
ax.plot(time_aes1, method1_aes1, color=colors['method1'], linestyle=linestyles['method1'], 
        linewidth=2, label='Method #1')
ax.plot(time_aes1, method2_aes1, color=colors['method2'], linestyle=linestyles['method2'], 
        linewidth=2, label='Method #2')  
ax.plot(time_aes1, method3_aes1, color=colors['method3'], linestyle=linestyles['method3'], 
        linewidth=2, label='Method #3')
ax.plot(time_aes1, proposed_aes1, color=colors['proposed'], linestyle=linestyles['proposed'], 
        linewidth=2, label='Proposed')

# AES 2 (offset by 3 hours for display)
time_offset_2 = time_aes2 + 3
ax.plot(time_offset_2, method1_aes2, color=colors['method1'], linestyle=linestyles['method1'], 
        linewidth=2)
ax.plot(time_offset_2, method2_aes2, color=colors['method2'], linestyle=linestyles['method2'], 
        linewidth=2)
ax.plot(time_offset_2, method3_aes2, color=colors['method3'], linestyle=linestyles['method3'], 
        linewidth=2)
ax.plot(time_offset_2, proposed_aes2, color=colors['proposed'], linestyle=linestyles['proposed'], 
        linewidth=2)

# AES 3 (offset by 6 hours)  
time_offset_3 = time_aes3 + 6
ax.plot(time_offset_3, method1_aes3, color=colors['method1'], linestyle=linestyles['method1'], 
        linewidth=2)
ax.plot(time_offset_3, method2_aes3, color=colors['method2'], linestyle=linestyles['method2'], 
        linewidth=2)
ax.plot(time_offset_3, method3_aes3, color=colors['method3'], linestyle=linestyles['method3'], 
        linewidth=2)
ax.plot(time_offset_3, proposed_aes3, color=colors['proposed'], linestyle=linestyles['proposed'], 
        linewidth=2)

# AES 4 (offset by 9 hours)
time_offset_4 = time_aes4 + 9  
ax.plot(time_offset_4, method1_aes4, color=colors['method1'], linestyle=linestyles['method1'], 
        linewidth=2)
ax.plot(time_offset_4, method2_aes4, color=colors['method2'], linestyle=linestyles['method2'], 
        linewidth=2)
ax.plot(time_offset_4, method3_aes4, color=colors['method3'], linestyle=linestyles['method3'], 
        linewidth=2)
ax.plot(time_offset_4, proposed_aes4, color=colors['proposed'], linestyle=linestyles['proposed'], 
        linewidth=2)

# Add vertical dashed lines to separate AES sections
ax.axvline(x=11, color='black', linestyle='--', linewidth=1)
ax.axvline(x=14, color='black', linestyle='--', linewidth=1) 
ax.axvline(x=17, color='black', linestyle='--', linewidth=1)

# Add AES section labels with arrows
arrow_props = dict(arrowstyle='<->', color='black', lw=1.5)
ax.annotate('AES 1', xy=(9.5, 19), ha='center', fontsize=12, weight='bold')
ax.annotate('AES 2', xy=(12.5, 19), ha='center', fontsize=12, weight='bold')
ax.annotate('AES 3', xy=(15.5, 19), ha='center', fontsize=12, weight='bold')
ax.annotate('AES 4', xy=(18.5, 19), ha='center', fontsize=12, weight='bold')

# Add horizontal arrows for AES sections
ax.annotate('', xy=(11, 18.5), xytext=(8, 18.5), arrowprops=arrow_props)
ax.annotate('', xy=(14, 18.5), xytext=(11, 18.5), arrowprops=arrow_props)
ax.annotate('', xy=(17, 18.5), xytext=(14, 18.5), arrowprops=arrow_props)
ax.annotate('', xy=(20, 18.5), xytext=(17, 18.5), arrowprops=arrow_props)

# Customize the plot
ax.set_xlabel('Time (h)', fontsize=14)
ax.set_ylabel('Velocity (knots)', fontsize=14)

# Set axis limits
ax.set_xlim(8, 20)
ax.set_ylim(0, 20)

# Set x-axis ticks to show the pattern for each AES
ax.set_xticks([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
ax.set_xticklabels(['8', '9', '10', '11', '8', '9', '10', '11', '8', '9', '10', '11'])

# Add legend
ax.legend(loc='upper left', fontsize=11)

# Add grid
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()