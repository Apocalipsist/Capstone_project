from flask import Blueprint, json


api = Blueprint('api', __name__, url_prefix='/api')



from . import routes, apikey, auth