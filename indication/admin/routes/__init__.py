from flask import Blueprint

admin = Blueprint('admin', __name__)

from indication.admin.routes.type_service import admin