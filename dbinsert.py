import sqlite3
db = sqlite3.connect("test.db")
c = db.cursor()
class loginapp():
    def __init__(self):
        self.logged = 0
    def signup():
        print("_"* 50)
        user = input("enter the name for your user: ")
        pwd = input("enter password for the user: ")
        if ((user or pwd) != ""):
            db.execute('insert into creds (user,pass) values (?,?)',[user,pwd]) 
            db.commit()
            print("succes")
    

    def login(self):
        print("_"* 50)
        user = input("enter  your username : ")
        pwd = input("enter your password: ")
        if (pwd or  user) != "":
            c.execute("select pass from creds where user= ?",[user])
            dbpwd = c.fetchone()
            if (dbpwd != None) and (dbpwd[0]) == pwd:
                print("login succesfull")
                print("correct credentials enetred")
                self.logged = 1
            else:
                print("login failed, incorrect credentials")


    def show(self):
        if self.logged == 1:

            c.execute("select user, pass from creds")
            row = c.fetchall()

            array =[]
            for i in range(0,len(row)):
                print(str(row[i]))

x = loginapp()
x.login()
x.show()