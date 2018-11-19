# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 16:12
# @Author  : YH
# @Site    : 
# @File    : yushu_book.py
# @Software: PyCharm

from app.libs.httper import HTTP
from flask import current_app

class YuShuBook(object):

    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        per_page = current_app.config['PER_PAGE']
        url = cls.keyword_url.format(keyword, per_page, cls.calculate_start(page))
        result = HTTP.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
