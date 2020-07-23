#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/11 8:38
@Author  : Blanc
@File    : post_test.py
"""
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'+
                  ' Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362 '
}
data={
    'username':'aaa',
    'password':'123456'
}

r = requests.post('http://test.boulderh.top/4.php',headers=headers,data=data)
print(type(r.status_code))