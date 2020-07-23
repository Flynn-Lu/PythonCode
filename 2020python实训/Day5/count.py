#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/2 23:09
@Author  : Blanc
@File    : count.py
"""
str = input('请输入字符串：')
key = set(str)
count = dict()
for i in key:
    count[i] = 0
for char in str:
    count[char] = count[char] + 1
for m, n in count.items():
    print(m, '出现次数为', n)
