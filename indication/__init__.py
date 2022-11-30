from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
# from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "payment_server_db.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'my_secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from indication.api.routes import api
    from indication.admin.routes import admin
    from indication.website.routes import service

    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(service, url_prefix='/')

    from indication.models import User, Address, TypeService, Price, ServiceInvoice

    create_database(app)

    # login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'
    # login_manager.init_app(app)

    # @login_manager.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('indication/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')