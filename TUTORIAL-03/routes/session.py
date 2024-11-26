from flask import Blueprint,session,jsonify,request
sessionBP = Blueprint("session",__name__)

@sessionBP.route("/session/auth/signin/<username>")
def signin(username):
    session["username"] = username
    return jsonify({
        "status" : "success",
        "data" : "signin successfully!"
    })
    


@sessionBP.route("/session/auth/profile")
def profile():
    return jsonify({
        "status" : "success",
        "data" : session.get("username")
    })
    
    

@sessionBP.route("/session/auth/signout")
def signout():
    session.pop("username")
    return jsonify({
        "status": "success",
        "data": "Signout successfully!"
    })