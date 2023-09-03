from rest_framework.response import Response
from .messages import get_status_message


def response_structure(status_code, entries):
    data = {
        "returns": {
            "status": status_code,
            "message": get_status_message(status_code)
        },
        "entries": entries
    }
    return Response(data, status=status_code)
