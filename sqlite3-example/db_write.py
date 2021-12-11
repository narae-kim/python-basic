import sqlite3

conn = sqlite3.connect('zoo_db')
curs = conn.cursor()
statement = '''
INSERT INTO zoo
VALUES ("Rabbit", 100, 0.79)
'''

try:
    curs.execute(statement)
    conn.commit()
except Exception as e:
    print("There was a problem: {}".format(e))
finally:
    conn.close()  # always make sure the connection is closed
