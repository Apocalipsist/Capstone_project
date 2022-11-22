from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True) 
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    date_created =db.Column(db.DateTime, nullable=False, default=datetime.utcnow) #ALWAYS store data as UTC time. Universal Time
    workout = db.relationship('Workouts', backref='author', lazy='dynamic')
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        # Set password to the hashed version of the password
        self.set_password(kwargs.get('password', ''))
        # Add and Committhe new instance to the database
        db.session.add(self)
        db.session.commit()
        
    def __str__(self):
        return self.username
        
        
    def set_password(self, plain_password):
        self.password = generate_password_hash(plain_password)
    
    def check_password(self, password_guess):
        return check_password_hash(self.password, password_guess)
        
@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Workouts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(255), nullable=False)
    date_created =db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # SQL equivalent to FOREIGN KEY(user_id) REFERNCES user_id
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()