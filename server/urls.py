# -*- coding: utf-8 -*-

from handlers import com, user, route, path

url_patterns = [
    (r"/test", com.TestHandler),
    (r"/captcha", com.CaptchaHandler),
    (r"/register", user.RegisterHandler),
    (r"/login", user.LoginHandler),
    (r"/password", user.PasswordHandler),
    (r"/info", user.InfoHandler),
    (r"/follow", user.FollowHandler),
    (r"/like", com.LikeHandler),
    (r"/comment", route.CommentHandler),
    (r"/event", path.EventHandler),
    (r"/path", path.PathHandler),
    (r"/position", com.PositionHandler),
    (r"/photo", com.PhotoHandler),
]
