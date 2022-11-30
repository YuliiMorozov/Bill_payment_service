from flask import Blueprint

api = Blueprint('api', __name__)

from indication.api.routes.home import api
from indication.api.routes.login import api
from indication.api.routes.registration import api
from indication.api.routes.address import api
from indication.api.routes.service_invoice import api