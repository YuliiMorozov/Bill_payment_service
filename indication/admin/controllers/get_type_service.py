from flask import jsonify
from indication.models import TypeService

def get_type_service():

    services = TypeService.query.filter_by(name_service=TypeService.name_service).all()

    all_services = []

    for service in services:
        service_info = {
            'id': service.id,
            'name_service': service.name_service
        }
        
        all_services.append(service_info)

    return jsonify(all_services), 200