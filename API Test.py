import requests 

location = input('location')

response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key=b2b6f09cd9d943fdab584210251803&q={location}&days=2')
data = response.json()
print(data)