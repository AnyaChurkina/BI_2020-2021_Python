import sqlite3 as sql


connection = sql.connect('pupils.db')

# create table 'children'
connection.execute('''CREATE TABLE IF NOT EXISTS children
( children_id INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT,
age INTEGER,
sex INTEGER )''')
connection.commit()

# add data to the table 'children'
children = [('Isabella', 'Smith', 15, 1),
            ('Emma', 'Johnson', 17, 1),
            ('Daniel', 'Brown', 15, 0),
            ('Andrew', 'Robinson', 17, 0),
            ('ABKCBINBSU', 'VYTKVLYUV', 1100, 0),
            ('Anna', 'Taylor', 16, 1),
            ('Mia', 'Davis', 17, 1),
            ('Michael', 'Smith', 15, 0),
            ('Ethan', 'Wright', 16, 0)]
query = "INSERT INTO children (first_name, last_name, age, sex) " \
        "VALUES (?, ?, ?, ?)"
connection.executemany(query, children)
connection.commit()

# SELECT
# look at the child with id=5
sql_select_query = """SELECT * FROM children WHERE children_id = 5"""
res = connection.execute(sql_select_query)
for row in res.fetchall():
    print("ID:", row[0])
    print("Name:", row[1])
    print("Surname:", row[2])
    print("Age:", row[3])
    print("Sex:", row[4])

# DELETE
# delete child with id = 5 because it is not a child
sql_delete_query = """DELETE FROM children WHERE children_id = 5"""
connection.execute(sql_delete_query)
connection.commit()

# UPDATE
# update the age of the child with id = 8
sql_update_query = """UPDATE children SET age = 18 WHERE children_id = 8"""
connection.execute(sql_update_query)
connection.commit()

# create table 'parents'
connection.execute('''CREATE TABLE IF NOT EXISTS parents
( parents_id INTEGER PRIMARY KEY,
mother_name TEXT,
father_name TEXT )''')
connection.commit()

# add data to the table 'parents'
parents = [('Agata', 'Tom'),
           ('Alice', 'Noah'),
           ('Gloria', 'Liam'),
           ('Debra', 'Michael'),
           ('Amanda', 'Alexander'),
           ('Barbara', 'Jacob'),
           ('Amelia', 'Harry')]
query = "INSERT INTO parents (mother_name, father_name) " \
        "VALUES (?, ?)"
connection.executemany(query, parents)
connection.commit()

# create table 'schools'
connection.execute('''CREATE TABLE IF NOT EXISTS schools
( school_id INTEGER PRIMARY KEY,
school_number INTEGER,
main_direction TEXT )''')
connection.commit()

# add data to the table 'schools'
schools = [(1677, 'maths'),
           (999, 'biology'),
           (10, 'ballet'),
           (654, 'foreign languages')]
query = "INSERT INTO schools (school_number, main_direction) " \
        "VALUES (?, ?)"
connection.executemany(query, schools)
connection.commit()

# CASCADE
# create table 'pupils'
connection.execute('''CREATE TABLE IF NOT EXISTS pupils
( pupils_id INTEGER PRIMARY KEY,
school_id INTEGER,
children_id INTEGER,
parents_id INTEGER,
FOREIGN KEY (school_id) REFERENCES schools (school_id)
ON DELETE CASCADE,
FOREIGN KEY (children_id) REFERENCES children (children_id)
ON DELETE CASCADE,
FOREIGN KEY (parents_id) REFERENCES parents (parents_id)
ON DELETE CASCADE )''')
connection.commit()

# add data to the table 'pupils'
pupils = [(1, 2, 6),
          (4, 4, 1),
          (2, 9, 5),
          (3, 1, 3),
          (1, 8, 3),
          (2, 3, 7),
          (4, 6, 4),
          (3, 7, 2)]
query = "INSERT INTO pupils (school_id, children_id, parents_id) " \
        "VALUES (?, ?, ?)"
connection.executemany(query, pupils)
connection.commit()

# JOIN
query = '''SELECT school_number, main_direction, first_name, last_name,
age, mother_name, father_name FROM pupils
JOIN schools USING (school_id)
JOIN children USING (children_id)
JOIN parents USING (parents_id)'''
res = connection.execute(query)

# Look at rows
for row in res.fetchall():
    print(row)

# delete 1 school and look at the 'pupils' again
connection.execute("PRAGMA foreign_keys = on")
query = """DELETE FROM schools WHERE school_id = 3"""
connection.execute(query)
connection.commit()

query = '''SELECT school_id, main_direction, first_name, last_name,
age, mother_name, father_name FROM pupils
JOIN schools USING(school_id)
JOIN children USING(children_id)
JOIN parents USING(parents_id)'''
res = connection.execute(query)
for row in res.fetchall():
    print(row)

# there are no rows with school id = 3, DELETE CASCADE works
