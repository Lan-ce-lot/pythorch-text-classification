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

"""
Cookie: bid=2YpxwjK9lvQ; douban-fav-remind=1; ll="118209"; ct=y; push_noty_num=0; push_doumail_num=0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1617723515%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.8cb4=*; ap_v=0,6.0; dbcl2="214312932:MYXGJCiIg0Y"; ck=0Amj; _pk_id.100001.8cb4=a68abd16218042d2.1603972914.12.1617723615.1617684722.
"""


def do_request(url):
    cookies = 'bid=2YpxwjK9lvQ; douban-fav-remind=1; ll="118209"; ct=y; push_noty_num=0; push_doumail_num=0; ' \
              '_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1617867376%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D' \
              '%25E5%2590%25B8%25E8%25A1%2580%25E9%25AC%25BC%22%5D; _pk_ses.100001.4cf6=*; ' \
              'dbcl2="214312932:4TztqT8LolA"; ck=xpj9; ' \
              '_pk_id.100001.4cf6=ce0f0e7bdf63c5fa.1614864188.17.1617867662.1617855456. '

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
                    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
                     },
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
    # t = random.randint(0, 12)
    t = 0
    response = requests.get(url, headers=headers_list[t], cookies=cookies_dict)
    html_txt = response.text
    if response.status_code != 200:
        print(response.content)
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
    # print('https://movie.douban.com/subject/' + program)
    sta = 0
    for i in tqdm(range(n), desc="页面爬取中..."):
        # for i in range(n):
        time.sleep(random.randint(10, 30))
        num = i * 20
        url = 'https://movie.douban.com/subject/' + program + '/comments'
        url = url + '?' + 'start=' + str(num) + '&limit=20&status=P&sort=new_score'
        print(url)
        if sta >= 6:
            break
        try:
            res0, res1 = zip(*do_request(url))
            comments += res0
            stars += res1
        except Exception as e:
            print(repr(e))
            sta += 1
            print('pass' + str(i))

    res = zip(comments, stars)

    return res


def save_excel(url, par):
    res0, res1 = zip(*par)

    work = xlrd.open_workbook(url)
    old_sheet = work.sheets()[0]
    con = old_sheet.nrows
    workbook_1 = copy(work)
    worksheet_1 = workbook_1.get_sheet(0)
    print(con)
    for i in range(len(res0)):
        worksheet_1.write(i + con, 1, res0[i])
        worksheet_1.write(i + con, 2, res1[i])
    workbook_1.save(url)
    print('保存{}条'.format(len(res0)))


def new_catch():
    programs = [
        '26613692', '35070344', '1295644', '1292052', '26322774', '3742360', '30444960',
        '26754233', '33440021', '32579283', '35236741',
        '35207723',
        '3016187',
        '6558062',
        '10590706',
        '26235354',
        '26584183',
        '23748525',
        '26268494',
        '27072327',
        '33440021',
        '30128916', '25862300', '26342391', '33591810',
        '34461705', '26754233', '30353869', '35069520',
        '30482481', '30346025', '26613692', '35076714',
        '35231379', '34925598', '35027719', '34779692',
        '26958479', '26935283', '35242942', '30458949',
        '30456637', '26759820', '34902639', '34804147',
        '27662747', '34960094', '34805873', '30454679',
        '2609258', '35096844', '24733428', '35068230',
        '27594653', '27073752', '30323120', '34962956',
        '30444960', '24298954', '30257787', '34869387',
        '30465068', '34845781', '34850598', '3439312',
        '30171424', '34982759', '34983332', '30310219',
        '35310153', '30464264', '30128916', '25862300',
        '26342391', '33591810', '34461705', '26754233',
        '30353869', '35069520', '30482481', '30346025',
        '26613692', '35076714', '35231379', '34925598',
        '35027719', '34779692', '26958479', '26935283',
        '35242942', '30458949', '35216228', '35243063',
        '27044385', '26302614', '35410279', '35202738',
        '35382366', '30238409', '35064992', '27068534',
        '26926445', '27605542', '35399987', '35296013',
        '34893332', '30483667', '34923491', '30228394',
        '35027568', '35280738', '30367642', '35306371',
        '34895145', '33390298', '35073642', '35196776',
        '34937895', '35268503', '35205803', '35326260',
        '35366253', '33440021', '35356724', '35231889',
        '34979479', '35170378', '30313878', '27148168',
        '34912917', '35384315', '30331433', '35033657',
        '35236741', '35268571', '35415428', '35350794',
        '35165368', '30488638', '35033654', '32579283',
        '35216228', '35243063', '27044385', '26302614',
        '35410279', '35202738', '35382366', '30238409',
        '35064992', '27068534', '26926445', '27605542',
        '35399987', '35296013', '34893332', '30483667',
        '34923491', '30228394', '35027568', '35280738',
    ]
    next_id = ['26752088', '1292052', '26794435', '25662329', '1291561', '1292722', '26387939', '1291546', '1295644',
               '30166972', '27060077', '1292720', '20495023', '3319755', '3541415', '1652587', '3793023', '1889243',
               '26683290', '1292064', '1292001', '3742360', '27010768', '1292213', '24733428', '1849031', '3011091',
               '4920389', '30170448', '26100958', '25986180', '26861685', '1299398', '1291560', '1295038', '27110296',
               '1291549', '2129039', '1307914', '26580232', '1929463', '1292063', '1291543', '1306249', '30334073',
               '30466931', '24773958', '2131459', '27119724', '26425063']
    # 0 - 20 -200
    # /@href
    comments = ['start----------------------']
    stars = ['start----------------------']
    # for i in id_list:
    for i in tqdm(next_id, desc="爬取中..."):
        if not i in programs:
            try:
                res1, res2 = zip(*auto_request(25, i))
                # print(res1)
                save_excel('tmp.xls', zip(res1, res2))
                # comments += res1
                # stars += res2
            except Exception as e:
                print(repr(e))
                pass
    # print(comments[-1], stars[-1])

    # return zip(comments, stars)


if __name__ == '__main__':
    # url = '111%d'
    # url = format(url % 100)
    # print(url)
    new_catch()
    # do_request('https://movie.douban.com/subject/35070344/comments?start=40&limit=20&status=P&sort=new_score')
