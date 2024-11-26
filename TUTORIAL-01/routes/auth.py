from flask import Blueprint,request,render_template,abort,flash,redirect,url_for

auth_bp = Blueprint("auth",__name__)

@auth_bp.route("/auth/signin",methods=["POST","GET"])
def signin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "root":
            flash("you are signin successfully!")
            print(f"POST : username = {username} , password = {password}")
            return redirect(url_for('home.index'))
        else:
            abort(401)
            return "signin failed"

    elif request.method == "GET":
        username = request.args.get("username")
        password = request.args.get("password")
        print(f"GET : username = {username} , password = {password}")
    return render_template("auth/signin.html")