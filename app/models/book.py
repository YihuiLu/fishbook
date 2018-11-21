# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 13:16
# @Author  : YH
# @Site    : 
# @File    : book.py
# @Software: PyCharm

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class Book(Base):

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)  # unique：不重复字段
    summry = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass
