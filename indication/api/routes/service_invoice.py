from flask import request
from indication.api.routes import api
from indication.api.controllers.get_service_invoice import get_service_invoice
from indication.api.controllers.post_service_invoice import post_service_invoice


@api.route('/service_invoice/<int:address_id>', methods=['GET', 'POST'])
def service_invoice(address_id):

    if request.method == "GET":        
        return get_service_invoice(address_id)
    
    if request.method == "POST":        
        return post_service_invoice(address_id)
