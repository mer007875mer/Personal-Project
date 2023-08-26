import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
userpass = {
    'username': 'erfan',
    'password': getpass()
}
auth_response = requests.post(auth_endpoint, json=userpass)
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    endpoint = "http://localhost:8000/api/products/"
    headers = {
        "Authorization": f"Token {token}"
    }
    get_response = requests.post(endpoint, headers=headers, json={"title": "token-test"})
    print(get_response.text)