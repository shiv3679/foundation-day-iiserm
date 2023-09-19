from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=current_directory)

# SQLite database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///registrations.db"
db = SQLAlchemy(app)

# Database model for individual registration
class IndividualRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidateName = db.Column(db.String(100), nullable=False)
    institutionName = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(20), nullable=False)
    mobileNumber = db.Column(db.String(20), nullable=False)
    emailId = db.Column(db.String(50), nullable=True)  # Now nullable

# Database model for school registration
class SchoolRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schoolName = db.Column(db.String(100), nullable=False)
    teacherName = db.Column(db.String(100), nullable=False)
    teacherContact = db.Column(db.String(20), nullable=False)
    totalStudents = db.Column(db.Integer, nullable=False)
    grade1to5 = db.Column(db.Integer, nullable=True)
    grade6to8 = db.Column(db.Integer, nullable=True)
    grade9to12 = db.Column(db.Integer, nullable=True)
    arrivalTime = db.Column(db.String(10), nullable=False)

def init_db():
    with app.app_context():
        db.create_all()

# Uncomment the following line if you want to initialize the database upon startup
init_db()

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
        # emailId = request.form["individualEmail"]  # Commented out as it's no longer in your form

        new_registration = IndividualRegistration(
            candidateName=candidateName,
            institutionName=institutionName,
            grade=grade,
            mobileNumber=mobileNumber,
            emailId=None  # Set to None as it's no longer in your form
        )

        db.session.add(new_registration)
        db.session.commit()

    return redirect(url_for("home"))

@app.route("/school_registration", methods=["POST"])
def school_registration():
    if request.method == "POST":
        schoolName = request.form["schoolName"]
        teacherName = request.form["teacherName"]
        teacherContact = request.form["teacherContact"]
        totalStudents = int(request.form["totalStudents"])
        grade1to5 = int(request.form["grade1to5"]) if request.form["grade1to5"] else None
        grade6to8 = int(request.form["grade6to8"]) if request.form["grade6to8"] else None
        grade9to12 = int(request.form["grade9to12"]) if request.form["grade9to12"] else None
        arrivalTime = request.form["arrivalTime"]

        new_school_registration = SchoolRegistration(
            schoolName=schoolName,
            teacherName=teacherName,
            teacherContact=teacherContact,
            totalStudents=totalStudents,
            grade1to5=grade1to5,
            grade6to8=grade6to8,
            grade9to12=grade9to12,
            arrivalTime=arrivalTime
        )

        db.session.add(new_school_registration)
        db.session.commit()

    return redirect(url_for("home"))

@app.route("/admin")
def admin():
    all_data_individual = IndividualRegistration.query.all()
    all_data_school = SchoolRegistration.query.all()
    return render_template("admin.html", individual_registrations=all_data_individual, school_registrations=all_data_school)

if __name__ == "__main__":
    app.run(debug=True)
