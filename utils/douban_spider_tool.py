#!/usr/bin/python
# encoding:utf-8
"""
@author: lance
@version: 1.0.0
@license: Apache Licence
@file: douban_spider_tool.py
@time: 2021/4/1 22:05
"""
import random
import time
import requests
from lxml import etree
import xlwt
import xlrd
from xlutils.copy import copy
from tqdm import tqdm


def do_request(url):
    cookies = 'bid=2YpxwjK9lvQ; douban-fav-remind=1; ll="118209"; ct=y; push_noty_num=0; push_doumail_num=0; ' \
              'dbcl2="214312932:yf9FiNmbSiA"; ck=FXHd; ap_v=0,' \
              '6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1617507780%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch' \
              '%3Fq%3D%25E5%2590%25B8%25E8%25A1%2580%25E9%25AC%25BC%22%5D; _pk_ses.100001.4cf6=*; ' \
              '_pk_id.100001.4cf6=ce0f0e7bdf63c5fa.1614864188.8.1617509246.1617453975. '

    cookies_dict = {}

    for i in cookies.split(";"):
        cookies_dict[i.split('=')[0]] = i.split('=')[1]
    # print(cookies_dict)
    headers_list = [{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                   'Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68'},
                    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                   'Chrome/85.0.4183.83 Safari/537.36'},
                    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'},
                    {'User-Agent': 'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'},
                    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
                    {'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},
                    {'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},
                    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'},
                    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'},
                    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'},
                    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)'},
                    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr '
                                   '1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'},
                    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'},
                    ]
    # 0 14
    t = random.randint(0, 12)
    response = requests.get(url, headers=headers_list[t], cookies=cookies_dict)
    html_txt = response.text
    if response.status_code != 200:
        print(headers_list[t])
    # print(html_txt)
    html_etree = etree.HTML(html_txt)
    comments = html_etree.xpath("//span[@class='short']/text()")
    stars = html_etree.xpath("//span[@class='comment-info']/span[2]/@class")
    # print(zip(comments, stars))
    for i in range(len(stars)):
        stars[i] = stars[i].split()[0][7:9]
    for i in range(len(comments)):
        comments[i] = comments[i].strip()
    # for i in zip(comments, stars):
    #     print(i)
    #     print("*" * 50)
    if len(comments) == 0:
        print(headers_list[t])
    return zip(comments, stars)


def auto_request(n, program):
    comments = []
    stars = []
    for i in range(n):
        time.sleep(2)
        num = i * 20
        url = 'https://movie.douban.com/subject/' + program + '/comments'
        url = url + '?' + 'start=' + str(num) + '&limit=20&status=P&sort=new_score'
        try:
            res0, res1 = zip(*do_request(url))
            comments += res0
            stars += res1
        except:
            print('pass' + str(i))
    res = zip(comments, stars)
    # for i in res:
    #     print(i)
    return res


def get_comments():
    # 500 10
    #           哥斯拉大战金刚 奇葩说 这个杀手不太冷 肖申克的救赎 逐梦演艺圈 让子弹飞 信条-Tenet
    #           八佰 进击的巨人-最终季 后翼弃兵  吐槽大会-第五季
    #           名侦探柯南-红之校外旅行 权力的游戏1 2 3 7 8
    #           进击的巨人2013 2017 2018 Final Season
    # programs = ['26613692', '35070344', '1295644', '1292052', '26322774', '3742360', '30444960',
    #             '26754233', '33440021', '32579283', '35236741', ]
    programs = ['35207723', '3016187', '6558062', '10590706', '26235354', '26584183',
                '23748525', '26268494', '27072327', '33440021']
    comments = []
    stars = []
    for i in tqdm(programs, desc="爬取中..."):
        res0, res1 = zip(*auto_request(25, i))
        comments += res0
        stars += res1
    return zip(comments, stars)


def save_excel():
    res0, res1 = zip(*get_comments())
    # for i in res0, res1:
    #     print(i)
    work = xlrd.open_workbook('2.xls')
    workbook_1 = copy(work)
    worksheet_1 = workbook_1.get_sheet(0)
    for i in range(len(res0)):
        worksheet_1.write(i + 1, 1, res0[i])
        worksheet_1.write(i + 1, 2, res1[i])
    workbook_1.save('2.xls')


if __name__ == '__main__':
    save_excel()
    # do_request('https://movie.douban.com/subject/35070344/comments?start=40&limit=20&status=P&sort=new_score')
