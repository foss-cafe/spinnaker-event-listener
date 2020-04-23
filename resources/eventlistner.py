from flask_restful import Resource
from flask import jsonify, request


class EventListner(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        print(json_data)
        return json_data, 200
