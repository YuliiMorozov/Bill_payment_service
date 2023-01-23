from flask import Blueprint

admin = Blueprint('admin', __name__)

from indication.admin.controllers.type_service import admin
from indication.admin.controllers.services_to_address import admin