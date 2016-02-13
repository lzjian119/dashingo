# -*- coding: utf-8 -*-

import redis

r = redis.Redis(host='120.55.160.237', port=6379, db=3)

def record():
    r.sadd('path:123','user:Guo')