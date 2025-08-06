from geopy.geocoders import  Nominatim

def get_location_name(latitude, longitude):
    geolocatir = Nominatim(user_agent="my_app")
    loction = geolocatir.reverse(f"{latitude}, {longitude}")
    return loction.address

# print(get_location_name())
