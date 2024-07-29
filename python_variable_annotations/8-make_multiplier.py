#!/usr/bin/env python3
"""
function that take a number as argument and return a function that multiplies
a float by the argument
>>> make_multiplier(2.22)
4.928400000000001
"""

from typing import Callable
import math


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """eturn a function that multiplies a float by the argument"""
    def inner_function():
        return math.pow(multiplier, 2)
    return inner_function
