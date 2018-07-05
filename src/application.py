#!/usr/bin/env python3
# coding=utf-8

from src.url import url

import tornado.web
import os

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "statics")
)

application = tornado.web.Application(
    handlers = url,
    **settings
)