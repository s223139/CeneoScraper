import requests

url ="https://www.ceneo.pl/91714422"
response = requests.get(url)

print(response.status_code)