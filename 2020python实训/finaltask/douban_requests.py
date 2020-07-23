#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/19 17:08
@Author  : Blanc
@File    : douban_requests.py
"""

import requests
import json
import csv
from bs4 import BeautifulSoup
import traceback
import jieba
from wordcloud import WordCloud
from PIL import Image
import numpy as np

class DouBanRequest(object):
    def __init__(self):
        self.headers = {
            'Host': 'movie.douban.com',
            'Connection': 'keep - alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' +
                          'Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40',
            'Referer': 'https://movie.douban.com/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        }

    def get_movie_short_comments(self, movie_id='27668550', page=1, sort='new_score', status='P', percent_type='',
                                 proxies=None):
        """
        movie_id: 电影ID
        page: 页面数，需要处理为开始条数（每页显示20条数据）
        sort: 排序规则，热门：new_score； 最新：time
        status: 状态，看过：P; 想看：F
        percent_type: 选定好评中评差评（状态必须为P）,好评：h; 中评：m; 差评：l
        proxies: 代理
        """
        start = (page - 1) * 20
        url = "https://movie.douban.com/subject/%s/comments?" % str(movie_id)
        headers = self.headers
        params = {
            'start': str(start),
            'limit': '20',
            'sort': sort,
            'status': status,
            'comments_only': '1',
        }
        if percent_type:
            params['percent_type'] = percent_type
        try:
            response = requests.request("GET", url, headers=headers, params=params, timeout=20, proxies=proxies)
            response.close()
        except Exception as e:
            traceback.print_exc()
            return None
        else:
            if response.status_code == 200:
                return response
            else:
                print(response.status_code)
                return None

    def analysis_movie_short_comments(self, resp, type='all'):
        # 初始化解析结果
        analysis_result = []
        try:
            resp_dict = json.loads(resp.text, strict=False)
            html = resp_dict['html'].strip()
            bsObj = BeautifulSoup(html, 'lxml')
            comment_item_list = bsObj.find_all('div', {'class': 'comment-item'})
            for comment_item in comment_item_list:
                # 用户短评信息
                comment_info = comment_item.find('span', {'class': 'comment-info'})
                # 用户昵称
                avatar = comment_info.find('a').text.strip()
                rating = comment_info.find('span', {'class': 'rating'})
                if rating:
                    # 打分描述
                    rating_title = rating['title']
                    # 打分（星值）
                    rating_allstar = rating['class']
                    rating_allstar.remove('rating')
                    rating_allstar = rating_allstar[0].replace('allstar', '')
                else:
                    rating_title = ''
                    rating_allstar = ''
                # 评论时间
                create_time = comment_info.find('span', {'class': 'comment-time'})['title']
                # 评论详情
                short = comment_item.find('span', {'class': 'short'}).text.strip()

                # 判断是否全部解析
                if type == 'all':
                    one_short_list = [avatar, rating_allstar, rating_title, create_time, short]
                else:
                    one_short_list = [short]
                analysis_result.append(one_short_list)
        except Exception as e:
            print('解析失败：')
            traceback.print_exc()
            return None
        else:
            return analysis_result


class CsvFile(object):
    def __init__(self):
        pass

    def save_short_to_csv(self, short_path, data):
        with open(short_path, 'a', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)


class CiYun(object):
    def __init__(self):
        pass

    def ci_yun(self, csv_file, image_file, out_file='ciyun.png'):
        with open(csv_file, encoding='utf-8') as f:
            contents = ''.join(f.readlines())

        # 使用jieba分词，获取词的列表
        contents_cut = jieba.cut(contents, cut_all=True)
        contents_list = " ".join(contents_cut)

        images = Image.open(image_file)
        maskImages = np.array(images)

        # 制作云图
        wc=WordCloud(font_path="msyh.ttc", background_color="white", max_words=1000, max_font_size=100,
                  width=1500, height=1500, mask=maskImages).generate(contents_list)
        wc.to_file(out_file)
