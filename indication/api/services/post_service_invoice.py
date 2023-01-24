from flask import jsonify, request
from indication import db
from indication.models import ServiceInvoice, ServiceRule
from indication.api.utils.invoice_validator import validate_cur_value

def post_service_invoice(address_id):

    type_service_id = request.json.get("type_service_id")    
    cur_value = request.json.get("cur_value")

    prv_invoice = (
        db.session
        .query(ServiceInvoice)
        .filter((ServiceInvoice.address_id == address_id) & (ServiceInvoice.type_service_id == type_service_id))
        .order_by(ServiceInvoice.id.desc())
        .first()
    )
    
    servise_rule = (
        db.session
        .query(ServiceRule)
        .filter(ServiceRule.type_service_id == type_service_id)
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
        duty = prv_invoice.duty - prv_invoice.paid + ((cur_value - prv_invoice.cur_value) * servise_rule.tax)
            if prv_invoice
            else cur_value * servise_rule.tax,    
        service_rule_id = servise_rule.id,
        type_service_id = type_service_id,
    )

    db.session.add(invoice)
    db.session.commit()    

    return jsonify({"status": "OK",
                    "detail": "Your meter readings have been taken"}), 200