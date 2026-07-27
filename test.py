import sqlite3

# Create a connection (this creates the file if it doesn't exist)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER
    )
''')

# Insert sample data
cursor.executemany('''
    INSERT INTO users (name, email, age) VALUES (?, ?, ?)
''', [
    ('Alice Wonderland', 'alice@example.com', 28),
    ('Bob Builder', 'bob@example.com', 42),
    ('Charlie Brown', 'charlie@example.com', 22)
])

# Commit changes and close
conn.commit()
conn.close()

print("Database 'test.db' created successfully!")