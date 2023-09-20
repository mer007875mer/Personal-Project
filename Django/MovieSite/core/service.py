from MovieSite import settings

import requests


base_url = settings.BASE_API_URL
api_Key = settings.API_KEY


# ---- Fetch Data of the TMDB database to search the available movie ----#
class AddItemList:
    def __init__(self, page, query_name, include_adult=None, release_year=None):
        self.url = f"{base_url}search/movie"
        self.api_key = api_Key
        self.release_year = release_year

        self.query_params = {
            "query": query_name,
            "include_adult": include_adult,
            "page": page,
        }

        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {settings.API_KEY}"
        }

    def get_movie_result(self):

        url = f"{base_url}search/movie"
        self.query_params["primary_release_year"] = self.release_year
        movie_query_params = self.query_params
        response = requests.get(url, headers=self.headers, params=movie_query_params)
        response = response.json()
        result_list = response['results']
        return result_list

    def get_series_result(self):

        url = f"{base_url}search/tv"
        self.query_params["first_air_date_year"] = self.release_year
        series_query_params = self.query_params
        response = requests.get(url, headers=self.headers, params=series_query_params)
        response = response.json()
        result_list = response['results']
        return result_list

