from flask import Flask,jsonify
from flask_jwt_extended import JWTManager
app = Flask(__name__)
app.secret_key = "private_key"


# REGISTER ROUTES
from routes.cookies import cookiesBP
from routes.home import homeBP
from routes.email import init_app,emailBP
from routes.session import sessionBP
from routes.jwt import jwtBP
app.register_blueprint(cookiesBP)
app.register_blueprint(homeBP)
init_app(app)
app.register_blueprint(emailBP)
app.register_blueprint(sessionBP)


# Initialize the JWT Manager with the app
app.config['JWT_SECRET_KEY'] = 'privateKey'
jwt_manager = JWTManager(app)
app.register_blueprint(jwtBP)


# Page not found
@app.errorhandler(404)
def pageNotFound(error):
    return jsonify({
        "status": "failed",
        "data": "page not found"
    }), 404

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8000)