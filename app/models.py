from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    '''
    Function that handles logged in users in each user session
    '''
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    '''
    Class that define user instance with its attributes
    Args:
        This user class inherits from db.model in flask-sqlalchemy base class
    Returns:
        Instances are created as instances of the db.column
        __repr__ method tells python how to print objects of this class
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        '''
        Function that prints out user information
        '''
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        '''
        Function that create a user password
        Args: password
        Retruns:
            encrypted password to be save in database
        '''
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        '''
        Function to check user password aganist the stored hash password
        Args:
            User password
        Returns:
            Confirm user password(more of a boolean)
        '''
        return check_password_hash(self.password_hash, password)

class Pitch(db.Model):
    '''
    Class that defines pitch instance made by users
    Args:
        Timestamp: To help retrive pitch in order and set as default to keep record of user posting
        user_id variable references user id(one to many db relationship)
    Returns:
        Users timestamp as at the time they created pitch messages
    '''
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Pitch {}>'.format(self.body)
    
