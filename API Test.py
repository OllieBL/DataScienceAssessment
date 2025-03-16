import requests 

location = input('location')

response = requests.get(f'http://api.weatherapi.com/v1/current.json?key=ce4a77e373334af9aa8221317250903&q={location}')
data = response.json()
print(data)