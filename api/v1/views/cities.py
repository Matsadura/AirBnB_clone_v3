#!/usr/bin/python3
""" A view for City objects that hands all default RESTFul API actions """
from api.v1.views import app_views
from models.state import State
from models.city import City
from models import storage
from flask import jsonify, request, abort


@app_views.route('/cities/<city_id>', methods=['GET', 'DELETE', 'PUT'])
def cities(city_id):
    """Retrives a City object during GET Method"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    if request.method == 'GET':
        city = storage.get(City, city_id)
        return jsonify(city.to_dict())

    if request.method == 'DELETE':
        storage.delete(city)
        storage.save()
        return {}, 200

    if request.method == 'PUT':
        try:
            data = request.get_json()
        except Exception as e:
            abort(400, 'Not a JSON')
        skippable = ['id', 'created_at', 'updated_at']
        for k, v in data.items():
            if k not in skippable:
                setattr(city, k, v)
        storage.save()
        return jsonify(city.to_dict()), 200


@app_views.route('/states/<state_id>/cities', methods=['GET', 'POST'])
def state_id_cities(state_id):
    """Retrieves all City objects of a State object during GET Method"""
    obj = storage.get(State, state_id)
    if not obj:
        abort(404)
    if request.method == 'GET':
        cities = [city.to_dict() for city in obj.cities]
        return jsonify(cities)

    # TO CHECK WHY STATE_ID IS NULL
    if request.method == 'POST':
        try:
            data = request.get_json()
            data['state_id'] = state_id
        except Exception as e:
            abort(400, 'Not a JSON')
        if 'name' not in data.keys():
            abort(400, 'Missing name')
        obj = City(**data)
        storage.new(obj)
        storage.save()
        return jsonify(obj.to_dict()), 201
