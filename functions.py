import requests

def Search_API(APIKey, location, referenceType):
    response = requests.get(f'http://api.weatherapi.com/v1/{referenceType}.json?key={APIKey}&q={location}')
    locationData = response.json()
    return locationData

