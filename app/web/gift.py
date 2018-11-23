# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 16:46
# @Author  : YH
# @Site    :
# @File    : gift.py
# @Software: PyCharm
from flask import current_app, flash, redirect, url_for

from app.models.base import db
from app.models.gift import Gift
from . import web
from flask_login import login_required, current_user


@web.route('/my/gifts')
@login_required
def my_gifts():
    return '此页面未完成'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():  # 通过自定义的上下文管理器来实现自动提交和回滚
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id  # 通过flask_login来获取uid，事实上flask_login只把uid存储在cookie中,然后通过models/user中的1.1来进行数据读取
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('这本书已经添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')

    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



