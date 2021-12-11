import sqlite3

conn = sqlite3.connect('zoo_db')
curs = conn.cursor()
statement1 = '''
SELECT animal, cost, count FROM zoo
'''

statement2 = '''
SELECT * FROM zoo
'''

try:
    curs.execute(statement2)
    rows = curs.fetchall()
except Exception as e:
    print("There was a problem: {}".format(e))
finally:
    conn.close()  # always make sure the connection is closed

for row in rows:
    print("Animal: {0} costs {1} each and there are {2} of them.".format(row[0], row[2], row[1]))
