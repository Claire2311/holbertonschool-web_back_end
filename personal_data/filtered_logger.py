#!/usr/bin/env python3
""" return the log message obfuscated"""

from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original_message = super().format(record)
        redacted_message = filter_datum(
            self.fields, self.REDACTION, original_message, self.SEPARATOR
        )
        return redacted_message


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """return the log message obfuscated"""
    log_msges = message.split(separator)
    for index, log_msg in enumerate(log_msges):
        if log_msg.startswith(tuple(fields)):
            log_msges[index] = re.sub("(?<==).*$", redaction, log_msg)
    return separator.join(log_msges)
