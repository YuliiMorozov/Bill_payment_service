from flask import request, jsonify
import re
from indication.models import User
from indication import db

def get_registration():

    username = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")
    password2 = request.json.get("password2")   

    new_username = User.query.filter_by(username=username).first()
    new_email = User.query.filter_by(email=email).first()

    regex_for_email = '[A-Za-z0-9._-]+@[a-z.-]+.[A-Z|a-z]'
    regex_for_password = '[a-z]+[a-z]+[a-z]+.+.+.+.'

    messages = []

    # check username
    if len(username) < 4 or len(username) > 25:
        messages.append("Name of username is short")
    if new_username:        
        messages.append("User with this username already exists"), 400

    # check email
    if bool(re.fullmatch(regex_for_email, email)) is False:
        messages.append("Please enter a valid email")
    if new_email:
        messages.append("This email has already used"), 400
    
    # check password
    if len(password) < 7:
        messages.append("Password is short")
    if bool(re.fullmatch(regex_for_password, password)) is False:
        messages.append("Please enter a valid password")
    if password2 != password:
        messages.append("Please repeat the password correctly")

    if messages:
        return jsonify({"Errors": messages}), 400
        
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    messages.append("Welcome to website")    
    return jsonify({"OK": messages}), 200