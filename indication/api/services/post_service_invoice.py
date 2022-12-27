from flask import jsonify, request
from indication import db
from indication.models import ServiceInvoice, Price

def post_service_invoice(address_id):

    name_service = request.json.get("name_service")
    cur_value = request.json.get("cur_value")

    gen =  ServiceInvoice.query.filter_by(address_id=address_id, type_service_id=name_service).order_by(ServiceInvoice.id.desc()).limit(2).all()

    messages = []

    try:
        float(cur_value)

        if float(cur_value) < 0:
            messages.append("Error, meter readings cannot be negative")

        elif gen != [] and float(cur_value) < float(gen[0].cur_value):
            messages.append("Error, counter readings cannot be less than previous readings")

    except:
        messages.append("Error, meter readings must be in numeric format")

    if messages:
        return jsonify({"status": "fail",
                        "detail": messages}), 400

    inv = ServiceInvoice(
        address_id = address_id, 
        cur_value = cur_value,
        prv_value = 0.0 if len(gen) == 0 else gen[0].cur_value,
        type_service_id = name_service, 
        price_id = name_service,
        paid = 0,
        duty = int(cur_value) * Price.query.get(name_service).rate 
                if len(gen) == 0 
                else gen[0].duty - gen[0].paid + int((int(cur_value) - gen[0].cur_value) * Price.query.get(name_service).rate),
    )

    db.session.add(inv)
    db.session.commit()    

    messages.append("Your meter readings have been taken")

    return jsonify({"status": "OK",
                    "detail": messages}), 200