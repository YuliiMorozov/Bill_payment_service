from indication import db

class Price(db.Model):    
    __tablename__ = 'price'
    id = db.Column(db.Integer, primary_key=True)
    rate = db.Column(db.Float, nullable=False)

    # one-to-one with ServiceInvoice
    service_invoice_id = db.relationship('ServiceInvoice', backref='price', uselist=False)