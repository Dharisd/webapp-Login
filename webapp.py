from flask import Flask,request,jsonify,render_template,session,redirect,url_for,abort,flash
import sqlite3
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def get_db():
    db = sqlite3.connect("test.db")
    c = db.cursor()
    return c
def enter_user(user,pwd):
        db = sqlite3.connect("test.db")
        c = db.cursor()
        c.execute("select user from creds where user=?",[user])
        check = c.fetchone()
        print()
        if check == None:
            c.execute("insert into creds (user,pass) values (?,?)",[user,pwd])
            db.commit()
            db.close()
            return("success")
        else:
            return("fail")
    
    
    




@app.route("/", methods=["POST","GET"])
def log():
    if not session.get("logged_in"):
        if request.method == "POST":
            #session["logged_in"] = True
            user = request.form["user"]
            pwd = request.form["pass"]
            if (pwd or  user) != "":
                cs = get_db()
                cs.execute("select pass from creds where user= ?",[user])
                dbpwd = cs.fetchone()
                if (dbpwd != None) and (dbpwd[0]) == pwd:
                    print("login succesfull")
                    print("correct credentials enetred")
                    session["logged_in"]= True
                    return redirect(url_for('control'))
                else:
                    return (redirect(url_for("log",error="incorrect")))
            else:
                print("login failed, incorrect credentials")
                
                return (redirect(url_for("log",error="incorrect")))
    flash("incorrect credentials")
    return render_template("index_material.html")



@app.route("/ctpanel", methods=["GET"])
def control(): 
    print(session.get("logged_in"))                     
    if not session.get("logged_in"):
        abort(401)
    return(render_template("index.html"))


@app.route("/logout", methods=["POST","GET"])
def logout():
    session.pop("logged_in",None)
    return redirect(url_for("log"))

@app.route("/signup", methods=["POST","GET"])
def signup():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pass"]
        print(user)
        print(pwd)
        if user or pwd != "":
            enter= enter_user(user,pwd)
            if enter == "success":
                return jsonify("1")
        else:
            return(render_template("signup.html"))
    return (render_template("signup.html"))



