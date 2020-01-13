"""
alright first things first:

I know the prompt said to use google api, but it requires billing information.

And I aint about that life. So we're using geopy

-- if you wanted to use Google --
using google api is just a matter of using python requests module.

idea is you just use requests to get submit a url with params for the adress
and then you'd parse the json it hands you back.

ez pz, but also billing. so no thanks.
"""
from geopy.geocoders import Nominatim

class GeoPoint:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

def get_lat_lon_from_address(address_str):

    geolocator = Nominatim()
    location = geolocator.geocode(address_str)

    if location is None:
        return GeoPoint(None, None)
    else:
        return GeoPoint(location.latitude, location.longitude)
