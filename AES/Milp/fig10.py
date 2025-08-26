import matplotlib.pyplot as plt
import numpy as np

# Create the figure
fig, ax = plt.subplots(figsize=(12, 6))

# Data for the comparison
variables = ['v₁,₈', 'v₁,₉', 'P_DG,1,8', 'P_DG,1,9', 'P_dis,1,8', 'P_dis,1,9', 'C₁']
nonconvex_values = [18, 22, 280, 205, 35, 65, 200]
proposed_values = [22, 20, 290, 203, 33, 63, 206]

# Colors
nonconvex_color = '#1f77b4'  # Blue
proposed_color = '#ff7f0e'   # Orange

# Bar positions
x_pos = np.arange(len(variables))
bar_width = 0.35

# Create bars
bars1 = ax.bar(x_pos - bar_width/2, nonconvex_values, bar_width, 
               color=nonconvex_color, edgecolor='black', linewidth=0.8, 
               label='Nonconvex')
bars2 = ax.bar(x_pos + bar_width/2, proposed_values, bar_width, 
               color=proposed_color, edgecolor='black', linewidth=0.8, 
               label='Proposed')

# Add difference annotations
# ΔP = 10.6 (between P_DG,1,8 values)
ax.annotate('ΔP = 10.6', xy=(2.2, 285), fontsize=11, ha='center', va='bottom')

# Δv < 0.4 (between v values)
ax.annotate('Δv < 0.4', xy=(0.8, 30), fontsize=11, ha='center', va='bottom')

# ΔC = 6.1 (between C₁ values)
ax.annotate('ΔC = 6.1', xy=(6.2, 203), fontsize=11, ha='center', va='bottom')

# Customize the plot
ax.set_xlabel('Variables', fontsize=14)
ax.set_ylabel('', fontsize=14)
ax.set_ylim(0, 300)

# Set x-axis
ax.set_xticks(x_pos)
ax.set_xticklabels(variables, fontsize=12)

# Set y-axis ticks
ax.set_yticks(np.arange(0, 301, 50))

# Add legend
ax.legend(loc='upper right', fontsize=11, frameon=True)

# Add grid
ax.grid(True, alpha=0.3, axis='y')

# Add title
ax.set_title('Fig. 10. Comparison of voyage scheduling results of AES 1 in 8:00-9:00 by\nsolving original and reformulated models', 
             fontsize=12, pad=20)

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adjust layout
plt.tight_layout()
plt.show()