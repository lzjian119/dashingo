# -*- coding: utf-8 -*-

import tornado.web
import models.orm as orm
import common.verify as verify
from base import BlankHandler, StatelessHandler, AuthHandler
from geoalchemy2 import Geography, functions, WKTElement, func

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
        pos = WKTElement('POINT({0} {1})'.format(lng, lat), srid=4326)
        self.write(self.response)
        self.finish()
        r = self.db.query(orm.UserAddr)\
                .filter(orm.UserAddr.uid == self.id)\
                .first()
        r.pos = pos
        r.lat = lat
        r.lng = lng
        r.update_time = now_datetime()
        self.db.commit()
        return

    def get(self):
        lat = self.get_argument('lat')
        lng = self.get_argument('lng')
        pos = WKTElement('POINT({0} {1})'.format(lng, lat), srid=4326)
        # todo: 添加对位置更新时间的筛选
        r = self.db.query(orm.UserAddr.uid, func.ST_Distance(orm.UserAddr.pos, pos), orm.UserAddr.lat,
                          orm.UserAddr.lng, orm.UserInfo.avatar, orm.UserInfo.nickname)\
            .filter(func.ST_DWithin(orm.UserAddr.pos, pos, 5000))\
            .filter(orm.UserAddr.uid == orm.UserInfo.uid)\
            .all()
        self.response['data'] = [dict(zip(u.keys(), u)) for u in r]
        return self.write(self.response)


class LikeHandler(AuthHandler):

    def get(self):
        lid = self.get_argument('lid')
        t = self.get_argument('type')
        r = self.db.query(orm.UserInfo.uid, orm.UserInfo.nickname, orm.UserInfo.avatar)\
            .filter(orm.UserLike.lid == lid and orm.UserLike.type == t)\
            .filter(orm.UserInfo.uid == orm.UserLike.uid)\
            .all()
        self.response['data'] = [dict(zip(u.keys(), u)) for u in r]
        return self.write(self.response)

    def delete(self):
        lid = self.get_argument('lid')
        t = self.get_argument('type')
        self.db.delete(orm.UserLike)\
            .where(orm.UserLike.uid == self.id and orm.UserLike.lid == lid and orm.UserLike.type == t)
        return self.write(self.response)

    def post(self):
        lid = self.get_argument('lid')
        t = self.get_argument('type')
        self.write(self.response)
        self.finish()
        if self.db.query(orm.UserLike)\
                .filter(orm.UserLike.uid == self.id and orm.UserLike.lid == lid and orm.UserLike.type == t)\
                .first():
            return
        like = orm.UserLike(self.id, lid, t)
        self.db.add(like)
        self.db.commit()
