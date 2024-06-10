#!/usr/bin/python3
""" A view for Place objects that hands all default RESTFul API actions """
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models import storage


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
        if "user_id" not in place_json:
            abort(400, 'Missing user_id')
        if "name" not in place_json:
            abort(400, 'Missing name')
        if not storage.get("User", place_json["user_id"]):
            abort(404)

        place_json["city_id"] = city_id
        new_place = Place(**place_json)
        new_place.save()

        return jsonify(new_place.to_dict()), 201


@app_views.route("/places/<place_id>",  methods=["GET", "DELETE", "PUT"])
def places_by_id(place_id):
    """ Gets a specific place by its id """
    if request.method == 'GET':
        place = storage.get("Place", str(place_id))
        if place is None:
            abort(404)
        return jsonify(place.to_dict())
    elif request.method == 'DELETE':
        place = storage.get("Place", str(place_id))
        if place is None:
            abort(404)
        storage.delete(place)
        storage.save()
        return jsonify({}), 200
    elif request.method == 'PUT':
        place_json = request.get_json(silent=True)

        if place_json is None:
            abort(400, 'Not a JSON')

        place = storage.get("Place", str(place_id))
        if place is None:
            abort(404)
        skippable = ["id", "created_at", "updated_at", "user_id", "city_id"]

        for key, value in place_json.items():
            if key not in skippable:
                setattr(place, key, value)

        place.save()
        return jsonify(place.to_dict())


@app_views.route("/places_search", methods=["POST"])
def places_search():
    """

    Retrieves all Place objects
    depending of the JSON
    in the body of the request

    """
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')

    if data and len(data):
        states = data.get('states', None)
        cities = data.get('cities', None)
        amenities = data.get('amenities', None)

    if not data or not len(data) or (
            not states and
            not cities and
            not amenities):
        places = storage.all(Place).values()
        list_places = [place.to_dict() for place in places]
        return jsonify(list_places)

    list_places = []
    if states:
        states_obj = [storage.get(State, state_id) for state_id in states]
        for state in states_obj:
            if state:
                for city in state.cities:
                    if city:
                        for place in city.places:
                            list_places.append(place)

    if cities:
        city_obj = [storage.get(City, city_id) for city_id in cities]
        for city in city_obj:
            if city:
                for place in city.places:
                    if place not in list_places:
                        list_places.append(place)
    if amenities:
        if not list_places:
            list_places = storage.all(Place).values()
        amenities_obj = [storage.get(Amenity, a_id) for a_id in amenities]
        list_places = [
            place for place in places
            if all(
                [amenity in place.amenities
                 for amenity in amenities_obj])]

    places = []
    for pl in list_places:
        d = pl.to_dict()
        d.pop('amenities', None)
        places.append(d)
    return jsonify(places)
