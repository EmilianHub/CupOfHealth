from flask import Blueprint, request
from backend.geolocation.locationService import getCurrentLocation
location = Blueprint("location", __name__)


@location.post("/")
def retrieveCurrentLocation():
    data = request.get_json()
    long = data.get("longitude")
    latit = data.get("latitude")
    return getCurrentLocation(long, latit)
