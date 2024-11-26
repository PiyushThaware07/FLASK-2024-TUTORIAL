from flask import Blueprint,render_template,request

home_bp = Blueprint("home",__name__)

@home_bp.route("/")
def index():
    profile_details = {
        "first_name" : "Shreyash",
        "last_name" : "Thaware",
        "email_address" : "Shreyash.thaware@gmail.com",
        "phone_number" : "987654321",
        "is_email_verified" : True,
        "skills" : ["React","Node","Express","Nest","Python","Flask"]
    }
    return render_template("index.html",data=profile_details)


@home_bp.route("/upload",methods=["POST"])
def upload():
    if request.method == "POST":
        myfile = request.files["file"]
        myfile.save("static/img/"+myfile.filename)
        return "uploaded successfully!"