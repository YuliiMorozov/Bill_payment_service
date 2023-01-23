from flask import request, jsonify
from indication import db
from indication.models import TypeService, Address, address_type_service

def post_services_to_address():

    address_id = request.json.get("address_id")
    type_service_id = request.json.get("type_service_id")   

    messages = [] 

    address = (
        db.session
        .query(Address)
        .filter_by(id=address_id)
        .first()
    )    

    services = (
        db.session
        .query(TypeService)
        .filter_by(id=type_service_id)
        .first()
    )  

    if address is None:
        messages.append("This address does not exist")  

    if services is None:
        messages.append("This service does not exist")
    
    if messages:
        return jsonify({"Errors": messages}), 400


    service_to_address = (
        db.session
        .query(address_type_service)
        .filter_by(address_id=Address.id)
        .filter_by(type_service_id=TypeService.id)
        .all()
    )

    if (address_id, type_service_id) in service_to_address:

        messages.append("Service already connected")
        return jsonify({"Errors": messages}), 400      

    new_service = (
        address_type_service
        .insert()
        .values(
            address_id=address_id, 
            type_service_id=type_service_id
        )
    )

    db.session.execute(new_service) 
    db.session.commit()

    messages.append("Service connected")
    return jsonify({"OK": messages}), 200