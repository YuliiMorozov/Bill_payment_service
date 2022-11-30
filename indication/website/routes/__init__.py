from flask import Blueprint

service = Blueprint('cervice', __name__, template_folder='../templates')

from indication.website.routes.home import service
from indication.website.routes.registration import service
from indication.website.routes.page_404 import service