from flask import jsonify
from indication.api.utils.cur_user import cur_user

def get_home():
    return jsonify(cur_user().username)