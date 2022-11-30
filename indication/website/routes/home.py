from flask import render_template
from indication.website.routes import service

@service.route('/')
@service.route('/home')
def home():
    return render_template("home.html")