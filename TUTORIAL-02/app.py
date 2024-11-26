from flask import Flask
from model.db import db
app = Flask(__name__)
app.secret_key = 'private_key' 
# DATABASE CONNECTION
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/flask-tutorial'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# REGISTER ROUTES
from routes.auth import authBP
from routes.home import homeBP
app.register_blueprint(authBP)
app.register_blueprint(homeBP)


if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True,host="0.0.0.0",port=8000)