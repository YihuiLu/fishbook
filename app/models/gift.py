# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 14:31
# @Author  : YH
# @Site    : 
# @File    : gift.py
# @Software: PyCharm
from flask import current_app
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.spider.yushu_book import YuShuBook


class Gift(Base):
    user = relationship('User')  # 引入User模型类
    uid = Column(Integer, ForeignKey('user.id'))  # 引入上面一行的user
    isbn = Column(String(15), nullable=False)
    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    # 对象代表一个礼物，具体
    # 类代表礼物这个事物，它是抽象，不是具体的“一个”
    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            Gift.create_time).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift
