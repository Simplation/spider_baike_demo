#!/usr/bin/env python
# encoding: utf-8
"""
@file: url_manager.py
@time: 2018-08-14 17:22
@desc: url 管理器
"""


class UrlManager(object):

    def __init__(self):
        self.new_url = set()
        self.old_url = set()

    # 添加 url
    def add_new_url(self, url):
        if url is None:
            return

        if url not in self.new_url or url not in self.old_url:
            self.new_url.add(url)

    # 添加新的 url
    def add_new_urls(self, urls):
        if urls is None:
            return

        for url in urls:
            self.new_url.add(url)

    # 判断是否存在新的 url
    def has_new_url(self):
        return len(self.new_url) != 0

    # 获取新的 url
    def get_new_url(self):
        new_url = self.new_url.pop()
        self.old_url.add(new_url)
        return new_url
