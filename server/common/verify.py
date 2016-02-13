# -*- coding: utf-8 -*-

import redis
import random
import re

from utils.tool import random_str

r = redis.Redis(host='120.55.160.237', port=6379, db=0)


class Captcha:

    def __init__(self, phone):
        self.key = 'captcha:' + phone

    def add(self):
        captcha = random.randint(1000, 9999)
        r.set(self.key, captcha)
        r.expire(self.key, 60)

    def check(self, captcha):
        return captcha == r.get(self.key)


class Auth:

    def __init__(self):
        pass

    def add(self, id):
        api_key = random_str()
        key = 'api_key:' + api_key
        r.set(key, id)
        return api_key

    def check(self, api_key):
        return r.get('api_key:' + api_key)


def valid_phone(phone):
    p = re.compile(r"(1)(3\d|4[5,7]|5[0-3,5-9]|8[023,6-9])\D*(\d{4})\D*(\d{4})$")
    return re.match(p, phone)


def valid_pwd(pwd):
    return len(pwd) == 32
