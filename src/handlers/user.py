#!/usr/bin/env python3
# coding=utf-8

import tornado.web
from ..methods import readdb as mrd


class UserHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        username = self.get_argument("user")
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
        self.render("user.html", users = user_infos)