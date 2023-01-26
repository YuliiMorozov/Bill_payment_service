from flask import jsonify
from indication import db
from indication.api.utils.cur_user import cur_user
from indication.models import Address


def get_address():

    addresses = (
        db.session
        .query(Address)
        .filter_by(user_id=cur_user().id)
        .all()
    )

    if addresses == []:
        return jsonify("You have no added addresses. Want to add?"), 200

    return jsonify(addresses), 200