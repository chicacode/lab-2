import psycopg2
import csv

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

# Created a table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);
""")
conn.commit()
print("✅ Table created!")

import csv
# Imported CSV data
with open('students.csv', 'r') as f:
    next(f)  # Skip header
    reader = csv.reader(f)
    for row in reader:
        cur.execute("""
        INSERT INTO students (id, name, age)
        VALUES (%s, %s, %s)
        ON CONFLICT (id) DO NOTHING;
        """, row)
        conn.commit()

print("✅ CSV data imported!")

# Queried the database
cur.execute("SELECT * FROM students;")
rows = cur.fetchall()

for row in rows:
    print(row)

# Close connection
cur.close()
conn.close()
print("✅ Connection closed.")


