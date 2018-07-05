#!/usr/bin/env python3
# coding=utf-8

import pymysql

conn = pymysql.connect(host="localhost", user="root", passwd="zt123", db="zhituweb", port=3306, charset="utf8")
cur = conn.cursor()