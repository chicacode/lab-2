import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname='test_db',
    user='postgres',
    password='admin',
    host='localhost',
    port='5432'
)

cur = conn.cursor()
print("✅ Connected to the database!")

# Create new table

cur.execute("""
CREATE TABLE IF NOT EXISTS test (
    id SERIAL PRIMARY KEY,
    num INTEGER,
    data VARCHAR(100)
);
""")
conn.commit()
print("✅ Table created!")

# Insert Data

cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
conn.commit()
print("✅ Data inserted!")

# Query data with Python
cur.execute("SELECT * FROM test;")
rows = cur.fetchall()

for row in rows:
    print(row)

# Create Table
cur.execute("""
CREATE TABLE IF NOT EXISTS departments (
    id SERIAL PRIMARY KEY,  -- Auto-incrementing ID
    name TEXT NOT NULL
);
""")
conn.commit()
print("✅ Table 'departments' created!")


# Insert Data
cur.execute("INSERT INTO departments (name) VALUES (%s)", ('HR',))
cur.execute("INSERT INTO departments (name) VALUES (%s)", ('Engineering',))
cur.execute("INSERT INTO departments (name) VALUES (%s)", ('Marketing',))
conn.commit()
print("✅ Data inserted into 'departments'!")

# Fetch data
cur.execute("SELECT * FROM departments;")
departments = cur.fetchall()

for dept in departments:
    print(dept)


cur.execute("SELECT * FROM employees;")
employees = cur.fetchall()

cur.execute("SELECT * FROM departments;")
departments = cur.fetchall()

print("📌 Employees:")
for emp in employees:
    print(emp)

print("\n📌 Departments:")
for dept in departments:
    print(dept)

# Update employees table
cur.execute("UPDATE employees SET age = %s WHERE name = %s", (32, 'Alice'))
conn.commit()
print("✅ Employee age updated!")

cur.execute("DELETE FROM employees WHERE name = %s", ('Charlie',))
conn.commit()
print("✅ Employee deleted!")


#cur.close()
#conn.close()
#print("✅ Connection closed.")

