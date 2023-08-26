from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def get_location(address):
    geolocator = Nominatim(user_agent="location_app")
    location = geolocator.geocode(address)
    return location.latitude, location.longitude

def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

if __name__ == "__main__":
    
    address1 = "1600 Amphitheatre Parkway, Mountain View, CA"
    address2 = "1 Infinite Loop, Cupertino, CA"

    coord1 = get_location(address1)
    coord2 = get_location(address2)

    distance = calculate_distance(coord1, coord2)
    print(f"Distance between the two locations: {distance:.2f} km")
