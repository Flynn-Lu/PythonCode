#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/6/25 17:03
@Author  : Blanc
@File    : Concentric_circle.py
"""
import turtle

t = turtle.Turtle(shape='turtle')
for i in range(5):
    t.penup()
    t.color((0.2 * i, 0.2 * i, 0.2 * i))
    t.goto(0, -40 * (5 - i))
    t.pendown()
    t.begin_fill()
    t.circle(40 * (5 - i))
    t.end_fill()
t.hideturtle()
turtle.mainloop()
