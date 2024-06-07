#!/usr/bin/python3
""" A view for Amenity objects that hands all default RESTFul API actions """
from api.v1.views import app_views
from models.amenity import Amenity
from models import storage
from flask import jsonify, request, abort


@app_views.route('/amenities', methods=['GET', 'POST'])
def amenities():
    """Retrieves all Amenity objects in GET request"""
    amenities = storage.all(Amenity).values()

    if request.method == 'GET':
        amenities = [amenity.to_dict() for amenity in amenities]
        return jsonify(amenities)

    if request.method == 'POST':
        try:
            data = request.get_json()
        except Exception as e:
            abort(400, 'Not a JSON')
    if 'name' not in data.keys():
        abort(400, 'Missing name')
    obj = Amenity(**data)
    storage.new(obj)
    storage.save()
    return jsonify(obj.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['GET', 'PUT'])
def amenity_id(amenity_id):
    """Retrieve an Amenity object in GET Request"""
    obj = storage.get(Amenity, amenity_id)

    if request.method == 'GET':
        if not obj:
            abort(404)
        return jsonify(obj.to_dict()), 200

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
