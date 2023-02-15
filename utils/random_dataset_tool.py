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

from excel_to_txt_tool import save_txt
from visualization_tool import open_txt

"""
66000
56000
5000
5000
"""


def random_set():
    res = open_txt('汇总/new.txt')
    random.shuffle(res)
    random.shuffle(res)
    length = len(res)
    dev_length = test_length = int(length * 0.1)
    train_length = length - dev_length * 2
    test_set = res[:test_length]
    dev_set = res[test_length:test_length + dev_length]
    train_set = res[test_length + dev_length:]
    save_txt('data\\' + 'data_3\\' + 'train.txt', train_set)
    save_txt('data\\' + 'data_3\\' + 'test.txt', test_set)
    save_txt('data\\' + 'data_3\\' + 'dev.txt', dev_set)


if __name__ == '__main__':
    random_set()
    pass
