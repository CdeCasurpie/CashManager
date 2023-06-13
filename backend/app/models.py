from flask_sqlalchemy import SQLAlchemy
from config.local import config
import uuid
from datetime import datetime

db = SQLAlchemy()

def setup_db(app, database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = config['DATABASE_URI'] if database_path is None else database_path
    db.app = app
    db.init_app(app)
    db.create_all()


# - Role model, with the fields: name and description.

class Role(db.Model):
    __tablename__ = 'roles'

    name = db.Column(db.String(80), primary_key=True)
    description = db.Column(db.String(200), nullable=False)


# - User model, with the fields: username and password.

class User(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(200), nullable=False)

    role_name = db.Column(db.String(80), db.ForeignKey('roles.name'), nullable=False)

    def serialize(self):
        return {
            'username': self.username,
            'role_name': self.role_name
        }

# - Expense model, with the fields: username, date, value, description and category_name.

class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    
    date = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    value = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(80), nullable=True)
    
    username = db.Column(db.String(80), db.ForeignKey('users.username'), nullable=False)
    category_id = db.Column(db.String(36), db.ForeignKey('categories.id'), nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'value': self.value,
            'description': self.description,
            'username': self.username,
            'category_id': self.category_id
        }


# - Budget model, with the fields: id, username, value, start_date, end_date.

class Budget(db.Model):
    __tablename__ = 'budgets'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    
    value = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=True)

    username = db.Column(db.String(80), db.ForeignKey('users.username'), nullable=False)



# - Saving model, with the fields: username, date and value.

class Saving(db.Model):
    __tablename__ = 'savings'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    date = db.Column(db.DateTime, default=lambda: datetime.now(), nullable=False)
    value = db.Column(db.Float, nullable=False, default=0.0)

    username = db.Column(db.String(80), db.ForeignKey('users.username'))


# - Category model, with the fields: name and username.

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), db.ForeignKey('users.username'))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username
        }