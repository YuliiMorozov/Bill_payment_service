import os
from flask import request, jsonify
from indication.models import User
from dotenv import load_dotenv
import jwt

def post_login():
    
    email = request.json.get("email")   
    password = request.json.get("password")
    
    user = User.query.filter_by(email=email).first()

    messages = []

    if user is None:
        messages.append("Bad username or password")
    
    if user and user.check_password(password) is False:
        messages.append("Bad username or password. Can't login?")

    if messages:
        return jsonify({"Errors": messages}), 401
    
    else: 
        messages.append("Welcome to the website")    
    
    load_dotenv()
    access_token = jwt.encode({"email": email}, os.getenv('SECRET_KEY'), algorithm="HS256")
    return jsonify({"status": "success",
                    "detail": messages,
                    "access_token": access_token})