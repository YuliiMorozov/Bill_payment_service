import os
import jwt
from flask import request
from dotenv import load_dotenv
from indication import db
from indication.models import User
    
def cur_user():

    load_dotenv()

    token = request.headers.get('Authorization') 

    get_user_info =  jwt.decode(token.split()[1], os.getenv('SECRET_KEY'), algorithms=["HS256"])['email']

    user = (
        db.session
        .query(User)
        .filter_by(email=get_user_info)
        .first()
    )

    return user