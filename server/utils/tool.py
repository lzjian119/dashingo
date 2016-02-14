# -*- coding: utf-8 -*-

import random
import string

def random_str(len=8):
    salt = ''.join(random.sample(string.ascii_letters + string.digits, len))
    return salt

def md5(s):
    import hashlib
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()

def now_float():
    import time
    return time.time()

def now_int():
    import time
    return int(time.time())

def now_datetime():
    import datetime
    return str(datetime.datetime.now())

import json
from datetime import datetime
class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        # elif isinstance(obj, date):
        #     return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)