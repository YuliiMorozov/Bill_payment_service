from indication import db

class ServiceRule(db.Model):    
    __tablename__ = 'servicerule'
    id = db.Column(db.Integer, primary_key=True)
    tax = db.Column(db.Integer)

    # one-to-one with ServiceInvoice
    service_invoice_id = db.relationship('ServiceInvoice', backref='servicerule', uselist=False)
    # one-to-one with TypeService
    # service_invoice_id = db.relationship('ServiceInvoice', backref='servicerule', uselist=False)
    
    type_service_id = db.Column(db.Integer, db.ForeignKey('typeservice.id'))
