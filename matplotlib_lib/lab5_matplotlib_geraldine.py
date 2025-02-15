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

# Exercise 7: Pie Chart

# Data

categories = ['Marketing', 'Development', 'Sales', 'Support']
values = [20, 35, 25, 20]

# Pie Chart
plt.figure(figsize=(7,7))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140, colors=['yellow', 'purple', 'orange', 'blue'])

# Title
plt.title('Departments')

# Legend
plt.legend(categories, loc="best")

# Show
plt.show()

# Exercise 8: Stacked Bar Plot

# Data

categories = ['Group 1', 'Group 2', 'Group 3']
value1 = [5, 7, 3]
value2 = [6, 8, 4]
value3 = [4, 3, 5]

x = np.arange(len(categories))

# Plotting
plt.bar(x, value1, label='Value 1', color='red')
plt.bar(x, value2, bottom=value1, label='Value 2', color='black')
plt.bar(x, value3, bottom=np.array(value1) + np.array(value2), label='Value 3', color='grey')

# Labels
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Stacked Bar Chart")

# Add category names on x-axis
plt.xticks(x, categories)

# Legend
plt.legend()

# Show
plt.show()

# Exercise 9: Box Plot

# Data
dataset1 = np.random.normal(60, 10, 100)

dataset2 = np.random.normal(70, 15, 100)

dataset3 = np.random.normal(80, 5, 100)

# Plotting
plt.boxplot([dataset1, dataset2, dataset3], label=['Dataset 1', 'Dataset 2', 'Dataset 3'])

# Labels
plt.ylabel('Values')

# Title
plt.title('Box Plot each dataset')

# Show
plt.show()

# Exercise 10: Line Plot with Annotations

# Dataset
x = range(0, 20)
y = [value ** 2 for value in x]

# Plot
plt.plot(x, y, marker='o', linestyle='-', color='b')

# Highest and Lowest Points

plt.annotate('Lowest', (x[0], y[0]), textcoords='offset points', xytext=(-10,10), ha='center', arrowprops=dict(arrowstyle='->'))
plt.annotate('Highest', (x[1], y[-1]), textcoords='offset points', xytext=(-10,10), ha='center', arrowprops=dict(arrowstyle='->'))

# Labels
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Line Plot with Annotations")

# show
plt.show()