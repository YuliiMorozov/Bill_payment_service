import os
from http.client import HTTPException
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow

from indication.api.exceptions.invoice_exceptions import InvalidUsage
# from indication.api.exceptions.invoice_exceptions import CurrentValueError


db = SQLAlchemy()
ma = Marshmallow()
login_manager = LoginManager()
login_manager.login_view = 'api.login'

def create_app():

    app = Flask(__name__)
    from flask_cors import CORS

    load_dotenv()

    CORS(app, supports_credentials=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    ma.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)    

    from indication.api.controllers import api
    from indication.admin.controllers import admin
    from indication.website.routes import service

    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(service, url_prefix='/')

    from indication.models import User, Address, TypeService, ServiceRule, ServiceInvoice, PaymentTransaction

    with app.app_context():
        db.create_all()

    @app.errorhandler(InvalidUsage)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response
    
    return app