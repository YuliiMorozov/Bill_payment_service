from flask import Blueprint

admin = Blueprint('admin', __name__)

from indication.admin.controllers.type_service import admin