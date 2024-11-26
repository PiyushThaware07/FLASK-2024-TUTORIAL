from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dbConnection import dbConnection

app = Flask(__name__)
app.secret_key = "my_secret_key"

# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/flask-tutorial'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dbConnection.init_app(app)

# REGISTER ROUTES
from routes.home import home_bp
from routes.post import post_bp
from routes.auth import auth_bp
from routes.student import student_bp
app.register_blueprint(home_bp)
app.register_blueprint(post_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(student_bp)

with app.app_context():
    dbConnection.create_all() 

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
