#!/usr/bin/env python
# encoding: utf-8
"""
@file: html_downloader.py
@time: 2018-08-14 17:21
@desc: 网页下载器
"""

from urllib import request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        # 打开新的 URL
        response = request.urlopen(url)

        # 判断返回值
        if response.getcode() != 200:
            return None

        # 返回内容
        return response.read()
