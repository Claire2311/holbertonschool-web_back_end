#!/usr/bin/env python3
""" return the log message obfuscated"""

from typing import List
import re


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """return the log message obfuscated"""
    log_msges = message.split(separator)
    for index, log_msg in enumerate(log_msges):
        if log_msg.startswith(tuple(fields)):
            log_msges[index] = re.sub("(?<==).*$", redaction, log_msg)
    return separator.join(log_msges)
