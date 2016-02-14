# -*- coding: utf-8 -*-

import models.orm as orm
import common.verify as verify
from base import BlankHandler, StatelessHandler, AuthHandler

from utils.tool import md5

class RegisterHandler(StatelessHandler):

    def post(self):
        phone = self.get_argument('phone')
        pwd = self.get_argument('pwd')
        captcha = self.get_argument('captcha')
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
        api_key = verify.Auth().add(user.id)
        self.response['data'] = api_key
        self.write(self.response)
        self.finish()
        user_info = orm.UserInfo(uid=user.id)
        user_addr = orm.UserAddr(uid=user.id)
        user_statistic = orm.UserStatistic(uid=user.id)
        self.db.add(user_info)
        self.db.add(user_addr)
        self.db.add(user_statistic)
        self.db.commit()
        return


class InfoHandler(AuthHandler):

    def patch(self, *args, **kwargs):
        nickname = self.get_argument('nickname')
        gender = self.get_argument('gender')
        avatar = self.get_argument('avatar')
        birth = self.get_argument('birth')
        height = self.get_argument('height')
        weight = self.get_argument('weight')
        self.write(self.response)
        self.finish()
        self.db.update(orm.UserInfo)\
            .where(orm.UserInfo.id == self.id)\
            .value(
                nickname=nickname, gender=gender, avatar=avatar,
                birth=birth, height=height, weight=weight
            )


class LoginHandler(StatelessHandler):

    def get(self):
        phone = self.get_argument('phone')
        pwd = self.get_argument('pwd')
        r = self.db.query(orm.User)\
            .filter(orm.User.phone == phone).one_or_none()
        if not r:
            return self.error(301, 'Nonexistent phone')
        if md5(pwd + r.salt) != r.pwd:
            return self.error(302, 'Wrong password')
        api_key = verify.Auth().add(r.id)
        self.response['data'] = api_key
        return self.write(self.response)


class PasswordHandler(StatelessHandler):

    def patch(self, *args, **kwargs):
        phone = self.get_argument('phone')
        password = self.get_argument('pwd')
        if not verify.valid_pwd(password):
            return self.error(302, 'Invalid password')
        captcha = self.get_argument('captcha')
        if not verify.Captcha(phone).check(captcha):
            return self.error(303, 'Wrong captcha')
        r = self.db.query(orm.User)\
            .filter(orm.User.phone == phone).one_or_none()
        if not r:
            return self.error(301, 'Nonexistent phone')
        self.db.update(orm.User)\
            .where(orm.User.phone == phone)\
            .values(pwd=password)
        return self.write(self.response)


class FollowHandler(AuthHandler):

    def get(self):
        r = self.db.query(orm.UserInfo.uid, orm.UserInfo.nickname)\
            .filter(orm.UserFollow.uid == self.id)\
            .join(orm.UserFollow, orm.UserFollow.fid == orm.UserInfo.uid)\
            .all()
        self.response['data'] = r
        return self.write(self.response)

    def post(self):
        fid = self.get_argument('fid')
        f = orm.UserFollow(self.id, fid)
        self.write(self.response)
        self.finish()
        if self.id == fid:
            return
        if self.db.query(orm.UserFollow)\
            .filter(orm.UserFollow.uid == self.id and orm.UserFollow.fid == fid)\
            .count():
            return
        self.db.add(f)
        self.db.commit()
        return

    def delete(self):
        fid = self.get_argument('fid')
        self.write(self.response)
        self.finish()
        self.db.delete().\
            where(orm.UserFollow.uid == self.id and orm.UserFollow.fid == fid)
        return
