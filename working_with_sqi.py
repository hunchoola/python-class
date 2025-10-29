import sqlite3

conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

# Create a table called students
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS students (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER NOT NULL
# )
# ''')

# # Populate students table
# cursor.execute('''
# INSERT INTO students (name, age)
# VALUES 
#     ('Alice Smith', 22),
#     ('Bob Johnson', 19),
#     ('Charlie Brown', 21),
#     ('Diana Evans', 23),
#     ('Ethan Davis', 20)
# ''')
# conn.commit()
