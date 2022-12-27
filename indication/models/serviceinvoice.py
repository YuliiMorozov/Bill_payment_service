from indication import db
from datetime import datetime

class ServiceInvoice(db.Model):    
    __tablename__ = 'serviceinvoice'
    id = db.Column(db.Integer, primary_key=True)
    # paid = db.Column(db.Boolean, default=False, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    prv_value = db.Column(db.Float)
    cur_value = db.Column(db.Float)
    paid = db.Column(db.Integer)
    duty = db.Column(db.Integer)
    
    # one-to-many with Address
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    # one-to-one with Price
    price_id = db.Column(db.Integer, db.ForeignKey('price.id'))
    # one-to-one with TypeService
    type_service_id = db.Column(db.Integer, db.ForeignKey('typeservice.id'))