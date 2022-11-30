from flask import render_template
from indication.website.routes import service

@service.app_errorhandler(404)
def page_not_found(error):
    return render_template("page_404.html"), 404
