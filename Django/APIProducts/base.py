import requests

def get_jwt_tokens():
    end_point = "http://localhost:8000/api/token/"

    data = {
        'username': 'erfan',
        'password': 'mer007875mer'
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
            'page': 1,
            'count': 5,
            'title': 'new product'
        }
        response = requests.get(end_point, params=params, headers=headers)
        print("Response:", response.text)

    # Use the access token to retrieve products
    get_products(jwt_tokens.get('access'))

    def post_products(access_token):
        end_point = "http://localhost:8000/api/"

        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        json_data = {
            # "title": "Product Title Test 67",
            "content": "Product Content Test 67",
            "price": 16.00
        }

        response = requests.post(end_point, headers=headers, data=json_data)

        print(response.text)

    # Use the access token to Create products
    # post_products(jwt_tokens.get('access'))
