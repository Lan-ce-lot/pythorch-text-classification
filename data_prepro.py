from random import sample

import numpy as np
import pandas as pd
import re
from tqdm import tqdm
from collections import Counter
# 数据预处理
def data_processor():


    # def get_labels(str):
    #     return {'体育': 0, '娱乐': 1, '家居': 2, '房产': 3, '教育': 4, '时尚': 5, '时政': 6, '游戏': 7, '科技': 8, '财经': 9}
    #
    # def get_num_labels():
    #     return len(get_labels())
    #
    # def map_label(str):
    #     return get_labels(str.strip())
    #

    mapper={'体育': 0, '娱乐': 1, '家居': 2, '房产': 3, '教育': 4, '时尚': 5, '时政': 6, '游戏': 7, '科技': 8, '财经': 9}

    labels=[]
    texts=[]
    datas = pd.read_csv('cnews/trainLEN500.tsv',sep='\t',error_bad_lines=False)
    datas=datas.values
    # datas=datas[0:1000]
    labels=datas[:,0].tolist()
    texts=datas[:,1].tolist()
    finallabels=[]
    obj = Counter(labels).keys()
    for i in labels:
        finallabels.append(mapper[i])

    print('ending!')
    print(texts)
    return texts,finallabels