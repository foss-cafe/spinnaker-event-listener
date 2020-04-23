from flask import Blueprint
from flask_restful import Api
from resources.health import HealthCheck
from resources.eventlistner import EventListner


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(HealthCheck, '/health')
api.add_resource(EventListner, '/events/')
