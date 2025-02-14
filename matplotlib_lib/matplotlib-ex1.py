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
# Data
x = np.random.rand(50)
y = np.random.rand(50)
# Plotting
plt.scatter(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')
plt.show()

# Exercise 6: Subplots
# Data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]
data = np.random.randn(1000)
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

# Plotting
fig, axs = plt.subplots(2, 2)
# Line Plot
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Line Plot')
# Bar Plot
axs[0, 1].bar(categories, values)
axs[0, 1].set_title('Bar Plot')
# Histogram
axs[1, 0].hist(data, bins=30, edgecolor='black')
axs[1, 0].set_title('Histogram')
# Scatter Plot
axs[1, 1].scatter(x_scatter, y_scatter)
axs[1, 1].set_title('Scatter Plot')
plt.tight_layout()
plt.show()