# -*- coding: utf-8 -*-

import requests

def send_sms(phone, content):
    params = {
        'account': 'jiekou-clcs-03',
        'pswd': 'Admin888',
        'msg': content,
        'mobile': phone
    }
    r = requests.post('http://222.73.117.158/msg/HttpBatchSendSM', params)
    print r.text
    return