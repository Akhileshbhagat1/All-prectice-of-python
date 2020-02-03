import cx_Oracle
db = cx_Oracle.connect("AK", "ak", "localhost:1521/ORCL")
print(db)
if db == None :
    print("connection is  not established")
else:
    print("connection is established")
    db.close()
    print(db)
    print("end")
