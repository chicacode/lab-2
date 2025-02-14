# Import matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Exercise 1: Basic Line Plot
# Data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
# Plotting
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

# Exercise 2: Customizing Plots
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
# Plotting
plt.plot(x, y, color='green', linestyle='--', marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Line Plot')
plt.grid(True)
plt.show()

# Exercise 3: Bar Plot

categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]
# Plotting
plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')
plt.show()

# Exercise 4: Histogram
data = np.random.randn(1000)

# Plotting
plt.hist(data, bins=30, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()

# Exercise 5: Scatter Plot
