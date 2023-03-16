from geopy.geocoders import Nominatim

geoLoc = Nominatim(user_agent="CupOfHealth")


def getCurrentLocation(longitude: str, latitude: str):
    query = f"{latitude}, {longitude}"
    loc = geoLoc.reverse(query)
    return loc.raw
