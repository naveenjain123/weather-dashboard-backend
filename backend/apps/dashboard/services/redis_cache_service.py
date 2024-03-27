from backend import settings
from backend.helper.redis_helper import RedisCachingService


class RedisCacheService:
    def __init__(self, request=None):
        self.request = request
        self.redis_cache_service = RedisCachingService(
            cache_host=settings.REDIS_HOST,
            cache_db=settings.REDIS_DB,
            cache_key_prefix=f"{settings.SESSION_DOMAIN_NAME}:1:{settings.REDIS_CACHE_PREFIX}",
            cache_key_suffix=None,
        )

    def build_cache_with_args(self, key, data, **kwargs):
        self.redis_cache_service._create_or_update_object_from_redis_by_key(
            key, data
        )
