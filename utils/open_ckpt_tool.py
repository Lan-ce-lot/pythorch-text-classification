#!/usr/bin/python
# encoding:utf-8
"""
@author: lance
@version: 1.0.0
@license: Apache Licence
@file: open_ckpt_tool.py
@time: 2021/4/13 9:41
"""
import torch
from utils import build_dataset, build_iterator, get_time_dif
import time
import torch
import numpy as np
from train_eval import train, init_network
from importlib import import_module

if __name__ == '__main__':
    # 加载
    dataset = 'data'
    # torch.cuda.empty_cache()
    model_name = 'bert'  # bert
    x = import_module('models.' + model_name)
    config = x.Config(dataset)
    model_dict = torch.load('..\\data\\saved_dict\\bert_2021_4_13_cpu.ckpt')
    pass