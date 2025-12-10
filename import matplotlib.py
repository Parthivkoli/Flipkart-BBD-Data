import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
visits_cr = [0.1, 5, 15, 25, 40, 55, 66.6, 85, 110, 140, 150, 175]
sales_cr = [0, 2000, 5000, 9000, 15000, 22000, 30000, 38000, 45000, 50000, 55000, 65000]

# Flipkart Orange
flipkart_orange = '#FF6B35'
dark_blue = '#1E3A8A'

# Create figure with dual axes
fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar chart - Total Visits (Left Axis)
bars = ax1.bar(years, visits_cr, color=flipkart_orange, alpha=0.8, width=0.6, label='Total Visits (Cr)')

# Left axis formatting
ax1.set_xlabel('Year', fontsize=14, fontweight='bold')
ax1.set_ylabel('Total Visits (Crores)', fontsize=14, fontweight='bold', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.grid(axis='y', alpha=0.3)

# Line chart - Sales (Right Axis)
ax2 = ax1.twinx()
line = ax2.plot(years, sales_cr, color=dark_blue, linewidth=4, marker='o', markersize=10, 
                markerfacecolor=flipkart_orange, markeredgecolor=dark_blue, markeredgewidth=2, label='Sales (₹ Cr)')

# Right axis formatting
ax2.set_ylabel('Sales Revenue (₹ Crore)', fontsize=14, fontweight='bold', color=dark_blue)
ax2.tick_params(axis='y', labelcolor=dark_blue)
ax2.grid(axis='y', alpha=0.3)

# 2025 Projection - Dotted line
ax2.plot(['2024', '2025'], [55000, 65000], color=dark_blue, linewidth=4, linestyle='--', alpha=0.7)

# **CRITICAL: PERFECT Day-1 2024 Callout**
# Position ABOVE 2024 bar (x=10, y=160, arrow to bar top at y=150)
ax1.annotate('⭐ DAY-1\n33 Cr Visits\n(22% of Total)', 
             xy=(10, 150),  # Points to EXACT 2024 bar top
             xytext=(9.5, 165),  # Positioned ABOVE bar
             fontsize=12, fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.4", facecolor=flipkart_orange, alpha=0.9, edgecolor='white'),
             arrowprops=dict(arrowstyle='->', color='white', lw=2),
             ha='center', va='bottom',
             color='white')

# Title and Subtitle
plt.title('Figure 14: Complete BBD Evolution Timeline\nVisits vs Revenue (2014-2025)', 
          fontsize=18, fontweight='bold', pad=20)
plt.suptitle('1,750x Growth: 0.1 Cr → 175 Cr Visits | ₹0 → ₹65,000 Cr Sales\nDay-1 2024 (33 Cr) = 2020 Entire Event', 
             fontsize=12, color='gray', y=0.95)

# Legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# Architectural Annotations (Clean)
annotations = {
    '2014': 'Monolith\n+Outage',
    '2018': 'Walmart\n+Cloud', 
    '2020': 'Hybrid\nCloud',
    '2023': 'K8s\nMicroservices',
    '2024': 'AI\nScaling'
}

for i, (year, text) in enumerate(annotations.items()):
    y_offset = 20 if year == '2020' else 10
    ax1.text(
        years.index(year),
        visits_cr[years.index(year)] + y_offset,
        text,
        ha='center',
        va='bottom',
        fontsize=9,
        fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.2", facecolor='white', alpha=0.8)
    )

# Styling
plt.tight_layout()
plt.xticks(rotation=45)
ax1.set_ylim(0, 185)
ax2.set_ylim(0, 70000)

# Save high-quality image
plt.savefig('bbd_evolution_perfect.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.show()
