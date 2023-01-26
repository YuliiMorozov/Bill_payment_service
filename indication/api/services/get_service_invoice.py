from flask import jsonify
from indication import db
from indication.api.utils.cur_user import cur_user
from indication.models import Address, ServiceInvoice


def get_service_invoice(address_id):

    address = (
        db.session
        .query(Address)
        .filter_by(user_id=cur_user().id, id=address_id)
        .first()
    )

    invoices = (
        db.session
        .query(ServiceInvoice)
        .filter_by(address_id=address_id)
        .order_by(ServiceInvoice.type_service_id.desc(), ServiceInvoice.id.desc())
        .distinct(ServiceInvoice.type_service_id)
        .all()
    )

    if address is None:
        return jsonify("Bad request. The address does`t belong to this user "), 400

    return jsonify(invoices), 200