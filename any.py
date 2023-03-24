import sqlite3

# create connection to database 'demo'
conn = sqlite3.connect('demo.db')

# create table 'table1'
conn.execute('''CREATE TABLE table1
                (name TEXT,
                 id INT)''')

# insert data into table
conn.execute("INSERT INTO table1 (name, id) VALUES ('John', 1)")
conn.execute("INSERT INTO table1 (name, id) VALUES ('Jane', 2)")

# commit changes
conn.commit()

# select and display data from table
cursor = conn.execute("SELECT name, id FROM table1")
print(type(cursor))
for row in cursor:
    print("Name = ", row[0])
    print("ID = ", row[1])

# close connection
conn.close()
