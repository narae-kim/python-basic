# DB2
# import DB2
# conn = DB2.connect(dsn='ibm-DB', uid='analyst', pwd='db2pwd')

# Sybase
# import Sybase
# conn = Sybase.connect('SYBASE', 'username', 'passwd', 'databasename')

# Oracle
# import cx_Oracle
# conn = cx_Oracle.connect('username', 'passwd', 'hostname:port/SID')
# conn2 = cx_Oracle.connect('username/passwd@hostname:portno/SID')
# dsn_tns = cx_Oracle.makedsn('hostname', portno, 'SID')
# conn3 = cx_Oracle.connect('username', 'passwd', dsn_tns)

# MySQL
# import MySQLdb
# conn = MySQLdb.connect(host = "hostname", user = "username",
# passwd = "password", db = "dbname")

# PySQLite
# from pysqlite2 import dbapi2 as sqlite
# conn = sqlite.connect("mydb", connectionproperties)

# ODBC
# import odbc
# conn = odbc. odbc("myDSN/username/password")


import sqlite3  # built-in database that comes with Python

# create the database if not exist
conn = sqlite3.connect('zoo_db')

# access members of the db
curs = conn.cursor()

# zoo database
# create name       string of up to 32 characters
# count             integer
# maintenance cost  float
statement = '''CREATE TABLE zoo 
(animal VARCHAR(32) PRIMARY KEY,
 count INT,
 cost FLOAT
 )'''

# execute the statement
curs.execute(statement)

# commit and close the connection
conn.commit()  # without commit the changes will not persist in the db
conn.close()

# CRUD opearations: Create, Read, Update, Delete (archiving is better idea than deleting)
