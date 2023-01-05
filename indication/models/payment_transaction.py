from datetime import datetime
from indication import db

class PaymentTransaction(db.Model):
    __tablename__ = 'paymenttransaction'
    id = db.Column(db.Integer, primary_key=True)
    sum = db.Column(db.Integer)
    status = db.Column(db.Boolean, default=False)
    date_of_transaction = db.Column(db.DateTime, default=datetime.utcnow)

    # one-to-many with User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # one-to-one with ServiceInvoice
    servis_invoice_id = db.Column(db.Integer, db.ForeignKey('serviceinvoice.id'))