from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_migrate import Migrate

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
    migrate = Migrate(app, db)

    from indication.api.controllers import api
    from indication.admin.controllers import admin
    from indication.website.routes import service

    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(service, url_prefix='/')

    from indication.models import User, Address, TypeService, Price, ServiceInvoice

    create_database(app)
    return app


def create_database(app):
    if not path.exists('indication/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')