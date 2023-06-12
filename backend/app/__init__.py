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
    
    # BASIC ROUTES
    # ================================================================

    # GET
    # ----------------------------------------------------------------

    @app.route('/users', methods=['GET'])
    def get_users():
        pass

    @app.route('/expenses', methods=['GET'])
    def get_expenses():
        pass

    @app.route('/budgets', methods=['GET'])
    def get_budgets():
        pass

    @app.route('/savings', methods=['GET'])
    def get_savings():
        pass

    @app.route('/categories', methods=['GET'])
    def get_categories():
        pass

    # POST
    # ----------------------------------------------------------------

    @app.route('/users', methods=['POST'])
    def post_users():
        pass

    @app.route('/expenses', methods=['POST'])
    def post_expenses():
        pass

    @app.route('/budgets', methods=['POST'])
    def post_budgets():
        pass

    @app.route('/savings', methods=['POST'])
    def post_savings():
        pass

    @app.route('/categories', methods=['POST'])
    def post_categories():
        pass

    # DELETE
    # ----------------------------------------------------------------

    @app.route('/users', methods=['DELETE'])
    def delete_users():
        pass

    @app.route('/expenses', methods=['DELETE'])
    def delete_expenses():
        pass

    @app.route('/budgets', methods=['DELETE'])
    def delete_budgets():
        pass

    @app.route('/savings', methods=['DELETE'])
    def delete_savings():
        pass

    @app.route('/categories', methods=['DELETE'])
    def delete_categories():
        pass



    # APP ROUTES
    # ===============================================================

    # GET
    # ----------------------------------------------------------------

    
    return app

