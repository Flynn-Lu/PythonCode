#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/6 8:58
@Author  : Blanc
@File    : tower.py
"""
num = int(input('请输入塔的层数：'))
if num > 10:
    num = int(input('请重新输入：'))
for i in range(1, num + 1):
    print(' ' * (num - i) + '=' * (2 * i - 1))