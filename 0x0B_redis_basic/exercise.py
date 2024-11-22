#!/usr/bin/env python3
"""exercise"""
import uuid
from typing import Union
import redis


class Cache:
    """cache class"""
    def __init__(self):
        """Initiliaze a Cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a key, store the input data in Redis and return the key"""
        key = str(uuid.uuid4())
        cache = Cache()
        cache._redis.set(key, data)
        return key
