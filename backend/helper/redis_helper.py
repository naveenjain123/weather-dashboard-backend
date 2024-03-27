# Common Function
import pickle

import redis
from django.conf import settings
from django.core.cache import cache
from rest_framework.response import Response

from backend.helper.common_helper import Singleton
from backend.helper.logging_helper import Logger

logger = Logger(__name__)


class RedisCachingService(metaclass=Singleton):
    def __init__(self, *args, **kwargs):
        self.cache_key_prefix = kwargs.get("cache_key_prefix")
        self.cache_key_suffix = kwargs.get("cache_key_suffix")
        self.cache_db = kwargs.get("cache_db")
        self.cache_host = kwargs.get("cache_host")
        r = redis.from_url(f"redis://{self.cache_host}:6379/{self.cache_db}")
        self.redis_client = r

    def _get_key(self, key):
        cache_key_full = f"{key}"
        if self.cache_key_prefix:
            cache_key_full = f"{self.cache_key_prefix}_{key}"

        if self.cache_key_suffix:
            cache_key_full = (
                f"{self.cache_key_prefix}_{key}_{self.cache_key_suffix}"
            )

        return cache_key_full

    def _get_object_from_redis_by_key(self, key, **kwargs):
        cache_key_full = f"{key}"
        if self.cache_key_prefix:
            cache_key_full = f"{self.cache_key_prefix}_{key}"

        if self.cache_key_suffix:
            cache_key_full = (
                f"{self.cache_key_prefix}_{key}_{self.cache_key_suffix}"
            )

        data = self.redis_client.get(cache_key_full)
        if data is not None:
            try:
                data = pickle.loads(data)
            except Exception as e:
                logger.log_exception("JSON Decode Error")
        return data

    def _create_or_update_object_from_redis_by_key(self, key, data):
        cache_key_full = f"{key}"
        if self.cache_key_prefix:
            cache_key_full = f"{self.cache_key_prefix}_{key}"

        if self.cache_key_suffix:
            cache_key_full = (
                f"{self.cache_key_prefix}_{key}_{self.cache_key_suffix}"
            )
        if data is not None:
            try:
                data = pickle.dumps(data)
            except Exception as e:
                logger.log_exception("JSON Decode Error")
        self.redis_client.set(cache_key_full, data, settings.MAX_CACHE_TIMEOUT)
        # return data
        return True

    def _delete_object_from_redis_by_key(self, key, **kwargs):
        cache_key_full = f"{key}"
        if self.cache_key_prefix:
            cache_key_full = f"{self.cache_key_prefix}_{key}"

        if self.cache_key_suffix:
            cache_key_full = (
                f"{self.cache_key_prefix}_{key}_{self.cache_key_suffix}"
            )

        self.redis_client.delete(cache_key_full)
        return True


class CachedMixin:
    """
    A mixin class to cache responses for API views.

    Attributes:
    CACHE_TIMEOUT (int): The timeout period for caching in seconds. Default is 30 days (60*60*24*30).
    WHITE_LIST_PARAMS (list): List of parameters that need to be included in the cached path.

    Methods:
    get(self, request, *args, **kwargs): Overrides the get method to implement caching logic.
    """

    CACHE_TIMEOUT = 60 * 60 * 24 * 30  # 30 days
    WHITE_LIST_PARAMS = (
        []
    )  # Please add param that need to be included in cached.

    def get(self, request, *args, **kwargs):
        """
        Overrides the get method to implement caching logic.

        Args:
            request (Request): The request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The response object.
        """
        flag = request.query_params.get("flag", None)
        cached_data = None
        path = request.path + "?"

        for param in self.WHITE_LIST_PARAMS:
            if param in request.query_params:
                path += param + "=" + request.query_params[param] + "&"

        if flag not in ["1", "true", "True"]:
            # Check if the data is already cached
            cached_data = cache.get(path)

        if cached_data:
            # If data is cached, return it
            return Response(cached_data)
        response = super().get(request, *args, **kwargs)
        cache.set(path, response.data, timeout=self.CACHE_TIMEOUT)
        return response
