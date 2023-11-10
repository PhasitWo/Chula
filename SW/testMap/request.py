import requests
import json

params = {
    'area': 10,
    'limit': 10,
    'keyword': 'chula',
    'key':'fe75c23350d22e5b0ff781a28a09aaf5'
}

response = requests.get(
    url = 'https://search.longdo.com/mapsearch/json/search?',
    params=params
)

d = json.loads(response.text)
print(d)
 