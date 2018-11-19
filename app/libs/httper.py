# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 15:42
# @Author  : YH
# @Site    : 
# @File    : httper.py
# @Software: PyCharm

import requests


class HTTP(object):
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
