# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 16:46
# @Author  : YH
# @Site    :
# @File    : drift.py
# @Software: PyCharm
from . import web


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
def send_drift(gid):
    pass


@web.route('/pending')
def pending():
    return '敬请期待'


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass
