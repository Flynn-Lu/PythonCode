#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/7 8:05
@Author  : Blanc
@File    : count.py
"""
f = open(file='TheOldManAndtheSea.txt', mode='r', encoding='utf-8-sig')
data = f.read()
for i in data:
    if i.isalpha() == False and i != ' ':#判空或符号
        data = data.replace(i, ' ')
data = data.lower()
count = 0
s = data.split()
d = {}
for k in s:
    if k not in d:
        d[k] = 1
    else:
        d[k] += 1
res = max(d, key=lambda x: d[x])    #lambda为匿名函数
print(s)
print(d)
print('{0}出现的次数最多，为{1}次'.format(res, d[res]))
f = open('out.txt', 'w', encoding='UTF-8')
f.write('{0}出现的次数最多，为{1}次'.format(res, d[res]))
f.close()