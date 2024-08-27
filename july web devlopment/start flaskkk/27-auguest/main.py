from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myprojectdb.db"

db.init_app(app)


class ContactUs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    message = db.Column(db.Text)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("home.html")

@app.route('/about')
def homepage():
    return render_template("about.html")

@app.route('/contact')
def contactus():
    return render_template("contact.html")

@app.route('/services')
def servicesus():
    return render_template("services.html")


@app.route("/savingdata", methods = ['post'])
def saveing():
    if request.method == "POST":
        fullname = request.form.get("fname")
        email = request.form.get("email")
        phon_num = request.form.get("pnumber")
        mssg = request.form.get("msg")

        data = ContactUs(full_name = fullname, email = email, phone_number = phon_num, message = mssg)
        db.session.add(data)
        db.session.commit()
    
    return f"this route saveing data. {fullname} {email}  {phon_num}  {mssg}"


if __name__ == "__main__":
    app.run(debug=True)