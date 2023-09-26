from MovieSite import settings

import requests


base_url = settings.BASE_API_URL
api_Key = settings.API_KEY


# ---- Fetch Data of the TMDB database to search the available movie ----#
class AddItemList:
    def __init__(self, page, query_name=None, release_year=None, lang=None):
        self.url = f"{base_url}search/movie"
        self.api_key = api_Key
        self.release_year = release_year
        self.page = page
        self.query_params = {
            "query": query_name,
            "page": self.page,
            "language": lang
        }

        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {settings.API_KEY}"
        }

    def get_movie_result(self):

        url = f"{base_url}search/movie"
        self.query_params["primary_release_year"] = self.release_year
        movie_query_params = self.query_params

        try:
            response = requests.get(url, headers=self.headers, params=movie_query_params)
            response = response.json()
            return response
        except requests.ConnectionError:
            return 600

    def get_movie_result_popular(self):

        url = f"{base_url}movie/popular"
        movie_query_params = {"page": self.page}

        try:
            response = requests.get(url, headers=self.headers, params=movie_query_params)
            response = response.json()
            return response
        except requests.ConnectionError:
            return 600

    def get_series_result(self):
        url = f"{base_url}search/tv"
        self.query_params["first_air_date_year"] = self.release_year
        series_query_params = self.query_params

        try:
            response = requests.get(url, headers=self.headers, params=series_query_params)
            response = response.json()
            return response
        except requests.ConnectionError:
            return 600

    def get_series_result_popular(self):

        url = f"{base_url}tv/top_rated"
        movie_query_params = {"page": self.page}

        try:
            response = requests.get(url, headers=self.headers, params=movie_query_params)
            response = response.json()
            return response
        except requests.ConnectionError:
            return 600


class AddItem:
    def __init__(self, id):
        self.url = f"{base_url}search/movie"
        self.api_key = api_Key
        self.id = id

        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {settings.API_KEY}"
        }

    def get_movie_detail(self):

        url = f"{base_url}movie/{self.id}?language=fa"

        try:
            response = requests.get(url, headers=self.headers)
            response = response.json()
            return response
        except requests.ConnectionError:
            return 600

    def get_movie_credit(self):

        url = f"{base_url}movie/{self.id}/credits"

        try:
            response = requests.get(url, headers=self.headers)
            response = response.json()
            return response
        except requests.ConnectionError:
            return 600