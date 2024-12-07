#!/usr/bin/env python3

import re

def filter_datum(fields: str, redaction: str, message: str, separator: str) -> str:
    return re.sub(r'(' + '|'.join(map(re.escape, fields)) + r')=[^;]*', lambda m: m.group(0).split('=')[0] + '=' + redaction, message)
   


field = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(field, 'xxx', message, ';'))