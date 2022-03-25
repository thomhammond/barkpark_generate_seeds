import os
from fastkml import kml

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
        "geometry": placemark.geometry
    }
    dogparks.append(dogpark)

