from flask import Blueprint, request, jsonify
from flask_jwt_extended import  create_access_token
jwtBP = Blueprint("jwt", __name__)

@jwtBP.route("/jwt/auth/signin", methods=["POST"])
def signin():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        token = create_access_token(identity=email)
        return jsonify({
            "status": "success",
            "data": token
        })
