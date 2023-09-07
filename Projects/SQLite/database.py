import sqlite3 #it doesn't need to be installed

# create a connection with database and we create the database
connection_with_db = sqlite3.connect('students.db')

cursor_db = connection_with_db.cursor()  # allow us to iterate  data row-by-row

# create a table
cursor_db.execute("""CREATE TABLE students (
            name TEXT,
            age INTEGER,
            height REAL
    )""")

# populating the table
cursor_db.execute("INSERT INTO students VALUES ('mark', 20, 1.9)")   #adding one row

all_students = [
    ('john', 21, 1.8),
    ('david', 35, 1.7),
    ('michael', 19, 1.83),
]
cursor_db.executemany("INSERT INTO students VALUES (?, ?, ?)", all_students) #adding differents rows a list with tuples

# QUERIES: select data
cursor_db.execute("SELECT * FROM students")
# print(cursor_db.fetchall()) # To view the result on the console
table = cursor_db.fetchall()
for row in table:
    print(row)
# commit: save all the change we have done
connection_with_db.commit()

# close the connection
connection_with_db.close()


# https://inloop.github.io/sqlite-viewer/ to view the .db file