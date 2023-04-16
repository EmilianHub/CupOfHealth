from flask import Blueprint, request
from locationService import getCurrentLocation
import jwtService
location = Blueprint("location", __name__)


@location.post("/")
def retrieveCurrentLocation():
    data = jwtService.decodeRequest(request.get_data())
    long = data.get("longitude")
    latitude = data.get("latitude")
    return jwtService.encodeResponse(getCurrentLocation(long, latitude))
