#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/6/29 11:15
@Author  : Blanc
@File    : draw.py
"""
import turtle
t = turtle.Turtle(shape='turtle')
num1 = input("画圆形(1)还是等边三角形(2)：")
if num1 == '1':
    num2 = input("请输入圆的半径：")
    num2 = int(num2)
    num4 = input("是否需要填充圆(y/n)：")
    if num4 == 'y':
        t.color('red', 'blue')
        t.begin_fill()
        t.circle(num2)
        t.end_fill()
        turtle.mainloop()
    if num4 == 'n':
        t.circle(num2)
        t.end_fill()
        turtle.mainloop()
if num1 == '2':
    num3 = input("请输入等边三角形的边长：")
    num3 = int(num3)
    num5 = input("是否需要填充三角形(y/n)：")
    if num5 == 'y':
        t.color('red', 'blue')
        t.begin_fill()
        t.forward(num3)
        t.left(120)
        t.forward(num3)
        t.left(120)
        t.forward(num3)
        t.left(120)
        t.end_fill()
        turtle.mainloop()
    if num5 == 'n':
        t.forward(num3)
        t.left(120)
        t.forward(num3)
        t.left(120)
        t.forward(num3)
        t.left(120)
        t.end_fill()
        turtle.mainloop()
