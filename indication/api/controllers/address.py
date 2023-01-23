from indication.api.controllers import api
from indication.api.services.get_address import get_address

@api.route('/address', methods=["GET"])
def address():
    return get_address()