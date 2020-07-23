#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/19 17:09
@Author  : Blanc
@File    : step02_ciyun.py
"""


from douban_requests import CsvFile, CiYun

csv_file = '27668250_movie_short.csv'
image_file = 'background.jpg'

CiYun().ci_yun(csv_file, image_file, out_file='ciyun.png')
