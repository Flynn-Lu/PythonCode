#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/11 16:36
@Author  : Blanc
@File    : string.py
"""
test_list = ['p', 'y', 't', '\n', 'h', 'o', 'n']

print(str(test_list))  # 不可见字符在列表中会以可见字符展现
r = str(test_list).replace('\n', '')
print(r)
print(''.join(test_list))
