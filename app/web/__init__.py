# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 16:46
# @Author  : YH
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint

web = Blueprint('web', __name__)

from . import book, auth, drift, gift, main, wish
