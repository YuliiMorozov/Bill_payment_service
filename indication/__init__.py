from http.client import HTTPException
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_migrate import Migrate

from indication.api.exceptions.invoice_exceptions import InvalidUsage
# from indication.api.exceptions.invoice_exceptions import CurrentValueError

db = SQLAlchemy()
DB_NAME = "payment_server_db.db"


def create_app():
    app = Flask(__name__)
    from flask_cors import CORS

    CORS(app)
    app.config['SECRET_KEY'] = 'my_secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)


    from flask import jsonify

    class InvalidUsage(Exception):
        status_code = 400

        def __init__(self, message, status_code=None, payload=None):
            Exception.__init__(self)
            self.message = message
            if status_code is not None:
                self.status_code = status_code
            self.payload = payload

        def to_dict(self):
            rv = dict(self.payload or ())
            rv['message'] = self.message
            return rv

    @app.errorhandler(InvalidUsage)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response
    
    @app.route('/foo')
    def get_foo():
        raise InvalidUsage('This view is gone', status_code=410)






    from indication.api.controllers import api
    from indication.admin.controllers import admin
    from indication.website.routes import service

    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(service, url_prefix='/')

    from indication.models import User, Address, TypeService, ServiceRule, ServiceInvoice, PaymentTransaction

    @app.errorhandler(InvalidUsage)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    create_database(app)
    return app


def create_database(app):
    if not path.exists('indication/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')