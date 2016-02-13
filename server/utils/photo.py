# -*- coding: utf-8 -*-

import qiniu


def get_qiniu_auth():
    q = qiniu.Auth('2xcEyqx3UhVMnajCRQSNVL31hOzcvNxdcZupHAKd', 'gGDCDDXMPveGzyWDht_lwYRKD2aJKl3caksMG-pl')
    auth = q.upload_token('dashingo')
    return auth