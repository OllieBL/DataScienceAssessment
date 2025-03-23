import requests

def CurrentAPISearch(APIKey, location):
    response = requests.get(f'http://api.weatherapi.com/v1/current.json?key=b2b6f09cd9d943fdab584210251803&q={location}')
    locationData = response.json()
    return locationData

def ForecastAPISearch(APIKey, location):
    response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={APIKey}&q={location}&days=7')
    locationData = response.json()
    return locationData

def HistoryAPISearch(APIKey, location, date):
    response = requests.get(f'http://api.weatherapi.com/v1/history.json?key={APIKey}&q={location}&date=2025-{date[0]}-{date[1]}')
    locationData = response.json()
    return locationData


def makeDataReadable(locationData):
    out = [[],[]]
    locationData['current'].pop('condition')
    for i in locationData.values():
        for j in i:
            out[0].append(j)
            out[1].append(i[j])

    return out

print(HistoryAPISearch('b2b6f09cd9d943fdab584210251803', 'Terrigal', [3, 20]))