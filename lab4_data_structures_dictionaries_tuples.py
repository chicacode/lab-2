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

# Exercise 3: Employee Records

employees = [
("John Doe", "Accounting", "john.doe@example.com"),
("Jane Smith", "Marketing", "jane.smith@example.com"),
("Emily Davis", "HR", "emily.davis@example.com"),
("Michael Brown", "IT", "michael.brown@example.com")
]

# 3.1 Print the names and departments of all employee
print("Employees Name and Departments:")
for name, department, _ in employees:
    print(f"{name} - {department}")

print("\n")
# 3.2 Print the email addresses of all employees in alphabetical order by their last names.
sorted_emails = sorted(employees, key=lambda items: items[0].split()[-1])
for _, _, email in sorted_emails:
    print("Emails: ", email)
# 3.3  Add a new employee ("David Wilson", "Sales", "david.wilson@example.com
# and print the updated list.
employees.append(("David Wilson", "Sales", "david.wilson@example.com"))
print("Updated Employees Record: ")
for name, department, email in employees:
    print(f"{name} - {department} - {email}")

print("\n")
# Find and print the department of "Jane Smith".
jane_department = next((dept for name, dept, _ in employees if name == "Jane Smith"), 'Not Found')
print(f"Jane's Smith department: {jane_department}")

# Exercise 4: Book Library System
library = {
"978-3-16-148410-0": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
"978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949},
"978-0-7432-7356-5": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
"978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
}
# 4.1 Print the details of all books in a user-friendly format

print("Library:")
for isbn, details in library.items():
    print(f"ISBN: {isbn}")
    print(f"Title: {details['title']}")
    print(f"fAuthor: {details['author']}")
    print(f"Year: {details['year']}")
    print()

# 4.2 Find and print the details of the book with the ISBN "978-0-14-028329-7
isbn_find = '978-0-14-028329-7'
if isbn_find in library:
    print(f"Details of the book with ISBN {isbn_find}")
    print(f"Title: {library[isbn_find]['title']}")
    print(f"fAuthor: {library[isbn_find]['author']}")
    print(f"Year: {library[isbn_find]['year']}")
else:
    print(f"Book with ISBN {isbn_find} not found in library")
# 4.3 Add a new book with ISBN "978-1-4028-9462-6", title "The Great Gatsby
# author "F. Scott Fitzgerald", and year 1925.

new_book = {
"978-1-4028-9462-6": {
    "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925 }
}
library.update(new_book)
print("Book added successfully")
# 4.4 Update the year of "To Kill a Mockingbird" to 1961 and print the updated
# details.
isbn_update = '978-0-7432-7356-5'
if isbn_update in library:
    library[isbn_update]['year'] = 1961
    print(f"Year updated successfully. Updated details:")
    print(f"Title: {library[isbn_update]['title']}")
    print(f"fAuthor: {library[isbn_update]['author']}")
    print(f"Year: {library[isbn_update]['year']}")
else:
    print(f"Book with ISBN {isbn_update} not found in library")
# 4.5 Remove the book with ISBN "978-0-452-28423-4" and print the u
# library.

isbn_remove = '978-0-452-28423-4'
if isbn_remove in library:
    del library[isbn_remove]
    print(f"Book with ISBN {isbn_remove} removed successfully.")
else:
    print(f"Book with ISBN {isbn_remove} not found in library.")

print("\n")
# Exercise 5: City Population Data
cities = {
"New York": 8419000,
"Los Angeles": 3980000,
"Chicago": 2716000,
"Houston": 2328000,
"Phoenix": 1690000
}

# 5.1 Print the population of each city in a user-friendly format
print("Population Data:")
for city, population in cities.items():
    print(f"{city}: {population} people")
print("\n")
# 5.2 Find and print the city with the highest population
highest_population = max(cities, key=cities.get)
print(f"City with the highest population: {highest_population} ({cities[highest_population]} people)")
# 5.3 Find and print the city with the lowest population
lowest_population = min(cities, key=cities.get)
print(f"City with the lowest population: {lowest_population} ({cities[lowest_population]} people)")
print("\n")
# 5.4 Update the population of "Phoenix" to 1700000 and print the updated data

cities['Phoenix'] = 1700000
print("Updated population:")
print(f"Phoenix: {cities['Phoenix']} people")
# 5.5 Add a new city "San Francisco" with a population of 884000 and print t
# updated data.

cities['San Francisco'] = 884000
print("New city added: San Francisco")
print("\nUpdated City Population Data:")
for city, population in cities.items():
    print(f"{city}: {population} people")
print("\n")
# Exercise 6: Movie Database
movies = {
"Inception": {"year": 2010, "rating": 8.8, "genre": "Sci-Fi"},
"The Godfather": {"year": 1972, "rating": 9.2, "genre": "Crime"},
"The Dark Knight": {"year": 2008, "rating": 9.0, "genre": "Action"},
"Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"},
"Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"}
}

# 6.2 Print the details of all movies in a user-friendly format
print("Movies Details:")
for title, details in movies.items():
    print(f"Title: {title}")
    print(f"Year: {details['year']}")
    print(f"Rating: {details['genre']}")
    print(f"Genre: {details['genre']}")
    print("-")

# 6.3 Find and print the highest-rated movie
top_rated_movie = max(movies, key=lambda movie: movies[movie]['rating'])
print(f"Highest rated movie: {top_rated_movie} ({movies[top_rated_movie]['rating']}")

# 6.4 Add a new movie "The Matrix" with year 1999, rating 8.7, and genre "Sci-Fi"
# the database.
movies['The Matrix'] = {
    'year': 1999,
    'rating': 8.7,
    'genre': 'Sci-Fi'
}
print(f"Added new movie, my favorite: The Matrix")

# 6.5 Update the rating of "Inception" to 9.0 and print the updated details
movies['Inception']['rating'] = 9.0
print("Updating rating")
print(f"Title: Inception, Year: {movies['Inception']['year']}, Rating: {movies['Inception']['rating']}, Genre: {movies['Inception']['genre']}, ")
print("\n")
# Remove "Pulp Fiction" from the database and print the updated list
if 'Pulp Fiction' in movies:
    del movies['Pulp Fiction']
    print(f"Removed 'Pulp Fiction' from dictionary")

print('\n')
for title, details in movies.items():
    print(f"Title: {title}, Year: {details['year']}, Rating: {details['rating']}, Genre: {details['genre']}")
print('\n')

# Exercise 7: Country Capitals

countries = {
"USA": "Washington, D.C.",
"Canada": "Ottawa",
"France": "Paris",
"Germany": "Berlin",
"Japan": "Tokyo"
}

# 7.1 Print the names of all countries and their capitals
print("Print countries and capitals")
for country, capital in countries.items():
    print(f" {country}: {capital}")
print('\n')
# 7.2 Find and print the capital of Germany
germany_capital = countries.get("Germany", "Not found")
print(f" Capital of Germany: {germany_capital}")
print('\n')

# 7.3 Add a new country "Australia" with capital "Canberra" to the dictionary a
# print the updated dictionary.
countries['Australia'] = 'Canberra'
print("Updated Dictionary")
for country, capital in countries.items():
    print(f" {country}: {capital}")
print('\n')

# 7.4 Update the capital of "USA" to "New Washington" and print the update
# dictionary.
countries['USA'] = "New Washington"
print("Updated Dictionary: USA capital")

for country, capital in countries.items():
    print(f" {country}: {capital}")
print('\n')

# 7.5 Remove "France" from the dictionary and print the updated dictionary

if "France" in countries:
    del countries["France"]
    print("Removed France from the dictionary.")
print('\n')
# Exercise 8: Shopping Cart

cart = [
{"item": "apple", "quantity": 3, "price_per_unit": 0.5},
{"item": "banana", "quantity": 6, "price_per_unit": 0.2},
{"item": "orange", "quantity": 4, "price_per_unit": 0.3},
{"item": "pear", "quantity": 2, "price_per_unit": 0.4}
]
# 8.1 Print the details of all items in the cart
print("Shopping cart details:")
for item in cart:
    print(f" Item: {item['item']}, Quantity: {item['quantity']}, Price per Unit; ${item['price_per_unit']}")

# 8.2 Calculate and print the total cost of the cart
total = sum(item['quantity'] * item['price_per_unit'] for item in cart)
print(f"Total cost of the cart: ${total:.2f}")
print('\n')
# 8.3 Add a new item "grape" with quantity 5 and price per unit 0.6 to the cart

cart.append({"item": "grape", "quantity": 5, "price_per_unit": 0.6})
print("Added 'Grape' into the car")
for item in cart:
    print(f" Item: {item['item']}, Quantity: {item['quantity']}, Price per Unit; ${item['price_per_unit']}")
print('\n')
# 8.4 Update the quantity of "banana" to 10 and print the updated cart
for item in cart:
    if item['item'] == 'banana':
        item['quantity'] = 10
        break
print("Added 'Banana' quantity in the car")
print('\n')
for item in cart:
    print(f" Item: {item['item']}, Quantity: {item['quantity']}, Price per Unit; ${item['price_per_unit']}")
print('\n')

# 8.5 Remove "pear" from the cart and print the updated cart
cart = [item for item in cart if item["item"] != "pear"]
print("Removed 'pear from cart")
print("Updated cart: ")
for item in cart:
    print(f" Item: {item['item']}, Quantity: {item['quantity']}, Price per Unit; ${item['price_per_unit']}")
print('\n')