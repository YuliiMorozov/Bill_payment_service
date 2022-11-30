from flask import jsonify
from indication.models import ServiceInvoice


def get_service_invoice(address_id):

    serviceinvocie = ServiceInvoice.query.filter_by(address_id=address_id)
    invoice = [] 

    for info in serviceinvocie:

        if info.paid is False:

            payment_order = {
                f"past_{info.typeservice.name_service}_value": info.prv_value,
                f"now_{info.typeservice.name_service}_value": info.cur_value,
                f"to_pay_for_{info.typeservice.name_service}": (info.cur_value - info.prv_value) * info.price.rate
            }
            invoice.append(payment_order)    

    return jsonify(invoice), 200