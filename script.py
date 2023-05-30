import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Specify the table name
table_name = 'myapp_Agenda'

# Retrieve the column names
cursor.execute(f"PRAGMA table_info({table_name})")
columns = cursor.fetchall()

# Print the column names
for column in columns:
    print(column[1])  # Column name is in the second position

# Close the database connection
conn.close()
