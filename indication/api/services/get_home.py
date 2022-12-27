from flask import jsonify
from indication.models import User

def get_home():
    user = User.query.filter_by(username=User.username).first()
    if user:
        return jsonify({"msg": "Welcome to home page, " + user.username}), 200
    return jsonify({"msg": "No users"}), 200