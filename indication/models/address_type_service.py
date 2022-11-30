from indication import db

# Table for many-to-many Address and TypeService
address_type_service = db.Table('address_type_service',
                                db.Column('address_id', db.Integer, db.ForeignKey('address.id')),
                                db.Column('type_service_id', db.Integer, db.ForeignKey('typeservice.id'))
)