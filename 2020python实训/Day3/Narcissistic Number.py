#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/6/29 14:56
@Author  : Blanc
@File    : Narcissistic Number.py
"""
count = 0
for i in range(100, 1000):
    bai = i // 100
    shi = (i - 100 * bai) // 10
    ge = i % 10
    if i == bai * bai * bai + shi * shi * shi + ge * ge * ge:
        count = count + 1
        # print(i)
print('水仙花为', count)
