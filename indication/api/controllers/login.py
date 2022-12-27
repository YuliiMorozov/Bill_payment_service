from indication.api.controllers import api
from indication.api.services.post_login import post_login

@api.route('/login', methods=["POST"])
def login():
    return post_login()