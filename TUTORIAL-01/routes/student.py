from flask import Blueprint, session, redirect, url_for
from model import AuthModel

student_bp = Blueprint("student", __name__)
@student_bp.route("/student/login/<string:username>/<string:password>")
def setStudent(username,password):
    session["username"] = username
    session["password"] = password
    newUser = AuthModel(username,password)
    return redirect(url_for("student.studentProfile"))  # Corrected route name



@student_bp.route("/student/profile")
def studentProfile():
    username = session.get("username")
    if username:
        return f'Hello {username}!'
    else:
        return redirect(url_for('home.index'))  # Redirect to home if no session


@student_bp.route("/student/logout")
def studentLogout():
    session.pop("username",None)
    return redirect(url_for('home.index')) 

