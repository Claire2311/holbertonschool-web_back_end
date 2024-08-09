#!/usr/bin/env python3
""" MRU caching
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """extends the BaseCaching class"""
    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """add key/value in the dictionnary"""
        if not key or not item:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
            self.cache_data[key] = item

        if key not in self.cache_data and \
                len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(list(self.cache_data)[-1]))
            self.cache_data.popitem()

        self.cache_data[key] = item

    def get(self, key):
        """get value according to the given key"""
        if key not in self.cache_data or key is None:
            return None

        val = self.cache_data.pop(key)
        self.cache_data[key] = val

        return self.cache_data[key]
