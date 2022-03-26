from audioop import add
import os
from fastkml import kml
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

def getCity(geometry):
    geolocator = Nominatim(user_agent="barkpark")
    reverse = RateLimiter(geolocator.reverse, min_delay_seconds=1)

    latitude = str(geometry.y)
    longitude = str(geometry.x)

    # location = geolocator.reverse(latitude + "," + longitude)
    location = reverse(latitude + "," + longitude)
    
    address = location.raw['address']
    
    city = address.get('city', '')
    if (not city):
        city = address.get('town', '')

    return city

dirname = os.path.abspath('.')

FILE = os.path.join(dirname, 'dogparks.kml')

# Read file into string and convert to UTF-8 
with open(FILE, 'rt', encoding="utf-8") as myfile:
    doc = myfile.read()

# Create the KML object to store the parsed result
k = kml.KML()

# Read in the KML string
k.from_string(doc)

features1 = list(k.features())
features2 = list(features1[0].features())
placemarks = list(features2[0].features())

dogparks = []

for placemark in placemarks:
    dogpark = {
        "name": placemark.name,
        "description": placemark.description,
        "geometry": placemark.geometry,
        "city": getCity(placemark.geometry)
    }

    dogparks.append(dogpark)

# geometry.x == longitude
# geometry.y == latitude

# e.g. print longitude
# print(dogparks[0].get("geometry").x)

# for dogpark in dogparks:
#     print(getCity(dogpark.get('geometry')))

print("city: " + dogparks[0].get("city"))



