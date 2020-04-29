from django.conf import settings
import redis

REDIS_INSTANCE = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    password=settings.REDIS_PASSWORD,
    charset='utf-8',
    db=0,
    decode_responses=True)
