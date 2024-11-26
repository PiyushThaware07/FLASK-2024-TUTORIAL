from dbConnection import dbConnection

class AuthModel(dbConnection.Model):
    id = dbConnection.Column(dbConnection.Integer, primary_key=True, autoincrement=True)
    username = dbConnection.Column(dbConnection.String(80), unique=True, nullable=False)
    password = dbConnection.Column(dbConnection.String(80), unique=True, nullable=False)

    def __str__(self):
        return f"User: {self.username}" 
