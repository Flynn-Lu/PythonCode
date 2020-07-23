#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/13 15:28
@Author  : Blanc
@File    : bili_user_info.py
"""
import requests
import re
import time
import random
import csv

headers = {
    "user-agent": 'Mozilla/5.0 ' +
                  '(Windows NT 10.0; Win64; x64) ' +
                  'AppleWebKit/537.36 ' +
                  '(KHTML, like Gecko) ' +
                  'Chrome/83.0.4103.116 ' +
                  'Safari/537.36'
}
f = open("bili_user_info.csv", "w", encoding="utf-8")
csv_writer = csv.writer(f)
csv_writer.writerow(["mid", "用户名", "个性签名", "用户等级"])
for i in range(1, 51):
    r = requests.get("https://api.bilibili.com/x/space/acc/info?mid=" + str(i) + "&jsonp=jsonp", headers=headers)
    if r.status_code == 200:
        re_mid = re.compile(r'"mid":([\s\S]*?),')
        re_name = re.compile(r'"name":"([\s\S]*?)",')
        re_sign = re.compile(r'"sign":"([\s\S]*?)",')
        re_level = re.compile(r'"level":([\s\S]*?),')
        mid = re_mid.findall(r.text)
        name = re_name.findall(r.text)
        sign = re_sign.findall(r.text)
        level = re_level.findall(r.text)
        if len(mid) > 0 and len(name) > 0 and len(level) > 0 and len(sign) > 0:
            csv_writer.writerow([mid[0], name[0], sign[0], level[0]])
        time.sleep(2 + random.random())
f.close()
print('已完成')