# Install matplotlib
# Import matplotlib

import matplotlib.pyplot as plt

year = [2025, 2026, 2027, 2028, 2028, 2029, 2030]
salaries = [46_000, 50_000, 100_000, 200_000, 220_000, 300_000, 400_000]

plt.plot(year, salaries)
plt.xlabel('Year')
plt.ylabel("Salary")
plt.title("My salary is coming")

plt.show()