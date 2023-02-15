#!/usr/bin/python
# encoding:utf-8
"""
@author: lance
@version: 1.0.0
@license: Apache Licence
@file: update_dataset_txt_tool.py
@time: 2021/4/15 13:10
"""
from excel_to_txt_tool import save_txt
from pre_data_clean_tool import *


def open_txt(url):
    res = []
    with open(url, 'r', encoding='utf-8') as f:
        for i in f:
            tmp = i.split('\t')
            res.append([tmp[0].strip(), tmp[1].strip()])
    return res


def update_txt(from_url, to_url):
    tmp = open_txt(from_url)
    res = []
    for i in tmp:
        if str_count(i[0]) and i[1] == '2':
            res.append(i)
    print(res)
    print(len(res))
    save_txt(to_url, res)


if __name__ == '__main__':
    # res = open_txt('great.txt')
    # print(res)
    # print(len(res))
    update_txt('great.txt', 'great2.txt')
    pass
