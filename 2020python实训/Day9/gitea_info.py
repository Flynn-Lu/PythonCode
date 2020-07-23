#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/11 9:51
@Author  : Blanc
@File    : gitea_info.py
"""
import re


def get_raw_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def write_file(filename, data_list):
    with open(filename, 'a', encoding='utf-8')as file:#追加写入
        for i in data_list:
            file.write(i[0] + ',' + i[1] + ',' + i[2] + '\n')


def process_data(data):
    mode = re.compile(r'<a class="name" href="/([\s\S]*?)/([\s\S]*?)">[\s\S]*?'
                      r'<span class="time-since"[\s\S]*?>([\s\S]*?)</span>')
    return mode.findall(data)


for page in range(3):
    name = 'repos_{}.html'.format(page + 1)
    raw_data = get_raw_data(name)
    processed_data = process_data(raw_data)
    write_file('out.txt', processed_data)