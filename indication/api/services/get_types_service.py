from flask import jsonify
from indication import db
from indication.models import TypeService


def get_types_service():

    all_services = (
        db.session
        .query(TypeService)
        .all()
    )

    return jsonify(all_services), 200