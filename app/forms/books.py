# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 23:35
# @Author  : YH
# @Site    : 
# @File    : books.py
# @Software: PyCharm

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
