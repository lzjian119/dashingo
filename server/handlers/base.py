# -*- coding: utf-8 -*-

import tornado.web
import common.verify as verify

import time

API_VERSION = 1

class BlankHandler(tornado.web.RequestHandler):

    response = {}
    start = 0

    def prepare(self):
        self.response = {
            'code': 100,
            'msg': 'OK',
            'data': None
        }
        self.start = time.time()

    def error(self, code, msg):
        self.response['code'] = code
        self.response['msg'] = msg
        self.write(self.response)

    def on_finish(self):
        print str(self.__class__) + \
              self.request.uri + " - " + \
              str(time.time() - self.start)

class StatelessHandler(tornado.web.RequestHandler):

    response = {}
    start = 0

    @property
    def db(self):
        return self.application.db

    def prepare(self):
        self.response = {
            'code': 100,
            'msg': 'OK',
            'data': None
        }
        self.start = time.time()

    def error(self, code, msg):
        self.response['code'] = code
        self.response['msg'] = msg
        self.write(self.response)

    def on_finish(self):
        print str(self.__class__) + \
              self.request.uri + " - " + \
              str(time.time() - self.start)


class AuthHandler(tornado.web.RequestHandler):

    response = {}
    id = -1
    start = 0

    @property
    def db(self):
        return self.application.db

    def prepare(self):
        self.response = {
            'code': 100,
            'msg': 'OK',
            'data': None
        }
        self.start = time.time()
        api_key = self.request.headers['api_key']
        version = self.request.headers['version']
        if not version:
            return self.error(201, 'Lack headers: version')
        if int(version) != API_VERSION:
            return self.error(204, 'Wrong version')
        if not api_key:
            return self.error(201, 'Lack headers: api_key')
        self.id = verify.Auth().check(api_key)
        if not self.id:
            return self.error(203, 'Invalid APIkey')

    def error(self, code, msg):
        self.response['code'] = code
        self.response['msg'] = msg
        self.write(self.response)
        if not self._finished:
            self.finish()

    def on_finish(self):
        print str(self.__class__) + \
              self.request.uri + " - " + \
              str(time.time() - self.start)
