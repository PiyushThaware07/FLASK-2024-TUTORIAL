from flask import Blueprint,jsonify,json,request,make_response
homeBP = Blueprint("home",__name__)

@homeBP.route("/")
def home():
    cookieValue = request.cookies.get("mycookie")
    cookieData = json.loads(cookieValue)
    cookieData["visited"] += 1
    updatedCookieValue = json.dumps(cookieData)
    response = make_response({
        'status' : 'success',
        'data' : 'Server Running...',
        'visited' : cookieData["visited"]
    })
    response.set_cookie("mycookie",updatedCookieValue,60*60*24)
    return response