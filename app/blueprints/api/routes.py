from flask import jsonify, request
from . import api
from app.models import Notes

@api.route('/')
def index():
    return 'Hello API here'

@api.route('/notes')
def get_posts():
    posts = ['post 1']
    return jsonify(posts)

# 1:30 week 8 pm
