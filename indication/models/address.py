from indication import db
from .address_type_service import address_type_service

class Address(db.Model):    
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(24), unique=False, nullable=False)
    city = db.Column(db.String(48), unique=False, nullable=False)
    street = db.Column(db.String(48), unique=False, nullable=False)
    house_number = db.Column(db.String(8), unique=False, nullable=False)
    flat_number = db.Column(db.String(8), unique=False, nullable=True)
    zip_code = db.Column(db.String(32), unique=False, nullable=False)

    # one-to-many with User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # one-to-many with ServiceInvoice
    serviceinvoices = db.relationship('ServiceInvoice', backref='address', lazy='dynamic')
    # many-to-many with Address_TypeService    
    type_services = db.relationship('TypeService', secondary=address_type_service, backref=db.backref('address', lazy='dynamic'))