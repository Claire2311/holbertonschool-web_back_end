#!/usr/bin/env python3
"""
function that return the first element of a list
"""


from typing import Sequence, Any, Optional


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """function that return the first element of a list"""
    if lst:
        return lst[0]
    else:
        return None
