#!/usr/bin/python
# encoding:utf-8
"""
@author: lance
@version: 1.0.0
@license: Apache Licence
@file: excel_to_txt_tool.py
@time: 2021/4/11 15:11
"""
import xlrd


def open_excel(url):
    wb = xlrd.open_workbook(url)
    sheet = wb.sheets()[0]
    clean_list = []
    con = sheet.nrows
    print(con)
    res = []
    for i in range(con):
        res.append(
            [sheet.row_values(i)[1].replace('\n', ',').replace('\r', ','), sheet.row_values(i)[2]])
    print(res)
    return res


def save_txt(url):
    tmp = open_excel('clean_dataset1.xls')
    with open(url, 'a', encoding='utf-8') as f:
        for i in tmp:
            f.write(i[0] + '\t\t\t\t')
            f.write(str(int(i[1])) + '\n')
    print('保存{}行'.format(len(tmp)))


if __name__ == '__main__':
    save_txt('1.txt')
    # open_excel('clean_dataset1.xls')
