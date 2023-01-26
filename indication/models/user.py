from datetime import datetime
from indication import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    email = db.Column(db.String(64))
    password_hash = db.Column(db.String(280))
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # one-to-many with Address
    addresses = db.relationship('Address', backref='user', lazy='dynamic')

    # one-to-many with PaymentTransaction
    payment_transactions = db.relationship('PaymentTransaction', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)