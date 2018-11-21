# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 14:31
# @Author  : YH
# @Site    : 
# @File    : base.py
# @Software: PyCharm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger, Integer

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)
    create_time = Column('create_time', Integer)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
