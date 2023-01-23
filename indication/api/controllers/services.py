from indication.api.controllers import api
from indication.api.services.get_types_service import get_types_service


@api.route('/service_invoice/types', methods=['GET'])
def types_service():        
    return get_types_service()