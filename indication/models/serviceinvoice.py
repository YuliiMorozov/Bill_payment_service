from dataclasses import dataclass
from indication import db
from datetime import datetime
from indication.models import Address, ServiceRule
from .type_service import TypeService

@dataclass
class ServiceInvoice(db.Model):
    __tablename__ = 'serviceinvoice'
    
    id: int
    date: datetime
    prv_value: float
    cur_value: float
    paid: int
    duty: float

    address_id: Address
    service_rule_id: ServiceRule
    type_service_id: TypeService

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    prv_value = db.Column(db.Float)
    cur_value = db.Column(db.Float)
    paid = db.Column(db.Integer)
    duty = db.Column(db.Integer)
    
    # one-to-many with Address
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    # one-to-one with ServiceRule
    service_rule_id = db.Column(db.Integer, db.ForeignKey('servicerule.id'))

    # one-to-one with PaymentTransaction
    payment_transaction_id = db.relationship('PaymentTransaction', backref='serviceinvoice', uselist=False)
    
    # one-to-one with TypeService
    type_service_id = db.Column(db.Integer, db.ForeignKey('typeservice.id'))