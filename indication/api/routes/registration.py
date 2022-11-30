from indication.api.routes import api
from indication.api.controllers.post_registration import get_registration

@api.route('/registration', methods=["POST"])
def registration():
    return get_registration()