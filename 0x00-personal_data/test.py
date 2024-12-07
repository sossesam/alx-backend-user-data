#!/usr/bin/env python3
"""
Module for handling Personal Data
"""
import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns a log message obfuscated """
    for f in fields:
        message = re.sub(f"{f}=.*?{separator}", f"{f}={redaction}{separator}", message)
    return message

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    logging.warning(filter_datum(fields, 'xxx', message, ';'))