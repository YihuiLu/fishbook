# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 16:45
# @Author  : YH
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask
from app.models.book import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)  # 初始化sqlalchemy
    db.create_all(app=app)  # 生成数据表（映射）
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
