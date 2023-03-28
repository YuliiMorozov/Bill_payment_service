from flask import jsonify
from indication import db
from indication.models import Address
from indication.models.user import User
from indication.schemas.address_schema import AddressSchema

def get_types_service(address_id):

    all_services = (
        db.session
        .query(Address)
        .filter_by(id=address_id)
    )

    check = (
        db.session
        .query(User)
        .filter_by(username='Admin')
        .first()
    )
    print(check)

    type_services = AddressSchema(many=True).dump(all_services)

    return jsonify(type_services), 200