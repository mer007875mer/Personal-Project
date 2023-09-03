from django.core.cache import cache
from functools import wraps
import logging


def set_log_level(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        log_level = cache.get("loglevel", "INFO")

        logger = logging.getLogger("root")
        logger.setLevel(log_level)

        return view_func(request, *args, **kwargs)

    return wrapper