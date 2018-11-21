# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 16:46
# @Author  : YH
# @Site    :
# @File    : main.py
# @Software: PyCharm
from . import web


@web.route('/')
def index():
    return '123'


@web.route('/personal')
def personal_center():
    pass
