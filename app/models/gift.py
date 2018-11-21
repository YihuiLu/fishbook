# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 14:31
# @Author  : YH
# @Site    : 
# @File    : gift.py
# @Software: PyCharm


from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class Gift(Base):
    user = relationship('User')  # 引入User模型类
    uid = Column(Integer, ForeignKey('user.id'))  # 引入上面一行的user
    isbn = Column(String(15), nullable=False)
    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)

