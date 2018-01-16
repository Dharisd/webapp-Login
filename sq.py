import sqlite3

db = sqlite3.connect("test.db")

cs = db.cursor()
cs.execute("select user, pass from creds")
row = cs.fetchall()

array =[]
for i in range(0,len(row)):
    print(str(row[i]))
    array.append(row[i])

cs.execute("select pass from creds where user="+ "'dharis'")
pas = cs.fetchone()
print(pas[0])



db.close()
