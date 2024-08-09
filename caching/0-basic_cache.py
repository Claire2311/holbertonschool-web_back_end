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
        if key not in self.cache_data or key not in self.cache_data:
            return None
        return self.cache_data[key]


my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
