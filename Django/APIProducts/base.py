import requests


def get():
    end_point = "http://localhost:8000/"
    response = requests.get(end_point)

    print(response.text)


def post():
    end_point = "http://localhost:8000/"

    json_data = {
        "title": "Product Title Test 2",
        "content": "Product Content Test 2",
        "price": 12.00
    }

    response = requests.post(end_point, data=json_data)

    print(response.text)


post()