# -*- coding: utf-8 -*-

import models.orm as orm
import common.verify as verify
from base import BlankHandler, StatelessHandler, AuthHandler


class EventHandler(AuthHandler):

    def post(self):
        rid = self.get_argument('rid')
        con = self.get_argument('content')
        pos = self.get_argument('position')
        lat = self.get_argument('lat')
        lng = self.get_argument('lng')
        pic = self.get_argument('pic')
        tape = self.get_argument('tape')
        self.write(self.response)
        self.finish()
        e = orm.Event(rid, con, pos, lat, lng, pic, tape)
        self.db.add(e)
        self.db.commit()
        return self.write(self.response)

    def delete(self):
        return self.write(self.response)


class PathHandler(AuthHandler):

    def post(self):
        return self.write(self.response)

