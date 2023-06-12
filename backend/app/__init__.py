from flask import (
    Flask,
    request,
    jsonify,
    abort,
    session
)
from .models import *
from flask_cors import CORS
from .utilities import *

import os
import sys


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = "Uvuvwevwevwe Onyetenyevwe Ugwemuhwem Osas"

    with app.app_context():
        setup_db(app, test_config['database_path'] if test_config else None)
        CORS(app, origins='*')

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response
    
    # BASIC ROUTES
    # ================================================================

    # GET
    # ----------------------------------------------------------------

    @app.route('/users', methods=['GET'])
    @admin_required
    def get_users():
        code = 200
        users = []
        error_list = []
        inputs = request.args
        try:
            if len(inputs) == 0:
                users = User.query.all()
                users = [user.serialize() for user in users]
            else:
                if 'username' in inputs and 'role_name' not in inputs:
                    users = User.query.filter(User.username.like('%' + inputs['username'] + '%')).all()
                elif 'role_name' in inputs and 'username' not in inputs:
                    users = User.query.filter_by(role_name=inputs['role_name']).all()
                elif 'username' in inputs and 'role_name' in inputs:
                    users = User.query.filter(User.username.like('%' + inputs['username'] + '%')).filter_by(role_name=inputs['role_name']).all()
                else:
                    code = 400
                    error_list.append("Filter can only be done by username or role_name")

                users = [user.serialize() for user in users]

        except:
            code = 500

        if len(users) == 0:
            code = 404

        if code == 200:
            return jsonify({
                'success': True,
                'users': users,
                'message': 'You can search by username or role_name'
            }), code
        elif code == 400:
            return jsonify({
                'success': False,
                'errors': error_list
            })
        else: 
            abort(code)

    @app.route('/expenses', methods=['GET'])
    @login_required
    def get_expenses():
        code = 200
        inputs = request.args
        expenses = []
        error_message = ""

        if not('username' in inputs or session.get('role_name') == 'admin'):
            code = 400
            error_message = "username is required"
        else:
            try:
                if session.get('role_name') == 'admin':
                    if 'username' in inputs:
                        expenses = Expense.query.filter_by(username=inputs['username']).all()
                        expenses = [expense.serialize() for expense in expenses]
                    else:
                        expenses = Expense.query.all()
                        expenses = [expense.serialize() for expense in expenses]
                elif session.get('username') != inputs['username']:
                    code = 401
                else:
                    expenses = Expense.query.filter_by(username=inputs['username']).all()
                    expenses = [expense.serialize() for expense in expenses]
            except:
                code = 500

        if len(expenses) == 0:
            code = 404

        if code == 200:
            return jsonify({
                'success': True,
                'expenses': expenses
            }), code
        elif code == 400:
            return jsonify({
                'success': False,
                'message': error_message
            }), code
        else:
            abort(code)

    @app.route('/budgets', methods=['GET'])
    @login_required
    def get_budgets():
        code = 200
        inputs = request.args
        budgets = []
        error_message = ""

        if not('username' in inputs or session.get('role_name') == 'admin'):
            code = 400
            error_message = "username is required"
        else:
            try:
                if session.get('role_name') == 'admin':
                    if 'username' in inputs:
                        budgets = Budget.query.filter_by(username=inputs['username']).all()
                        budgets = [budget.serialize() for budget in budgets]
                    else:
                        budgets = Budget.query.all()
                        budgets = [budget.serialize() for budget in budgets]
                elif session.get('username') != inputs['username']:
                    code = 401
                else:
                    budgets = Budget.query.filter_by(username=inputs['username']).all()
                    budgets = [budget.serialize() for budget in budgets]
            except:
                code = 500

        if len(budgets) == 0:
            code = 404

        if code == 200:
            return jsonify({
                'success': True,
                'budgets': budgets
            }), code
        elif code == 400:
            return jsonify({
                'success': False,
                'message': error_message
            }), code
        else:
            abort(code)

    @app.route('/savings', methods=['GET'])
    @login_required
    def get_savings():
        code = 200
        inputs = request.args
        savings = []
        error_message = ""

        if not('username' in inputs or session.get('role_name') == 'admin'):
            code = 400 # Bad Request
            error_message = "username is required"
        else:
            try:
                if session.get('role_name') == 'admin':
                    if 'username' in inputs:
                        savings = Saving.query.filter_by(username=inputs['username']).all()
                        savings = [saving.serialize() for saving in savings]
                    else:
                        savings = Saving.query.all()
                        savings = [saving.serialize() for saving in savings]
                elif session.get('username') != inputs['username']:
                    code = 401 # Unauthorized
                else:
                    savings = Saving.query.filter_by(username=inputs['username']).all()
                    savings = [saving.serialize() for saving in savings]
            except:
                code = 500 # Internal Server Error
                print(sys.exc_info())
        
        if len(savings) == 0:
            code = 404

        if code == 200:
            return jsonify({
                'success': True,
                'savings': savings
            }), code
        elif code == 400:
            return jsonify({
                'success': False,
                'message': error_message
            }), code
        else:
            abort(code)



    @app.route('/categories', methods=['GET'])
    @login_required
    def get_categories():
        code = 200
        inputs = request.args
        categories = []
        error_message = ""

        if not('username' in inputs or session.get('role_name') == 'admin'):
            code = 400 # Bad Request
            error_message = "username is required"
        else:
            try:
                if session.get('role_name') == 'admin':
                    if 'username' in inputs:
                        categories = Category.query.filter_by(username=inputs['username']).all()
                        categories = [category.serialize() for category in categories]
                    else:
                        categories = Category.query.all()
                        categories = [category.serialize() for category in categories]
                elif session.get('username') != inputs['username']:
                    code = 401 # Unauthorized
                else:
                    categories = Category.query.filter_by(username=inputs['username']).all()
                    categories = [category.serialize() for category in categories]
            except:
                code = 500
                print(sys.exc_info())

        if len(categories) == 0:
            code = 404

        if code == 400:
            return jsonify({
                'success': False,
                'message': error_message
            }), code
        elif code == 200:
            return jsonify({
                'success': True,
                'categories': categories
            }), code
        else:
            abort(code)




    # POST
    # ----------------------------------------------------------------

    @app.route('/users', methods=['POST'])
    def post_users():
        error_list = []
        code = 201
        user_data = {}

        try:
            data = {}

            if request.json:
                data = request.json

                if not('username' in data):
                    error_list.append('username is required')

                if not('password' in data):
                    error_list.append('password is required')
            else:
                code = 400
                error_list.append('json data is required')
            

            if error_list:
                code = 400
            else:
                if User.query.filter_by(username=data['username']).first():
                    code = 400
                    error_list.append('username already exists')
                else:

                    user = User(
                        username=data['username'],
                        password=data['password'],
                        role_name='user'
                    )

                    db.session.add(user)
                    db.session.commit()

                    user_data = user.serialize()
                    session['username'] = user_data['username']
                    session['role_name'] = user_data['role_name']

        except Exception as e:
            db.session.rollback()
            print(sys.exc_info())
            code = 500

        if code == 400:
            return jsonify({'success': False, 'errors': error_list}), code
        elif code != 201:
            abort(code)
        else:
            return jsonify({'success': True, 'user': user_data}), code


    # DELETE
    # ----------------------------------------------------------------

    @app.route('/users', methods=['DELETE'])
    @admin_required
    def delete_users():
        try:
            db.session.query(User).delete()
            db.session.commit()
            return jsonify({
                'success': True,
                'message': 'Users deleted'
            }), 200
        except:
            db.session.rollback()
            print(sys.exc_info())
            abort(500)


    @app.route('/expenses', methods=['DELETE'])
    @admin_required
    def delete_expenses():
        try:
            db.session.query(Expense).delete()
            db.session.commit()
            return jsonify({
                'success': True,
                'message': 'Expenses deleted'
            }), 200
        except:
            db.session.rollback()
            print(sys.exc_info())
            abort(500)

    @app.route('/budgets', methods=['DELETE'])
    @admin_required
    def delete_budgets():
        try:
            db.session.query(Budget).delete()
            db.session.commit()
            return jsonify({
                'success': True,
                'message': 'Budgets deleted'
            }), 200
        except:
            db.session.rollback()
            print(sys.exc_info())
            abort(500)

    @app.route('/savings', methods=['DELETE'])
    @admin_required
    def delete_savings():
        try:
            db.session.query(Saving).delete()
            db.session.commit()
            return jsonify({
                'success': True,
                'message': 'Savings deleted'
            }), 200
        except:
            db.session.rollback()
            print(sys.exc_info())
            abort(500)

    @app.route('/categories', methods=['DELETE'])
    @admin_required
    def delete_categories():
        try:
            db.session.query(Category).delete()
            db.session.commit()
            return jsonify({
                'success': True,
                'message': 'Categories deleted'
            }), 200
        except:
            db.session.rollback()
            print(sys.exc_info())
            abort(500)



    # APP ROUTES
    # ===============================================================

    # GET
    # ----------------------------------------------------------------






    # ERROR HANDLER
    # ===============================================================

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': "Bad request"
        }), 400;

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': "Unauthorized"
        }), 401;


    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'success': False,
            'error': 403,
            'message': "Forbidden"
        }), 403;

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': "Resource not found"
        }), 404;


    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': "Method not allowed"
        }), 405;



    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': "Internal server error"
        }), 500;

    @app.errorhandler(501)
    def not_implemented(error):
        return jsonify({
            'success': False,
            'error': 501,
            'message': "Not implemented"
        }), 501;

    @app.errorhandler(502)
    def bad_gateway(error):
        return jsonify({
            'success': False,
            'error': 502,
            'message': "Bad gateway"
        }), 502;

    @app.errorhandler(503)
    def service_unavailable(error):
        return jsonify({
            'success': False,
            'error': 503,
            'message': "Service unavailable"
        }), 503;

    @app.errorhandler(504)
    def gateway_timeout(error):
        return jsonify({
            'success': False,
            'error': 504,
            'message': "Gateway timeout"
        }), 504;

    return app

