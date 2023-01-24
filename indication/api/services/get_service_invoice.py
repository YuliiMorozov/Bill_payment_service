from flask import jsonify
from indication.models import ServiceInvoice, TypeService


def get_service_invoice(address_id):

    # serviceinvocie = ServiceInvoice.query.filter_by(address_id=address_id).order_by(ServiceInvoice.id.desc()).all()
    # serviceinvocie = ServiceInvoice.query.filter_by(address_id=address_id).order_by(ServiceInvoice.type_service_id.desc()).all()
    serviceinvocie = ServiceInvoice.query.filter_by(address_id=address_id).order_by(ServiceInvoice.type_service_id.desc()).all()
    # print(type(serviceinvocie))

    invoice_23 = [] 
    # f = []

    for info in serviceinvocie:
                
        print(info.type_service_id)
        # if info.type_service_id not in f:
        #     f.append(info.type_service_id)
            


        # f.append(info.type_service_id)
        

        payment_order = {
            f"past_{info.typeservice.name_service}_value": info.prv_value,
            f"now_{info.typeservice.name_service}_value": info.cur_value,
            f"to_pay_for_{info.typeservice.name_service}": info.duty
        }
        # print(info.typeservice)



        invoice_23.append(payment_order) 
        # for key in invoice:
            # print(key)
        # print(type(payment_order))   
    # print(f)
    return jsonify(invoice_23), 200