#!/usr/bin/python
# encoding:utf-8
"""
@author: lance
@version: 1.0.0
@license: Apache Licence
@file: test_tool.py
@time: 2021/4/12 12:57
"""
import numpy as np
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn import metrics
import time

from torch.autograd import Variable

from utils import get_time_dif
from pytorch_pretrained.optimization import BertAdam
if __name__ == '__main__':

    # from sklearn.metrics import accuracy_score
    y_pred = [0, 2, 1, 3, 0]
    y_true = [0, 1, 2, 3, 1]
    print(metrics.accuracy_score(y_true, y_pred))
    pass