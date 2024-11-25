#!/usr/bin/env python3
"""exercise"""
import uuid
from typing import Union, Optional
from collections.abc import Callable
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

    def get(self, key: Union[str, int], fn: Optional[Callable] = None):
        """convert data from Redis in the right format"""
        value = self._redis.get(key)
        if value is not None and fn:
            return fn(value)
        else:
            return value

    def get_str(self, key: str) -> str:
        """convert data from Redis in string"""
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """convert data from Redis in integer"""
        return self.get(key, lambda x: int(x.decode("utf-8")))
