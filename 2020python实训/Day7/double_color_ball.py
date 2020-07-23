#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/9 13:15
@Author  : Blanc
@File    : double_color_ball.py
"""
# 程序运行之后，从1‐64中挑选5个数作为彩票的抽奖结果
import random

a = list()

for i in range(0, 5):
    b = random.randint(1, 64)
    a.append(b)
print('双色球号开奖：', a)