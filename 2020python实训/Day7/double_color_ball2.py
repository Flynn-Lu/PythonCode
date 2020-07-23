#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/10 15:42
@Author  : Blanc
@File    : double_color_ball2.py
"""
import random
import time
'''
name = time.strftime('%Y-%m-%d', time.localtime())
print(name)
f = open(file=name + '.txt', mode='w', encoding='utf-8-sig')
a = list()

for i in range(0, 5):
    b = random.randint(1, 64)
    a.append(b)
a = str(a)
f.write('双色球号开奖：' + a)
f.close()'''
list1 = random.sample(range(1, 65), 5)
list1 = str(list1)
name = time.strftime('%Y-%m-%d', time.localtime())
f = open(file=name + '.txt', mode='w', encoding='utf-8-sig')
f.write('双色球号开奖：' + list1)
f.close()