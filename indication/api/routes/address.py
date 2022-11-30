from indication.api.routes import api
from indication.api.controllers.get_address import get_address

@api.route('/address/<int:user_id>', methods=["GET"])
def address(user_id):
    return get_address(user_id)