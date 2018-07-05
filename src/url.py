#!/usr/bin/python3
# coding=utf-8
"""
the url structure of website
"""
from src.handlers.index import IndexHandler

url = [
    (r'/', IndexHandler),
]