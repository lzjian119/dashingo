# -*- coding: utf-8 -*-

import models.orm as orm
import common.verify as verify
from base import BlankHandler, StatelessHandler, AuthHandler


class ReportHandler(AuthHandler):

    def post(self):
        rid = self.get_argument('rid')
        t = self.get_argument('type')
        self.write(self.response)
        self.finish()
        e = orm.AdminReport(self.id, rid, t)
        self.db.add(e)
        self.db.commit()
        return self.write(self.response)


class FeedbackHandler(AuthHandler):

    def post(self):
        rid = self.get_argument('rid')
        t = self.get_argument('type')
        self.write(self.response)
        self.finish()
        e = orm.AdminReport(self.id, rid, t)
        self.db.add(e)
        self.db.commit()
        return self.write(self.response)
