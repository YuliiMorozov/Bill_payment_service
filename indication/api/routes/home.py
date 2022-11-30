from indication.api.routes import api
from indication.api.controllers.get_home import get_home

@api.route('/home', methods=["GET"])
def home():
    return get_home()