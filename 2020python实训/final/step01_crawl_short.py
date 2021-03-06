# coding=utf-8

import time
from douban_requests import DouBanRequest
from douban_requests import CsvFile

# 输入豆瓣电影ID，开始页数，结束页数
movie_id = '27668250'
start_page = 1
end_page = 11
# 存入文件路径名称
short_path = '%s_movie_short.csv' % movie_id


# 好评中评差评列表
percent_type_list = ['h', 'm', 'l']

# 每个选项只能采集11页，遍历每个评价类型
for percent_type in percent_type_list:
    # 遍历页数
    for page in range(start_page, end_page + 1):
        # 采集HTML
        resp = DouBanRequest().get_movie_short_comments(movie_id='27668250', page=page, sort='new_score', status='P',
                                                        percent_type=percent_type, proxies=None)
        if resp:
            # 解析HTML
            analysis_result = DouBanRequest().analysis_movie_short_comments(resp, type='all')
            if analysis_result:
                # 追加写入csv
                CsvFile().save_short_to_csv(short_path, analysis_result)
                print('%s : 第%d页写入文件成功' % (percent_type, page))
                # 设置强制等待，防止网站封IP
                time.sleep(10)
            else:
                print('%s : 第%d页解析失败' % (percent_type, page))
        else:
            print('%s : 第%d页采集失败' % (percent_type, page))
