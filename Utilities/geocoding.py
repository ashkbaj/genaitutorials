import urllib.parse
import requests


Forward_Geocode= "https://geocode.maps.co/search?q=address&api_key=api_key"

Reverse_Geocode= "https://geocode.maps.co/reverse?lat=latitude&lon=longitude&api_key=api_key"
apikey = "665579c8adeee393327428korab6552"
format = "json"


address = "5, Dhenugambal Nagar, Madambakkam, chennai - 600073."
url_encoded_address = "5%2C+Dhenugambal+Nagar%2C+Madambakkam%2C+chennai+-+600+073."

safe_string = urllib.parse.quote_plus(address)


geocoding_url = f"https://geocode.maps.co/search?q={safe_string}&api_key={apikey}&format={format}"
print(geocoding_url)

response = requests.get(geocoding_url)
print(response.json())


## Get the value of current lat long for the current location
import geocoder
g = geocoder.ip('me')
print(g.latlng)