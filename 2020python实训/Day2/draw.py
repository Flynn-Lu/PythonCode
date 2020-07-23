#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/6/28 16:29
@Author  : Blanc
@File    : draw.py
"""
num1 = input("请输入等边三角形边长：")
num1 = int(num1)
num2 = input("请输入以原点为圆心的圆的半径：")
num2 = int(num2)

import turtle

# 创建一个画笔对象，形状为海龟
t = turtle.Turtle(shape='turtle')
t.penup()
t.goto(-500, 0)
t.pendown()
t.forward(num1)
t.left(120)
t.forward(num1)
t.left(120)
t.forward(num1)
t.left(120)
t.penup()
t.goto(0, -num2)
t.pendown()
t.circle(num2)

# 持续刷新窗口，保证画图结束不会自动关闭
turtle.mainloop()
# ==turtled.own
