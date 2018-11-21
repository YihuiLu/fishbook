# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 16:45
# @Author  : YH
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask
from flask_login import LoginManager
from app.models.base import db

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    db.init_app(app)  # 初始化sqlalchemy
    db.create_all(app=app)  # 生成数据表（映射）
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
