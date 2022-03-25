import requests

url ="xd"
response = requests.get(url)
print(response.status_code)