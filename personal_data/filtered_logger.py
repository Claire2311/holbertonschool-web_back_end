#!/usr/bin/env python3
""" return the log message obfuscated
"""


from typing import List
import re


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
):
    """return the log message obfuscated"""
    loggin_messages = message.split(separator)
    for i in range(len(loggin_messages)):
        if loggin_messages[i].startswith(tuple(fields)):
            loggin_messages[i] = re.sub(
                "(?<==).*$", redaction, loggin_messages[i]
                )
    return separator.join(loggin_messages)
