#!/usr/bin/python
# encoding:utf-8
"""
@author: lance
@version: 1.0.0
@license: Apache Licence
@file: 1.py
@time: 2021/6/15 2:39
"""
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# yy=[1,2,3,4,5,3,1,2,7,8] #随便创建的数据
# # xx=[3,5,4,1,9,3,2,5,6,3]
# # zz=[2,2,4,7,4,8,2,4,5,6]
# #
# # plt.plot(xx, color='r', linestyle='-', label ="Data 1")
# # plt.plot(yy, color='g', linestyle='--', label ="Data 2")
# # plt.plot(zz, color='b', linestyle=':', label ="Data 3")
# # plt.legend()
# # plt.xlabel("x轴名称", fontproperties="simhei")
# # plt.ylabel("y轴名称", fontproperties="simhei")
# # plt.title("折线图进阶", fontproperties="simhei")
# #
# # plt.show()
# # plt.legend(loc='upper right')#绘制曲线图例，信息来自类型label

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['KaiTi']
month = list(range(100, 1200, 100))
bert = [0.690777659,0.308641165,0.241858676,0.179323852,0.077473082,0.074396998,0.067271106,0.022260299,0.030473961,0.064170562,0.031921085
]
# bert = [0.4922, 0.8750, 0.9062, 0.9219,0.9844,0.9844,0.9844,1.0000,.9922, .9922, .9844]
# BiLSTM = [.3984, .7266, .7969, .8594, .8828,.8750,.9062,.8672,.9141,.8828,.9297]
# money = [5.2, 7.7, 5.8, 5.7,7.3,9.2,18.7,14.6,20.5,17.0,9.8,6.9]
BiLSTM = [
0.700405598,0.561699212,0.456799388,0.338978231,0.24447608,0.266192824,0.269706935,0.277315617,0.226197496,0.274992526,0.241465271

]
plt.style.use('ggplot')
plt.plot(month, bert,  'r-^', label ="BERT")
plt.plot(month, BiLSTM, 'g-o', label ="BiLSTM")
plt.legend()
# plt.xlabel('month',fontsize=14)
plt.ylabel('loss',fontsize=14)
plt.title('BiLSTM和BERT在训练集上的loss对比', fontsize = 18)

plt.show()

if __name__ == '__main__':
    pass