from functools import wraps
from flask import session, abort

def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		#verify if user is logged in
		if not(session.get('username')):
			abort(401)
		return f(*args, **kwargs)
	return decorated_function

def admin_required(f):
	@wraps(f)
	@login_required
	def decorated_function(*args, **kwargs):
		#verify if user is admin
		if session.get('role_name') != 'admin':
			abort(403)
	return decorated_function