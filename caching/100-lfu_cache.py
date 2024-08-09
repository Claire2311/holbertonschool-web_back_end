#!/usr/bin/env python3
""" LFU caching
"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """extends the BaseCaching class"""
    def __init__(self):
        super().__init__()
        self.cache_data = {}
        self.use_dictionnary = {}

    def put(self, key, item):
        """add key/value in the dictionnary"""
        if not key or not item:
            return

        if key in self.use_dictionnary:
            val = self.use_dictionnary.pop(key)
            self.use_dictionnary[key] = val + 1

        if key in self.cache_data:
            self.cache_data.pop(key)
            self.cache_data[key] = item

        if key not in self.cache_data and \
                len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            key_to_delete = min(self.use_dictionnary,
                                key=self.use_dictionnary.get)
            print("DISCARD: {}".format(key_to_delete))
            self.use_dictionnary.pop(key_to_delete)
            self.cache_data.pop(key_to_delete)

        self.cache_data[key] = item

        if key not in self.use_dictionnary:
            self.use_dictionnary[key] = 1

    def get(self, key):
        """get value according to the given key"""
        if key not in self.cache_data or key is None:
            return None

        val = self.use_dictionnary[key]
        self.use_dictionnary[key] = val + 1

        return self.cache_data[key]
