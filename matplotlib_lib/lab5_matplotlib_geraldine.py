# Vancouver February 13, 2025,
# MatplotLib
# Instructor: Derrick
# Student: Geraldine
import matplotlib.pyplot as plt
import numpy as np

# 1. Exercise 1: Basic Line Plot

# Data
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 9, 16, 25, 36]

# Plotting
plt.plot(x, y)

# Labels
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Title
plt.title('First Line Plot')

# Show
plt.show()

# Exercise 2: Customizing Plots

plt.plot(x, y, color='green', linestyle='--', marker='o', markersize=8, markerfacecolor='white')

# Labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

#Title
plt.title('Customized Line Plot')

# Grid
plt.grid(True)

#show
plt.show()

# Exercise 3: Bar Plot

# Data
categories = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
values = [10, 15, 7, 12, 5]

# Plotting
plt.bar(categories, values)

# Labels
plt.xlabel('Categories')
plt.ylabel('Values')

#Title
plt.title('Bar Plot Example')

#show
plt.show()

# Exercise 4: Histogram

# Data
data = np.random.normal(0, 1, 500)

# Plotting
plt.hist(data, bins=25, edgecolor='red')

# Labels
plt.xlabel('Value')
plt.ylabel('Frequency')

#Title
plt.title('Histogram Exercise')

#show
plt.show()

# Exercise 5: Scatter Plot

# Data

x = np.random.rand(50)
y = np.random.rand(50)

# Plotting
plt.scatter(x, y)

# Labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# title
plt.title('Scatter Plot Exercise')

# Show
plt.show()

# Exercise 6: Subplots

# Dataset

# Line Plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Bar Plot
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]

# Histogram
data = np.random.randn(1000)

# Scatter Plot
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
axs[1, 0].hist(data, bins=35, edgecolor='red')
axs[1, 0].set_title('Histogram')

# Scatter Plot
axs[1, 1].scatter(x_scatter, y_scatter)
axs[1, 1].set_title('Scatter Plot')

plt.tight_layout()
plt.show()
