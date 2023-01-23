from flask import jsonify
from indication import db
from indication.models import TypeService


def get_types_service():

    types_service = []

    all_services = (
        db.session
        .query(TypeService)
        .all()
    )

    for service in all_services:
            
        types_service.append({
            "id": service.id,
            "name_service": service.name_service
        })

    return jsonify(types_service), 200