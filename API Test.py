import requests 
test = input()

response = requests.get(f'https://api.datamuse.com/words?sl={test}')
data = response.json()
print(data)