#!/usr/bin/python
# encoding:utf-8
"""
@author: lance
@version: 1.0.0
@license: Apache Licence
@file: visualization_tool.py
@time: 2021/4/11 16:44
"""

import matplotlib.pyplot as plt


def open_txt(url):
    res = []
    with open(url, 'r', encoding='utf-8') as f:
        for i in f:
            tmp = i.split('\t\t\t\t')
            res.append([tmp[0].strip(), tmp[1].strip()])
    return res


def draw_bar():
    res = open_txt('2.txt')
    print('总共%d条' % len(res))
    data = [0, 0]
    for i in res:
        if i[1] == '0':
            data[0] += 1
        else:
            data[1] += 1
    plt.style.use('ggplot')
    plt.rcParams['font.sans-serif'] = ['KaiTi']
    labels = ['好评', '差评']
    plt.bar(range(len(data)), data, width=0.3, tick_label=labels)
    plt.title('%d条评论统计' % len(res))
    for a, b in zip(range(len(data)), data):  # 柱子上的数字显示
        plt.text(a, b, '%d' % b, ha='center', va='bottom', fontsize=10)
    plt.show()


if __name__ == '__main__':
    draw_bar()
