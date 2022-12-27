from indication.api.controllers import api
from indication.api.services.get_address import get_address

@api.route('/address/<int:user_id>', methods=["GET"])
def address(user_id):
    return get_address(user_id)