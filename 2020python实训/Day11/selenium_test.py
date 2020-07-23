#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/13 15:53
@Author  : Blanc
@File    : selenium_test.py
"""
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://space.bilibili.com/1')
name=browser.find_element_by_id('h-name')
print(name.text)
browser.close()