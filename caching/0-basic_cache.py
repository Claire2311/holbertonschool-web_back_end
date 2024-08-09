#!/usr/bin/env python3
""" Create a basic dictionnary
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """extends the BaseCaching class"""
    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """add key/value in the dictionnary"""
        if not key or not item:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """get value according to the given key"""
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data[key]
