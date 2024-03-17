import sqlite3

# connect to the database
conn = sqlite3.connect('example.db')

# create a cursor object
cursor = conn.cursor()

# create a table
cursor.execute('''CREATE TABLE users
                  (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# insert data into the table
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('John', 'john@example.com'))

# commit the changes
conn.commit()

# fetch data from the table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# close the database connection
conn.close()