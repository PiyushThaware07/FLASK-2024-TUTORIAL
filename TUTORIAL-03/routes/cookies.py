import json
from flask import Blueprint, make_response, request, jsonify
cookiesBP = Blueprint("cookies", __name__)



@cookiesBP.route("/set/cookie")
def setCookies():
    cookie_data = {
        "username": "piyushthaware",
        "email": "piyush@example.com",
        "role": "developer",
        "visited" : 0
    }
    cookie_value = json.dumps(cookie_data)
    res = make_response(jsonify({
        "status": "success",
        "message": "Cookie set successfully"
    }))
    res.set_cookie("mycookie", cookie_value, max_age=60*60*24)
    return res



@cookiesBP.route("/get/cookie")
def getCookie():
    cookie_value = request.cookies.get("mycookie")
    if cookie_value:
        cookie_data = json.loads(cookie_value)
        return jsonify({
            "status": "success",
            "data": cookie_data
        })
    return jsonify({
        "status": "error",
        "message": "No cookie found"
    }), 404


@cookiesBP.route("/delete/cookie")
def deleteCookie():
    cookie_value = request.cookies.get("mycookie")
    if cookie_value:
        res = make_response(jsonify({
            "status": "success",
            "message": "Cookie deleted successfully"
        }))
        res.delete_cookie("mycookie")
        return res
    else:
        return jsonify({
            "status": "error",
            "message": "No cookie found"
            }), 404