#!/usr/bin/python3
""" A view for State objects that hands all default RESTFul API actions """
from api.v1.views import app_views
from models.state import State
from models import storage
from flask import jsonify, request, abort
from werkzeug.exceptions import BadRequest


@app_views.route('/states', methods=['GET', 'POST'])
def states():
    """Retrives the list of all State objects during GET Method"""
    if request.method == 'GET':
        states = storage.all(State).values()
        states_list = [state.to_dict() for state in states]
        return jsonify(states_list)

    if request.method == 'POST':
        try:
            data = request.get_json()
        except Exception as e:
            abort(400, 'Not a JSON')
        if 'name' not in data.keys():
            abort(400, 'Missing name')
        obj = State(**data)
        storage.new(obj)
        storage.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'])
def state_id(state_id):
    """Retrieves a State object during GET Method"""
    obj = storage.get(State, state_id)
    if request.method == 'GET':
        if not obj:
            abort(404)
        return jsonify(obj.to_dict())

    if request.method == 'DELETE':
        if not obj:
            abort(404)
        storage.delete(obj)
        storage.save()
        return {}, 200

    if request.method == 'PUT':
        if not obj:
            abort(404)
        try:
            data = request.get_json()
        except Exception as e:
            abort(400, 'Not a JSON')
        skippable = ['id', 'created_at', 'updated_at']
        for k, v in data.items():
            if k not in skippable:
                setattr(obj, k, v)
        storage.save()
        return jsonify(obj.to_dict()), 200
