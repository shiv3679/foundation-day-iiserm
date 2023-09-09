from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=current_directory)

# SQLite database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///registrations.db"
db = SQLAlchemy(app)

# Database model for registration
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidateName = db.Column(db.String(100), nullable=False)
    institutionName = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(20), nullable=False)
    mobileNumber = db.Column(db.String(20), nullable=False)
    emailId = db.Column(db.String(50), nullable=False)

# Initialize database tables
db.create_all()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/individual_registration", methods=["POST"])
def individual_registration():
    if request.method == "POST":
        candidateName = request.form["individualName"]
        institutionName = request.form["individualSchool"]
        grade = request.form["individualGrade"]
        mobileNumber = request.form["individualContact"]
        emailId = request.form["individualEmail"]

        new_registration = Registration(candidateName=candidateName, institutionName=institutionName, grade=grade, mobileNumber=mobileNumber, emailId=emailId)

        db.session.add(new_registration)
        db.session.commit()

    return redirect(url_for("home"))

@app.route("/school_registration", methods=["POST"])
def school_registration():
    if request.method == "POST":
        candidateName = request.form["teacherName"]
        institutionName = request.form["schoolName"]
        grade = request.form["gradesSections"]
        mobileNumber = request.form["totalStudents"]  # Note: You may want to change this to an actual contact number field in your form
        emailId = "N/A"  # Note: You may want to add an email field to your school registration form

        new_registration = Registration(candidateName=candidateName, institutionName=institutionName, grade=grade, mobileNumber=mobileNumber, emailId=emailId)

        db.session.add(new_registration)
        db.session.commit()

    return redirect(url_for("home"))

@app.route("/admin")
def admin():
    all_data = Registration.query.all()
    return render_template("admin.html", registrations=all_data)

if __name__ == "__main__":
    app.run(debug=True)
