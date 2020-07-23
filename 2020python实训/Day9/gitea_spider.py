#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/11 8:48
@Author  : Blanc
@File    : gitea_spider.py
"""
import requests
import time
import random


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' +
                      'Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
    }

    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.text
    else:
        return ''


def write_to_file(filename, data):
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(data)


def main():
    for page in range(1, 3 + 1):
        url = 'http://gitea.boulderh.top/explore/repos?page={}&sort=recentupdate&q=&topic=false'.format(page)
        print(url)
        data = get_html(url)
        filename = 'repos_{}.html'.format(page)
        write_to_file(filename, data)
        print('第{}页数据获取完毕'.format(page))
        time.sleep(random.randint(1, 4))
    print('程序完成')


# 双指针取字符串<a>
main()
