from getpass import getpass
import requests

def get_jwt_tokens():
    end_point = "http://localhost:8000/api/token/"

    data = {
        'username': 'erfan',
        'password': getpass()
    }

    response = requests.post(end_point, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        print("Token request is failed: ", response.text)
        return None

jwt_tokens = get_jwt_tokens()

if jwt_tokens is not None:
    def get_products(access_token):
        end_point = "http://localhost:8000/api/"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        params = {
            'title': 'new product'
        }
        response = requests.post(end_point, data=params, headers=headers)
        print(response.text)

    # Use the access token to retrieve products
    get_products(jwt_tokens['access'])



def post(access_token):
    end_point = "http://localhost:8000/"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    json_data = {
        "title": "Product Title Test 3",
        "content": "Product Content Test 3",
        "price": 12.10
    }

    response = requests.post(end_point, headers=headers, data=json_data)

    print(response.text)


# post()