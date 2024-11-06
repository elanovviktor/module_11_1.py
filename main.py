import requests
URL = 'https://www.timeapi.io/api/time/current/zone?timeZone=Europe%2FMoscow'

response = requests . get(URL)
data = response . json()

print(data)