# -*- coding: utf-8 -*-

import models.orm as orm
import common.verify as verify
from base import BlankHandler, StatelessHandler, AuthHandler


class RouteHandler(AuthHandler):

    def get(self):
        # todo: 验证是否有权限查看
        rid = self.get_argument('rid')
        if rid:
            self.db.query(orm.Route)\
                .filter(orm.Route.uid == rid)\
                .all()
        else:
            self.db.query(orm.Route)\
                .filter(orm.Route.uid == self.id)\
                .all()

    def post(self):
        self.write(self.response)
        self.finish()


class CommentHandler(StatelessHandler):

    def get(self):
        return self.write(self.response)

    def delete(self):
        return self.write(self.response)

    def post(self):
        phone = self.get_query_argument('phone')
        pwd = self.get_query_argument('pwd')
        captcha = self.get_query_argument('captcha')
        if not verify.valid_phone(phone):
            return self.error(301, 'Invalid phone')
        if self.db.query(orm.User).\
                filter(orm.User.phone == phone).first():
            return self.error(302, 'Registered phone')
        if not verify.valid_pwd(pwd):
            return self.error(303, 'Invalid password')
        if not verify.Captcha(phone).check(captcha):
            return self.error(304, 'Wrong captcha')
        user = orm.User(phone, pwd)
        self.db.add(user)
        self.db.commit()
        return self.write(self.response)
