from flask import  Flask, render_template, request, redirect
import mysql.connector

conn = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "flaskdb")

cuser = conn.cursor()


app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/about")
def aboutus():
    return render_template("about.html")

@app.route("/contact")
def contactus():
    return render_template("myhtml/contact.html")

@app.route("/services")
def servicespage():
    cuser.execute("select * from flasksave")
    data = cuser.fetchall()

    return render_template("myhtml/services.html", mydata = data)

@app.route("/savethisdata", methods = ["post"])
def savethisdata(): 
    if request.method == "POST":
        mytitle = request.form.get("title")
        message = request.form.get("msg")

        cuser.execute(f"insert into flasksave values('{mytitle}', '{message}')")
        conn.commit()

        return redirect("/contact")

    return "your data saved sucessfulyyy......!"


@app.route("/deletethisdata/<x>", methods = ["POST"])
def deletethisdata(x):
    cuser.execute(f"delete from flasksave where  title='{x}'")
    return "data deleteeeeeeee"



if __name__ == "__main__":
    app.run(debug = True)

# oRM: sqlalchemy