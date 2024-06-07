#!/usr/bin/python3
""" A view for Place objects that hands all default RESTFul API actions """
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.place import Place
from models import storage
from werkzeug.exceptions import BadRequest

@app_views.route("/cities/<city_id>/places", methods=["GET", "POST"])
def places(city_id):
    """ handles request made to places api """
    if request.method == 'GET':
        city = storage.get("City", str(city_id))
        if city is None:
            abort(404)
        places_list = [place.to_dict() for place in city.places]
        return jsonify(places_list)
    elif request.method == 'POST':
        place_json = request.get_json(silent=True)
        if place_json is None:
            abort(400, 'Not a JSON')
        if not storage.get("City", str(city_id)):
            abort(404)
        if not storage.get("User", place_json["user_id"]):
            abort(404)
        if "user_id" not in place_json:
            abort(400, 'Missing user_id')
        if "name" not in place_json:
            abort(400, 'Missing name')

        place_json["city_id"] = city_id
        new_place = place(**place_json)
        new_place.save()

        return jsonify(new_place.to_dict()), 201


@app_views.route("/places/<place_id>",  methods=["GET", "DELETE", "PUT"])
def places_by_id(place_id):
    """ Gets a specific place by its id """
    if request.method == 'GET':
        place = storage.get("Place", str(place_id))
        if place in None:
            abort(404)
            return jsonify(place.to_dict())
    elif request.method == 'DELETE':
        place = storage.get("Place", str(place_id))
        if place in None:
            abort(404)
        storage.delete(place)
        storage.save()
        return jsonify({}), 200
    elif request.method == 'PUT':
        place_json = request.get_json(silent=True)

        if place_json is None:
            abort(404)

        place = storage.get("Place", str(place_id))
        if place is None:
            abort(404)

        for key, value in place_json.items():
            if key not in ["id", "created_at", "updated_at", "user_id", "city_id"]:
                setattr(place, key, value)

        place.save()
        return jsonify(place.to_dict())


