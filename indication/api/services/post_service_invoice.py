from flask import jsonify, request
from indication import db
from indication.api.utils.cur_user import cur_user
from indication.models import ServiceInvoice, ServiceRule, Address, address_type_service, TypeService
from indication.api.utils.invoice_validator import validate_cur_value

def post_service_invoice(address_id):

    type_service_id = request.json.get("type_service_id")    
    cur_value = request.json.get("cur_value")

    address = (
        db.session
        .query(Address)
        .filter_by(user_id=cur_user().id, id=address_id)
        .first()
    )

    if address is None:
        return jsonify("Bad request. The address does`t belong to this user."), 400

    address_services = (
        db.session
        .query(address_type_service)
        .filter_by(address_id=address.id, type_service_id=type_service_id)
        .first()
    )

    if address_services is None:
         return jsonify("Bad request. Service at this address does`t exist"), 400

    prv_invoice = (        
        db.session
        .query(ServiceInvoice)
        .filter_by(address_id=address_id, type_service_id=type_service_id)
        .order_by(ServiceInvoice.id.desc())
        .first()            
    )

    servise_rule = (
        db.session
        .query(ServiceRule)
        .filter_by(type_service_id=type_service_id)
        .order_by(ServiceRule.id.desc())
        .first()
    )

    errors = validate_cur_value(cur_value, prv_invoice)
    if errors:
        return jsonify({"status": "fail",
                        "detail": errors}), 400

    invoice = ServiceInvoice(
        address_id = address_id, 
        prv_value = prv_invoice.cur_value
            if prv_invoice
            else 0.0,
        cur_value = cur_value,
        paid = 0,    
        duty = prv_invoice.duty - prv_invoice.paid + ((int(cur_value) - prv_invoice.cur_value) * servise_rule.tax)
            if prv_invoice
            else cur_value * servise_rule.tax,    
        service_rule_id = servise_rule.id,
        type_service_id = type_service_id,
    )

    db.session.add(invoice)
    db.session.commit()  

    return jsonify({"status": "OK",
                    "detail": "Your meter readings have been taken"}), 200