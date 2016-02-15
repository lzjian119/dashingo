# -*- coding: utf-8 -*-

import os.path
from tornado.options import define

define("port", default=8001, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")

settings = {}

settings["debug"] = True
settings["cookie_secret"] = "askdfjpo83q47r9haskldfjh8"
settings["login_url"] = "/login"
settings["static_path"] = os.path.join(os.path.dirname(__file__), "static")
settings["template_path"] = os.path.join(os.path.dirname(__file__), "templates")
settings["xsrf_cookies"] = False

settings["DB_USER"] = "postgres"
settings["DB_HOST"] = "120.55.160.237"
settings['DB_PWD'] = "postgres"
settings['DB_NAME'] = "dashingo"

DB_HOST = '120.55.160.237'
DB_USER = 'postgres'
DB_PWD = 'postgres'
DB_NAME = 'dashingo'