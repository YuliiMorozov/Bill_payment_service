from flask import jsonify
from indication import db
from indication.models import ServiceInvoice, TypeService


def get_service_invoice(address_id):

    invoices = []

    all_services = (
        db.session
        .query(TypeService)
        .all()
    )

    invoice_234 = [] 
    # f = []
    for service in all_services:   

        last_invoice = (
            db.session
            .query(ServiceInvoice)
            .filter(ServiceInvoice.address_id == address_id)
            .order_by(ServiceInvoice.id.desc())
            .filter(ServiceInvoice.type_service_id == service.id)
            .first()
        )

        if last_invoice:
            # print(last_invoice.servicerule.tax)
            get_info = {
                "type_service_id": last_invoice.type_service_id,
                "service_rule_id": last_invoice.service_rule_id,
                "previous_value": last_invoice.prv_value,
                "current_value": last_invoice.cur_value,
                "duty": last_invoice.duty
            }
            
            invoices.append(get_info)

    return jsonify({"invoices": invoices}), 200