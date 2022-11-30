from flask import request
from indication.admin.routes import admin
from indication.admin.controllers.post_type_service import post_type_service
from indication.admin.controllers.get_type_service import get_type_service

@admin.route('/type_service', methods=["GET", "POST"])
def type_service():

    if request.method == "POST":
        return post_type_service()
        
    if request.method == "GET":
        return get_type_service()