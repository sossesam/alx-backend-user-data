#!/usr/bin/env python3

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    return re.sub(r'(' + '|'.join(map(re.escape, fields)) + r')=[^;]*', lambda m: m.group(0).split('=')[0] + '=' + redaction, message)
   