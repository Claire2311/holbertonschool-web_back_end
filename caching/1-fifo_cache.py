#!/usr/bin/env python3
""" FIFO caching
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """extends the BaseCaching class"""
    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """add key/value in the dictionnary"""
        if not key or not item:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(next(iter(self.cache_data))))
            self.cache_data.pop(next(iter(self.cache_data)))

    def get(self, key):
        """get value according to the given key"""
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data[key]
