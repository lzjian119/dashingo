#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Basic run script"""

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.autoreload
from tornado.options import options
import tornado.web

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from settings import settings
from urls import url_patterns


class Application(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)
        engine = create_engine('postgres://%s:%s@%s:5432/%s' %
                       (settings['DB_USER'], settings['DB_PWD'],
                        settings['DB_HOST'], settings['DB_NAME']))
        self.db = scoped_session(
                sessionmaker(bind=engine,
                             autocommit=False, autoflush=True,
                             expire_on_commit=False))
        print "Server running on: " + str(options.port)


def main():
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
