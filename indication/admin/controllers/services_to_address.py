from flask import request, jsonify
from indication.admin.controllers import admin
# from indication.admin.services.post_type_service import post_type_service
# from indication.admin.services.get_type_service import get_type_service
from flask_login import current_user

from indication.admin.services.post_services_to_address import post_services_to_address

@admin.route('/services_to_address', methods=["GET", "POST", "PUT", "DELETE"])
def services_to_address():

    if current_user.username == "Admin":

        if request.method == "POST":
            return post_services_to_address()

        # if request.method == "GET":
        #     return get_services_to_address()

        # if request.method == "PUT":
        #     return put_services_to_address()

        # if request.method == "DELETE":
        #     return delete_services_to_address()

    return jsonify("You are not admin")