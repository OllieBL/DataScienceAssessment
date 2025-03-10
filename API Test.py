import requests 
year = int(input('year'))
month = int(input('month'))
day = int(input('day'))

location = input('location')

response = requests.get(f'http://api.weatherapi.com/v1/history.json?key=ce4a77e373334af9aa8221317250903&q={location}&dt={year}-{month}-{day}')
data = response.json()
print(data)