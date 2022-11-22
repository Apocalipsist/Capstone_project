import requests
import json
from pprint import pprint

url = 'https://wger.de/api/v2/'
data = '{"key": "value"}'
headers = {'Accept': 'application/json', 
           'Authorization': 'Token 1234....'}
r = requests.patch(url=url, data=data, headers=headers)
r
r.content
pprint(json.loads(r.content))
