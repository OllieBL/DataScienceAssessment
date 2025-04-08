import requests

def CurrentAPISearch(APIKey, location):
    try:
        response = requests.get(f'http://api.weatherapi.com/v1/current.json?key={APIKey}&q={location}')
        locationData = response.json()
        assert 'location' in locationData
        return locationData
    except:
        return 'error'

def ForecastAPISearch(APIKey, location):
    try:
        response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={APIKey}&q={location}&days=3')
        locationData = response.json()
        return locationData
    except:
        return ['error']

def HistoryAPISearch(APIKey, location, date):
    try:
        response = requests.get(f'http://api.weatherapi.com/v1/history.json?key={APIKey}&q={location}&date={date}')
        locationData = response.json()
        return locationData
    except:
        return ['error']


def listifyCurrent(locationData):
    try:
        out = [[],[]]
        for i in locationData.values():
            for j in i:
                out[0].append(j)
                out[1].append(i[j])

        return out
    except:
        return ['error']

def listifyForecast(locationData):
    try:
        out = [[[],[[],[],[]]],[]]
        firstToggle = -1
        locationDataDay = locationData['forecast']['forecastday']
        numberLoops = -1
        for i in locationDataDay:
            firstToggle += 1
            for j in i['day']:
                if firstToggle < 1:
                    out[0][0].append(j)
                out[0][1][firstToggle].append(i['day'][j])
        
        for i in locationDataDay:
            for j in i['hour']:
                out[1].append([])
                numberLoops += 1
                for x in j:
                    out[1][numberLoops].append(j[x])

        return out
    except:
        return ['error']

def listifyHistory(locationData):
    try:
        out = [[[],[]],[]]
        locationDataDay = locationData['forecast']['forecastday']
        numberLoops = -1
        for i in locationDataDay[0]['day']:
            out[0][0].append(i)
            out[0][1].append(locationDataDay[0]['day'][i])
        for i in locationDataDay[0]['hour']:
            out[1].append([])
            numberLoops += 1
            for j in i:
                out[1][numberLoops].append(i[j])
        
        return out
    except:
        return ['error']