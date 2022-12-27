from flask import request, jsonify
from indication import db
from indication.models import TypeService

def post_type_service():

        name_service = request.json.get("name_service")       
        new_service = TypeService.query.filter_by(name_service=name_service).first()

        messages = []

        if new_service:
            messages.append("This service has already been created")

        if messages:
            return jsonify({"Errors": messages}), 400  

        service = TypeService(name_service=name_service)
        db.session.add(service)
        db.session.commit()

        messages.append("New service created")
        return jsonify({"OK": messages}), 200