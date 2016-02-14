# -*- coding: utf-8 -*-

import models.orm as orm
import common.verify as verify
from base import BlankHandler, StatelessHandler, AuthHandler
import json
from utils.tool import AlchemyEncoder

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


class CommentHandler(AuthHandler):

    def get(self):
        rid = self.get_argument('rid')
        r = self.db.query(orm.RouteComment.uid, orm.RouteComment.aid,
                          orm.RouteComment.content,
                          orm.UserInfo.nickname, orm.UserInfo.avatar)\
            .filter(orm.UserInfo.uid == orm.RouteComment.uid)\
            .filter(orm.RouteComment.rid == rid).all()
        self.response['data'] = [dict(zip(u.keys(), u)) for u in r]
        return self.write(self.response)

    def delete(self):
        rid = self.get_argument('rid')
        aid = self.get_argument('aid')
        content = self.get_argument('content')
        self.write(self.response)
        self.finish()
        user = orm.RouteComment(self.id, rid, content, aid)
        self.db.add(user)
        self.db.commit()

    def post(self):
        rid = self.get_argument('rid')
        aid = self.get_argument('aid')
        content = self.get_argument('content')
        self.write(self.response)
        self.finish()
        user = orm.RouteComment(self.id, rid, content, aid)
        self.db.add(user)
        self.db.commit()
