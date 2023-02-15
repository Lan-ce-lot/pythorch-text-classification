#!/usr/bin/python
# encoding:utf-8
"""
@author: lance
@version: 1.0.0
@license: Apache Licence
@file: temp_tool.py
@time: 2021/5/18 15:37
"""
import random


def open_txt(url):
    res = []
    with open(url, 'r', encoding='utf-8') as f:
        for i in f:
            tmp = i.split('    ')
            res.append([tmp[0].strip(), tmp[1].strip()])
    return res

def save_txt(url):
    tmp = open_txt("汇总/new_neg.txt")
    with open(url, 'a', encoding='utf-8') as f:
        for i in tmp:
            if i[0] == '1':
                i[0] = '0'
            if i[0] == '-1':
                i[0] = '1'
            f.write(i[1] + '\t\t\t\t')
            f.write(i[0] + '\n')
    print('保存{}行'.format(len(tmp)))

def random_(url):
    res = []
    with open(url, 'r', encoding='utf-8') as f:
        for i in f:
            res.append(i)
    random.shuffle(res)
    # print(res)
    # print(len(res))
    return res
def save(url):
    tmp = random_("汇总/new_neg.txt")
    random.shuffle(tmp)
    with open(url, 'a', encoding='utf-8') as f:
        for i in tmp:
            f.write(i)
    print('保存{}行'.format(len(tmp)))

if __name__ == '__main__':
    # save_txt("汇总/new_neg.txt")
    save("汇总/new.txt")
    pass