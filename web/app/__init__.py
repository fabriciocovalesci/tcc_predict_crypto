from re import TEMPLATE
from flask import Flask
from app import routes
import os


TEMPLATES = os.path.abspath("templates")
STATIC = os.path.abspath("static")



def create_app():
    app = Flask(__name__, template_folder=TEMPLATES, static_folder=STATIC)

    routes.init_app(app)
        
    return app