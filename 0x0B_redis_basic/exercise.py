#!/usr/bin/env python3
"""exercise"""
import uuid
from typing import Union, Optional
from collections.abc import Callable
from functools import wraps
import inspect
import redis


def count_calls(method: Callable) -> Callable:
    """count how many times methods of the Cache class are called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """inner function"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """inner function"""
        name = method.__qualname__
        self._redis.rpush(name + ':inputs', str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(name + ':outputs', output)
        return output
    return wrapper


def replay(func: Callable) -> str:
    """display the history of calls of a particular function"""
    cache = func.__self__
    func_name = func.__qualname__
    counter = cache.get_int(func_name)
    print("{fname} was called {fcounter} times:".format(
        fname=func_name, fcounter=counter))
    list_inputs = cache._redis.lrange(func_name + ':inputs', 0, -1)
    list_outputs = cache._redis.lrange(func_name + ':outputs', 0, -1)

    for input, output in zip(list_inputs, list_outputs):
        print("{fname}(*{finput}) -> {foutput}".format(
            fname=func_name,
            finput=input.decode("utf-8"),
            foutput=output.decode("utf-8")
        ))


class Cache:
    """cache class"""
    def __init__(self):
        """Initiliaze a Cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a key, store the input data in Redis and return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
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
