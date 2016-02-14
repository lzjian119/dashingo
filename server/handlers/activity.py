# -*- coding: utf-8 -*-

import models.orm as orm
import common.verify as verify
from base import BlankHandler, StatelessHandler, AuthHandler


class TimelineHandler(AuthHandler):

    def get(self):
        page = self.get_argument('page', 0)
        r = self.db.query(orm.UserTimeline)\
            .filter(orm.UserTimeline.uid == self.id)\
            .limit(10).offset(10 * page)
        self.response['data'] = r
        return self.write(self.response)


class NotificationHandler(AuthHandler):

    def get(self):
        r = self.db.query(orm.UserNotification)\
            .filter(orm.UserNotification.uid == self.id and orm.UserNotification.state == 'N')\
            .all()
        self.response['data'] = r
        return self.write(self.response)
