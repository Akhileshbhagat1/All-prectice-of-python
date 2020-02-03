import cx_Oracle
db = None
try:
    db = cx_Oracle.connect("AK", "ak", "localhost:1521/ORCL")
except(cx_Oracle.DatabaseError):
    print("invalid username/password")
    print(db)
    if db==None:
        print("connection is not established")
    else:
        print("connection is established")
    if db != None:
        db.close()
        print("connection is not established")
        print("end")

