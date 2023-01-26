import os
from indication import db
from flask import request, jsonify
from indication.models import User
from dotenv import load_dotenv
import jwt

def post_login():
    
    email = request.json.get("email")   
    password = request.json.get("password")
    
    user = (
        db.session
        .query(User)
        .filter_by(email=email)
        .first()
    )

    if user is None or user.check_password(password) is False:
        return jsonify("Bad username or password"), 400 
    
    load_dotenv()

    access_token = jwt.encode({"email": email}, os.getenv('SECRET_KEY'), algorithm="HS256")
    return jsonify({"status": "success",
                    "access_token": access_token})