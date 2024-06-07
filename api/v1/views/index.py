#!/usr/bin/python3
""" Contains API Routes """
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """ Returns the api status all wrapped in a json object """
    
    return {"status": "OK"}, 200


@app_views.route('/stats')
def stats():
    """ Retrives the number of each object by type"""
    from models import storage
    from models.city import City
    from models.user import User
    from models.amenity import Amenity
    from models.place import Place
    from models.state import State
    from models.review import Review

    return {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
