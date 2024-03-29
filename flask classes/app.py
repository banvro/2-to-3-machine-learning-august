from flask import  Flask, render_template

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
    return render_template("myhtml/services.html")


if __name__ == "__main__":
    app.run(debug = True)