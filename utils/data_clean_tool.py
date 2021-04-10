#!/usr/bin/python
# encoding:utf-8
"""
@author: lance
@version: 1.0.0
@license: Apache Licence
@file: data_clean_tool.py
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
def open_excel(url):
    wb = xlrd.open_workbook(url)
    sheet = wb.sheets()[0]
    clean_list = []
    con = sheet.nrows
    workbook_1 = copy(wb)
    worksheet_1 = workbook_1.get_sheet(0)
    print(con)
    # for i in range(len(res0)):
    #     worksheet_1.write(i + con, 1, res0[i])
    #     worksheet_1.write(i + con, 2, res1[i])
    # for each_row in range(1, sheet.nrows):  # 循环打印每一行
    #     # print(sheet.row_values(each_row)[1].strip(), sheet.row_values(each_row)[2].strip())
    #     tmp1 = sheet.row_values(each_row)[1].replace('\n', '').strip()
    #     tmp2 = sheet.row_values(each_row)[2].replace('\n', '').strip()
    #     # tmp1 = filter_emoji(tmp1)
    #     # tmp2 = filter_emoji(tmp2)
    #     # tmp1 = emojiswitch.demojize(tmp1, delimiters=("_", "_"), lang="zh")
    #     count_zh = 0
    #     for i in tmp1:
    #         if '\u4e00' <= i <= '\u9fff':
    #             count_zh += 1
    #     if tmp2 != '-t' and count_zh >= 5:
    #         if tmp2 >= '3':
    #             tmp2 = '1'
    #         else:
    #             tmp2 = '2'
    #         print(tmp1, tmp2)
    #         clean_list += [[tmp1, tmp2]]
    #     # print(len(clean_list))
    # print(len(clean_list))
    # # print(clean_list)
    # save_excel(clean_list, 'clean_dataset2.xls')

def save_excel(clean_list, url):

    work = xlrd.open_workbook(url)
    workbook_1 = copy(work)
    worksheet_1 = workbook_1.get_sheet(0)
    for i in range(len(clean_list)):
        worksheet_1.write(i + 1, 1, clean_list[i][0])
        worksheet_1.write(i + 1, 2, clean_list[i][1])
    workbook_1.save(url)

def clean(from_url, to_url):

    work = xlrd.open_workbook(from_url)

    old_sheet = work.sheets()[0]
    con = old_sheet.nrows
    print(old_sheet[1][1])
    print(con)

    # with open('data.txt', "w+") as f:  # 设置文件对象
    #     for i in range(con):
    #         f.write()
    # print('保存{}条'.format())


if __name__ == '__main__':
    # try:
    open_excel('data_set2.xls')
    # except Exception as e:
    #     print(e)

    pass