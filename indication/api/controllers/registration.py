from indication.api.controllers import api
from indication.api.services.post_registration import get_registration

@api.route('/registration', methods=["POST"])
def registration():
    return get_registration()