from indication import db
from .address_type_service import address_type_service

class TypeService(db.Model):    
    __tablename__ = 'typeservice'

    id = db.Column(db.Integer, primary_key=True)
    name_service = db.Column(db.String(24), unique=True)

    # one-to-one with ServiceRule
    type_service_id = db.relationship('ServiceRule', backref='typeservice', uselist=False)
    
    # one-to-one with ServiceInvoice
    type_service_id = db.relationship('ServiceInvoice', backref='typeservice', uselist=False)