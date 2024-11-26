from flask import Blueprint,jsonify
from flask_mail import Mail,Message
emailBP = Blueprint("email",__name__)


# Initialize Flask-Mail
mail = Mail()
def init_app(app):
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'piyush.bootcoding@gmail.com'
    app.config['MAIL_PASSWORD'] = 'ztazcydbsudwfimb'
    app.config['MAIL_DEFAULT_SENDER'] = 'piyush.bootcoding@gmail.com'
    mail.init_app(app)



@emailBP.route("/send/email")
def sendEmail():
    subject = "Test Email"
    recipient = "piyushbthaware4@gmail.com"
    body = "This is a test email sent using Flask-Mail."
    html = "<h1>This is html from test email</h1>"
    message = Message(subject=subject,recipients=[recipient],body=body,html=html)
    try:
        mail.send(message=message)
        return jsonify({
            "status": "success",
            "message": "Email sent successfully!"
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Failed to send email: {str(e)}"
        })