from flask import Blueprint,render_template,session,redirect,url_for,flash
homeBP = Blueprint("home",__name__)

@homeBP.route("/")
def index():
    if "user" not in session:  
        flash("You must be logged in to access the dashboard.")
        return redirect(url_for("auth.signin"))
    return render_template("home/Home.html")