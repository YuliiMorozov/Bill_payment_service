from flask import jsonify, request
from indication import db
from indication.models import ServiceInvoice

def post_service_invoice(address_id):
    
    name_service = request.json.get("name_service")
    cur_value = request.json.get("cur_value")

    info = ServiceInvoice.query.filter_by(address_id=address_id, type_service_id=name_service).first()

    messages = []

    try:
        float(cur_value)

        if float(cur_value) < 0:
            messages.append("Error, meter readings cannot be negative")

        elif bool(info) is True and float(cur_value) < float(info.cur_value):
            messages.append("Error, counter readings cannot be less than previous readings")

    except:
        messages.append("Error, meter readings must be in numeric format")

    if messages:
        return jsonify({"status": "fail",
                        "detail": messages}), 400

    if bool(info) is False:

        service_invoice = ServiceInvoice(
            address_id = address_id, 
            cur_value = cur_value,
            prv_value = 0.0,
            type_service_id = name_service, 
            price_id = name_service
        )
        
        db.session.add(service_invoice)
        db.session.commit()     

    else:

        if info.paid is False:            
            info.prv_value = info.prv_value

        else:
            info.prv_value = info.cur_value
            info.paid = 0
        
        info.cur_value = cur_value

        db.session.commit() 
    
    messages.append("Your meter readings have been taken")
    
    return jsonify({"status": "OK",
                    "detail": messages}), 200










































# SECOND FUNCTION






    # name_service = request.json.get("name_service")
    # cur_value = request.json.get("cur_value")

    # gen =  ServiceInvoice.query.filter_by(address_id=address_id, type_service_id=name_service).order_by(ServiceInvoice.id.desc()).limit(2).all()

    # messages = []

    # try:
    #     float(cur_value)

    #     if float(cur_value) < 0:
    #         messages.append("Error, meter readings cannot be negative")

    #     elif gen != [] and float(cur_value) < float(gen[0].cur_value):
    #         messages.append("Error, counter readings cannot be less than previous readings")

    # except:
    #     messages.append("Error, meter readings must be in numeric format")

    # if messages:
    #     return jsonify({"status": "fail",
    #                     "detail": messages}), 400

    # inv = ServiceInvoice(
    #     address_id = address_id, 
    #     cur_value = cur_value,
    #     prv_value = 0.0 if len(gen) == 0 else (gen[0].prv_value if len(gen) > 0 and gen[0].paid is False else gen[0].cur_value),
    #     type_service_id = name_service, 
    #     price_id = name_service
    # )

    # db.session.add(inv)
    # db.session.commit() 

    # messages.append("Your meter readings have been taken")

    # return jsonify({"status": "OK",
    #                 "detail": messages}), 200