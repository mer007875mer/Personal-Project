from django.http.response import HttpResponseForbidden


class Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before

        if False:
            return HttpResponseForbidden("Access Denied")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        return response