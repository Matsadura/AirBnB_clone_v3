#!/usr/bin/python3
"""A view for Amenity objects with link to Places objects"""
from flask import jsonify, abort, request
from models import storage
from api.v1.views import app_views
from os import getenv
from models.place import Place
from models.amenity import Amenity


@app_views.route("/places/<place_id>/amenities", methods=["GET"])
def amenity_of_place(place_id):
    """ Retrieves amenity of a place """
    obj = storage.get(Place, place_id)

    if obj is None:
        abort(404)

    amenities = [amenity.to_dict() for amenity in obj.amenities]
    return jsonify(amenities)


@app_views.route("/places/<place_id>/amenities/<amenity_id>",
                 methods=["DELETE", "POST"])
def remove_amenity_from_place(place_id, amenity_id):
    """ Deletes an amenity in a place """
    if not storage.get(Place, place_id):
        abort(404)

    if not storage.get(Amenity, amenity_id):
        abort(404)

    if request.method == 'DELETE':
        objects = storage.get(Place, place_id)
        flag = 0

        for obj in objects.amenities:
            if str(obj.id) == amenity_id:
                if getenv("HBNB_TYPE_STORAGE") == "db":
                    objects.amenities.remove(obj)
                else:
                    objects.amenity_ids.remove(obj.id)
                objects.save()
                flag = 1
                break

        if flag == 0:
            abort(404)
        else:
            return jsonify({}), 200

    elif request.method == 'POST':
        place_obj = storage.get(Place, place_id)
        amenity_obj = storage.get(Amenity, amenity_id)
        amenity_found = None

        for obj in place_obj.amenities:
            if str(obj.id) == amenity_id:
                amenity_found = obj
                break

        if amenity_found is not None:
            return jsonify(amenity_found.to_dict()), 200

        if getenv("HBNB_TYPE_STORAGE") == "db":
            place_obj.amenities.append(amenity_obj)
        else:
            place_obj.amenities = amenity_obj

        place_obj.save()

        return jsonify(amenity_obj.to_dict()), 201
