import requests
import matplotlib.pyplot as plt

def CurrentAPISearch(APIKey, location):
    response = requests.get(f'http://api.weatherapi.com/v1/current.json?key=b2b6f09cd9d943fdab584210251803&q={location}')
    locationData = response.json()
    return locationData

def ForecastAPISearch(APIKey, location):
    response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key=b2b6f09cd9d943fdab584210251803&q={location}&days=3')
    locationData = response.json()
    return locationData

def HistoryAPISearch(APIKey, location, date):
    response = requests.get(f'http://api.weatherapi.com/v1/history.json?key=b2b6f09cd9d943fdab584210251803&q={location}&date={date}')
    locationData = response.json()
    return locationData


def listifyCurrent(locationData):
    out = [[],[]]
    for i in locationData.values():
        for j in i:
            out[0].append(j)
            out[1].append(i[j])

    return out

def listifyForecast(locationData):
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

def listifyHistory(locationData):
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