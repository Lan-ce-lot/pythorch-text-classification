#!/usr/bin/python
# encoding:utf-8
"""
@author: lance
@version: 1.0.0
@license: Apache Licence
@file: pre_data_clean_tool.py
@time: 2021/4/9 20:01
"""
import re

import emojiswitch
import xlrd
from xlutils.copy import copy


def filter_emoji(desstr, restr=''):
    # 过滤表情
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)


def str_count(string):
    res = 0
    for s in string:
        # 中文字符范围
        if '\u4e00' <= s <= '\u9fff':
            res += 1
    return 10 <= res <= 100


def open_excel(url):
    wb = xlrd.open_workbook(url)
    sheet = wb.sheets()[0]
    clean_list = []
    con = sheet.nrows
    workbook_1 = copy(wb)
    worksheet_1 = workbook_1.get_sheet(0)
    print(con)
    res = []
    for i in range(0, con):
        com = sheet.row_values(i)[1].strip()
        com = filter_emoji(com)
        star = sheet.row_values(i)[2].strip()
        if 5 <= len(com) and star != '-t' and star != '30' and str_count(com):
            if int(star) < 30:
                star = 2
            else:
                star = 1
            print(com, star)
            res.append([com, star])

    print(res)
    print(con)
    print(len(res))
    save_excel(res, 'clean_' + url)


def save_excel(clean_list, url):
    work = xlrd.open_workbook(url)
    workbook_1 = copy(work)
    worksheet_1 = workbook_1.get_sheet(0)
    for i in range(len(clean_list)):
        worksheet_1.write(i, 1, clean_list[i][0])
        worksheet_1.write(i, 2, clean_list[i][1])
    workbook_1.save(url)


if __name__ == '__main__':
    open_excel('dataset1.xls')
