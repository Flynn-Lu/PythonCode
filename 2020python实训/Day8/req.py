#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/10 23:13
@Author  : Blanc
@File    : req.py
"""
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '+
                  'Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362 '
}

r = requests.get('http://test.boulderh.top/2.php',headers=headers)
print(r.text)