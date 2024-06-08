#!/usr/bin/python3
"""A view for Reviews objects that hands all default RESTFul API actions"""
from api.v1.views import app_views
from models.review import Review
from models.place import Place
from models.user import User
from models import storage
from flask import jsonify, request, abort


@app_views.route('/places/<place_id>/reviews', methods=['GET', 'POST'])
def review_of_a_place(place_id):
    """Handles Reviews routes"""
    if request.method == 'GET':
        place = storage.get(Place, place_id)
        if not place:
            abort(404)
        return jsonify([review.to_dict() for review in place.reviews])

    if request.method == 'POST':
        data = request.get_json(silent=True)
        if not data:
            abort(400, 'Not a JSON')
        if 'user_id' not in data.keys():
            abort(400, 'Missing user_id')
        user = storage.get(User, data["user_id"])
        if not user:
            abort(404)
        if 'text' not in data.keys():
            abort(400, 'Missing text')

        if not storage.get(Place, place_id):
            abort(404)

        # In case the place_id is not included in the request body
        data['place_id'] = place_id

        review = Review(**data)
        storage.new(review)
        storage.save()
        return jsonify(review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['GET', 'DELETE', 'PUT'])
def review_id(review_id):
    """Handles single review object"""
    obj = storage.get(Review, review_id)

    if request.method == 'GET':
        if not obj:
            abort(404)
        return jsonify(obj.to_dict())

    if request.method == 'DELETE':
        if not obj:
            abort(404)
        storage.delete(obj)
        storage.save()
        return jsonify({}), 200

    if request.method == 'PUT':
        if not obj:
            abort(404)
        data = request.get_json(silent=True)
        if not data:
            abort(400, 'Not a JSON')
        skippable = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']
        for k, v in data.items():
            if k not in skippable:
                setattr(obj, k, v)
        storage.save()
        return jsonify(obj.to_dict()), 200
