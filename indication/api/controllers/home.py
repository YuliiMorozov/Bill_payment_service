from indication.api.controllers import api
from indication.api.services.get_home import get_home

@api.route('/home', methods=["GET"])
def home():
    return get_home()