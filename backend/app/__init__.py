from flask import (
    Flask,
    request,
    jsonify,
    abort
)
from .models import *
from flask_cors import CORS
from .utilities import *

import os
import sys

def create_app(test_config=None):
    app = Flask(__name__)
    with app.app_context():
        setup_db(app, test_config['database_path'] if test_config else None)
        CORS(app, origins='*')

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        response.headers.add(' Access-Control-Max-Age', '10')
        return response
    
    # ROUTES

    return app

