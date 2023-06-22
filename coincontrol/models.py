from coincontrol.extensions import db
from datetime import datetime


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(80), unique= True, nullable=False)
    password = db.Column(db.String(60), nullable = False)
    email = db.Column(db.String(80), unique=True, nullable = False)
    verified = db.Column(db.Boolean, default=0)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"Users('username:{self.username}', 'email:{self.email}')"
        