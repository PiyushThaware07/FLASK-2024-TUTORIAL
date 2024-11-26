from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from model.db import db
from model.auth import Auth
import bcrypt
authBP = Blueprint("auth", __name__)




@authBP.route("/auth/signin", methods=["POST", "GET"])
def signin():
    if "user" in session:
        return redirect(url_for("home.index"))
      
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = Auth.query.filter_by(email=email).first()
        if not user:
            flash("Email not registered with us!")
            return redirect(url_for("auth.signup"))

        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            flash("Invalid Password")
            return redirect(url_for("auth.signin"))

        session["user"] = user.id
        flash("Signin Successfully!")
        return redirect(url_for("home.index"))
    return render_template("auth/Signin.html")









@authBP.route("/auth/signup", methods=["POST", "GET"])
def signup():
    if "user" in session:
        return redirect(url_for("home.index"))
    
    if request.method == "POST":
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        password = request.form.get('password')

        existingUser = Auth.query.filter_by(email=email).first()
        if existingUser:
            flash("Email already registered. Please use a different email.", "error")
            return redirect(url_for('auth.signup'))

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        newUser = Auth(fname=fname, lname=lname, email=email, password=hashed_password.decode('utf-8'))
        db.session.add(newUser)
        db.session.commit()

        flash("Registration successful! You can now sign in.", "success")
        return redirect(url_for("auth.signin"))
    return render_template("auth/Signup.html")



@authBP.route("/auth/signout")
def signout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.signin"))
