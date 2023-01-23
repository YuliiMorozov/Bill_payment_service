from flask import request, jsonify
from indication.admin.controllers import admin
from indication.admin.services.post_type_service import post_type_service
from indication.admin.services.get_type_service import get_type_service
from flask_login import current_user

@admin.route('/type_service', methods=["GET", "POST"])
def type_service():

    if current_user.username == "Admin":

        if request.method == "POST":
            return post_type_service()

        if request.method == "GET":
            return get_type_service()

    return jsonify('You are not admin')