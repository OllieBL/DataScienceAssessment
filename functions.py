import requests

def CurrentAPISearch(APIKey, location):
    response = requests.get(f'http://api.weatherapi.com/v1/current.json?key=b2b6f09cd9d943fdab584210251803&q={location}')
    locationData = response.json()
    return locationData

def ForecastAPISearch(APIKey, location):
    response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key=b2b6f09cd9d943fdab584210251803&q={location}&days=1')
    locationData = response.json()
    return locationData

def HistoryAPISearch(APIKey, location, date):
    response = requests.get(f'http://api.weatherapi.com/v1/history.json?key={APIKey}&q={location}&date=2025-{date[0]}-{date[1]}')
    locationData = response.json()
    return locationData


def listifyCurrent(locationData):
    out = [[],[]]
    locationData['current'].pop('condition')
    for i in locationData.values():
        for j in i:
            out[0].append(j)
            out[1].append(i[j])

    return out

def listifyForecast(locationData):
    out = [[],[]]
    locationDataDay = [locationData['forecast']['forecastday']]
    for i in locationDataDay:
        for j in i['day']:
            out[0].append(j)
            out[1].append(i['day'][j])
        
        
        '''
        for j in i:
            currentList = [[],[]]
            for x in j['day'].values():
                for y in i:
                    currentList[0].append(y)
                    currentList[1].append(x[y])
            for k in currentList[1]:
                out[1].append(k)
        '''

    return out

print(listifyForecast(ForecastAPISearch('', 'Terrigal')))