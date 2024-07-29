#!/usr/bin/env python3
"""
function that take a string and an int or a float as argument and returns
a tuple
>>> to_kv("eggs", 3)
('eggs', 9)
"""

from typing import Tuple, Union
import math


def to_kv(k: str, v: Union[int, float]) -> Tuple[Union[str, float]]:
    """return a tuple"""
    return (k, float(math.pow(v, 2)))
