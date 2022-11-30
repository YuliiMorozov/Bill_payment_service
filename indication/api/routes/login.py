from indication.api.routes import api
from indication.api.controllers.post_login import post_login

@api.route('/login', methods=["POST"])
def login():
    return post_login()