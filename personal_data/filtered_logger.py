#!/usr/bin/env python3
"""return the log message obfuscated"""

from typing import List
import re
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """get a logger message"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(streamHandler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """connection to the database"""
    username = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password_db = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host_db = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    database_name = os.environ.get("PERSONAL_DATA_DB_NAME")
    cnx = mysql.connector.connect(
        user=username,
        password=password_db,
        host=host_db,
        database=database_name
    )
    return cnx


def main():
    """main function"""
    cnx = get_db()
    cursor = cnx.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    format(cursor)
    cursor.close()
    cnx.close()
