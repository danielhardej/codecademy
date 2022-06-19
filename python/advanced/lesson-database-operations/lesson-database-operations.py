from start import helper
helper()
import sqlite3

# connect a new SQL db
con = sqlite3.connect("titanic.db")
# create a cursor for the db
curs = con.cursor

# Create table named new_table
curs.execute('''CREATE TABLE new_table (
                   name TEXT,
                   age INTEGER,
                   username TEXT,
                   pay_rate REAL)''')

# Insert row of values into new_table
curs.execute('''INSERT INTO new_table VALUES ('Bob Peterson', 34, 'bob1234', 40.00)''')

# Here is the new_rows object of a tuple list with multiple rows of data that you will insert into new_table
new_rows = [('Anne Smith', 33, 'AS896', 25.00),
            ('Billy Roberts', 29, 'bill5Rob', 30.00),
            ('Jason Johnson', 48, 'JasonJ77', 40.00),
            ('Tim Trunk', 51, 'Timtrunk4', 40.00),
            ('Sarah Fall',19, 'SFall232', 25.00)
            ]

# Insert new_rows into the new_table table
curs.executemany('''INSERT INTO new_table VALUES (?,?,?,?)''', new_rows)
