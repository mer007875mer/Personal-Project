import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "p3"})

print(get_response.text)