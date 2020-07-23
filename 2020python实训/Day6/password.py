#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/7 8:06
@Author  : Blanc
@File    : password.py
"""
with open("password.txt") as f:
    s = f.read()

res = ""
for character in s:
    if 'a' <= character <= 'z':
        res += chr(97 + (ord(character) + 2 - 97) % 26);
    else:
        res += character

print(res)