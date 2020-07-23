#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/16 22:53
@Author  : Blanc
@File    : pokeman.py
"""


class Pokemon(object):
    attribute = "pokemon"

    def __init__(self, name):
        self.name = name


class Water(Pokemon):
    attribute = "水系" + Pokemon.attribute

    def WaterSkill(self):
        print("技能：喷水")


class Fire(Pokemon):
    attribute = "火系" + Pokemon.attribute

    def FireSkill(self):
        print("技能：喷火")


class Grass(Pokemon):
    attribute = "草系" + Pokemon.attribute

    def GrassSkill(self):
        print("技能：飞叶快刀")


a = Water("杰尼龟")
print(a.name, a.attribute)
a.WaterSkill()

b = Fire("小火龙")
print(b.name, b.attribute)
b.FireSkill()

c = Grass("妙蛙种子")
print(c.name, c.attribute)
c.GrassSkill()
