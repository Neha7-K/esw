import matplotlib.pyplot as plt

# Data
days = list(range(1, 9))  # Adjusted to match the length of the other lists
leaf_temperature = [25.5, 26.4, 27.5, 27.3, 24.2, 28, 27.2, 25.7]
soil_moisture = [13.4, 16.6, 14.1, 17.2, 15.8, 12.9, 17.2, 14.6]
ph = [6.08, 5.92, 5.76, 5.60, 5.5, 5.44, 5.23, 5.12]

# Plotting
plt.figure(figsize=(12, 8))

# Line styles and colors
line_styles = ['-', '--', '-.']
colors = ['#1f77b4', '#2ca02c', '#d62728']

# Plot each factor
for i, (factor, style, color) in enumerate(zip([leaf_temperature, soil_moisture, ph], line_styles, colors)):
    plt.plot(days, factor, marker='o', linestyle=style, color=color, linewidth=2, markersize=10, label=f'Factor {i + 1}')

# Adding labels and title
plt.xlabel('Days', fontsize=14)
plt.ylabel('Values', fontsize=14)
plt.title('Comparative Analysis of Environmental Factors', fontsize=16)
plt.legend(fontsize=12)

# Adding grid
plt.grid(True, linestyle='--', alpha=0.6)

# Customize tick parameters
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Display the plot
plt.show()
