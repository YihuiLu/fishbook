# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 16:49
# @Author  : YH
# @Site    :
# @File    : wish.py
# @Software: PyCharm
from . import web


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    pass


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
