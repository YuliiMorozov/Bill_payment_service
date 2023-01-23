from flask import Blueprint

api = Blueprint('api', __name__)

from indication.api.controllers.home import api
from indication.api.controllers.login import api
from indication.api.controllers.registration import api
from indication.api.controllers.address import api
from indication.api.controllers.service_invoice import api
from indication.api.controllers.services import api