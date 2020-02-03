import cx_Oracle
conn = cx_Oracle.connect("AK", "ak", "localhost:1521/ORCL")
cursor = conn.cursor()
cursor.execute('select * from test')
for row in cursor:
    print(row)
cursor.close()
conn.close()