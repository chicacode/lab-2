# Vancouver February 11, 2025,
# Data Structures
# Instructor: Derrick
# Student: Geraldine

#Exercise 1: Student Grades Analysis

students = {
"Alice": [85, 78, 92],
"Bob": [79, 74, 81],
"Charlie": [91, 82, 85],
"David": [76, 85, 83],
"Eve": [88, 79, 92]
}

# 1.1 Calculate and print the average score for each student
averages = {}
for name, scores in students.items():
    avg_score = sum(scores) / len(scores)
    averages[name] = avg_score
    print(f"{name}'s average score: {avg_score:.2f}")

# 1.2 Find and print the name of the student with the highest average score
print("\n")
best_student = max(averages, key=averages.get)
print(f"Student with highest average score is: {best_student} ({averages[best_student]:.2f})")
print("\n")
# 1.3 Find and print the name of the student with the lowest average score
print("\n")
worst_student = min(averages, key=averages.get)
print(f"Student with worst average score is: {worst_student} ({averages[worst_student]:.2f})")

# 1.4 Add a new student "Frank" with scores [80, 90, 85] to the dictionary and p
# the updated dictionary.
print("\n")
students['Frank'] = [80, 90, 85]
print("Student record: ")
print("\n")
for name, scores in students.items():
    print(f"{name}: scores: {scores}")

# Exercise 2: Product Inventory Management

inventory = {
"apple": (50, 0.5),
"banana": (100, 0.2),
"orange": (75, 0.3),
"pear": (20, 0.4)
}

# 2.1 Print the current inventory in a user-friendly format
print("\n")
print(f"Current inventory:")
for product, (quantity, price) in inventory.items():
    print(f"{product.capitalize()}: Quantity = {quantity}, Price = ${price:.2f}")

# 2.2 Calculate and print the total value of the inventory

total: float = sum(quantity * price for (quantity, price) in inventory.values())
print(f"\n Total Inventory values: {total:.2f}")

# 2.3 Add a new product "mango" with 30 items priced at $0.6 each to t
# inventory.

inventory['mango'] = (30, 0.6)
print("\n")
# 2.4 Update the quantity of "banana" to 120 and print the updated inventory
inventory['banana'] = (120, inventory['banana'][1])

# 2.5 Remove "pear" from the inventory and print the updated inventory
inventory.pop('pear')

print("\n Updated Inventory:")
for product, (quantity, price) in inventory.items():
    print(f"{product.capitalize()}: Quantity = {quantity}, Price = ${price:.2f}")
print("\n")