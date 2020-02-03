import cx_Oracle
db = cx_Oracle.connect('Ak','ak',"localhost:1521/ORCL")
print("connection")
db.close()
print("close")

