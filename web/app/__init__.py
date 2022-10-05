from re import TEMPLATE
from flask import Flask
from flask_cors import CORS
from app import routes
from app.config import BASE_DIR, DATA_CORR
from app.filters import format_date
import os


def create_app():
    app = Flask(__name__, 
                template_folder=os.path.join(BASE_DIR, "resources", "templates"), 
                static_folder=os.path.join(BASE_DIR, "resources", "static"))
    
    CORS(app)
    
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.jinja_env.filters["format_date"] = format_date
    
    routes.init_app(app)
        
    return app