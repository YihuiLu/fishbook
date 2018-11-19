# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 16:46
# @Author  : YH
# @Site    : 
# @File    : book.py
# @Software: PyCharm
from flask import jsonify, request
from app.forms.books import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web


@web.route('/book/search')
def search():
    """
    :return:
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)

        return jsonify(result)
    else:
        return jsonify({"msg": form.errors})
