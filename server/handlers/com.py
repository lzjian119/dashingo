# -*- coding: utf-8 -*-

import tornado.web
import models.orm as orm
import common.verify as verify
from base import BlankHandler, StatelessHandler, AuthHandler

from utils.tool import now_datetime
import utils.photo


class TestHandler(BlankHandler):

    def get(self):
        return self.write(self.response)

    def post(self):
        return self.write(self.response)

    def patch(self, *args, **kwargs):
        return self.write(self.response)

    def delete(self, *args, **kwargs):
        return self.write(self.response)

    def put(self, *args, **kwargs):
        return self.write(self.response)


class CaptchaHandler(BlankHandler):

    def post(self):
        phone = self.get_query_argument('phone')
        if not verify.valid_phone(phone):
            return self.error(301, 'Invalid phone')
        verify.Captcha(phone).add()
        return self.write(self.response)


class PhotoHandler(BlankHandler):

    def get(self):
        self.response['data'] = utils.photo.get_qiniu_auth()
        return self.write(self.response)


class PositionHandler(AuthHandler):

    def patch(self):
        lat = self.get_argument('lat')
        lng = self.get_argument('lng')
        self.write(self.response)
        self.finish()
        self.db.update(orm.UserAddr)\
            .where(orm.UserAddr.uid == self.id)\
            .values(lat=lat, lng=lng, update_time=now_datetime())
        return

    def get(self):
        lat = self.get_argument('lat')
        lng = self.get_argument('lng')
        return self.write(self.response)


class LikeHandler(AuthHandler):

    def get(self):
        id = self.id
        star = orm.RouteLike()
        self.db.insert()
        return self.write(self.response)

    def delete(self):
        return self.write(self.response)

    def post(self):
        return self.write(self.response)
