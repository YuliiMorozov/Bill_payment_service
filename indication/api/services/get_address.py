from flask import jsonify
from indication.api.utils.cur_user import cur_user
from indication.models import Address


def get_address():

    addresses = Address.query.filter_by(user_id=cur_user().id).all()

    if addresses == []:
        return jsonify({"status": "fail",
                        "detail": "Page not found"}), 404
    
    user_addresses = []

    for address in addresses:
        address_info = {
            'id': address.id,
            'country': address.country,
            'city': address.city,
            'street': address.street,
            'house_number': address.house_number,
            'flat_number': address.flat_number,
            'zip_code': address.zip_code
        }
        user_addresses.append(address_info)    
    
    return jsonify(user_addresses), 200