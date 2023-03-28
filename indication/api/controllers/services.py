from indication.api.controllers import api
from indication.api.services.get_types_service import get_types_service


@api.route('/service_invoice/types/<int:address_id>', methods=['GET'])
def types_service(address_id):        
    return get_types_service(address_id)