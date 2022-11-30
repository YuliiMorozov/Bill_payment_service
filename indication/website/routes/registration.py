from indication.website.routes import service
from indication.website.controllers.registration import create_registration


@service.route('/registration', methods=['GET', 'POST'])
def registration():
    return create_registration()