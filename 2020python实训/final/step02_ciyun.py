# coding=utf-8
'''依据采集的电影短评结果做词云图'''

from douban_requests import CsvFile, CiYun

csv_file = '27668250_movie_short.csv'
image_file = 'background.jpg'

CiYun().ci_yun(csv_file, image_file, out_file='ciyun.png')
