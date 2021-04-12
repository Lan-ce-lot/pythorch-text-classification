#!/usr/bin/python
# encoding:utf-8
"""
@author: lance
@version: 1.0.0
@license: Apache Licence
@file: random_dataset_tool.py
@time: 2021/4/12 7:46
"""
import random
from visualization_tool import open_txt
from excel_to_txt_tool import save_txt
"""
66000
56000
5000
5000
"""


def random_set():
    res = open_txt('test.txt')
    random.shuffle(res)
    res = res[:66000]
    print(len(res))
    train_set = res[:56000]
    test_set = res[56000:61000]
    dev_set = res[61000:66000]
    save_txt('data\\train_set.txt', train_set)
    save_txt('data\\test_set.txt', test_set)
    save_txt('data\\dev_set.txt', dev_set)


if __name__ == '__main__':
    random_set()
    pass
