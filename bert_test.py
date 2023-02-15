#!/usr/bin/python
# encoding:utf-8
"""
@author: lance
@version: 1.0.0
@license: Apache Licence
@file: bert_test.py
@time: 2021/6/9 20:52
"""
import torch
from importlib import import_module
import models.bert
from utils import build_iterator

PAD, CLS = '[PAD]', '[CLS]'  # padding符号, bert中综合信息符号

dataset = 'data'
x = import_module('models.bert')
config = x.Config(dataset)
model = x.Model(config).to(config.device)
model.load_state_dict(torch.load('data/saved_dict/bert_2021_4_15_cpu.ckpt'))


def read(s):
    pad_size = 32
    contents = []

    token = config.tokenizer.tokenize(s.strip())
    token = [CLS] + token
    seq_len = len(token)
    mask = []
    token_ids = config.tokenizer.convert_tokens_to_ids(token)

    if pad_size:
        if len(token) < pad_size:
            mask = [1] * len(token_ids) + [0] * (pad_size - len(token))
            token_ids += ([0] * (pad_size - len(token)))
        else:
            mask = [1] * pad_size
            token_ids = token_ids[:pad_size]
            seq_len = pad_size
    contents.append((token_ids, 0, seq_len, mask))
    return contents


def predict(data):
    data_ = build_iterator(data, config)
    for texts, labels in data_:
        outputs = model(texts)
    predict_ = torch.max(outputs.data, 1)[1].cpu().numpy()
    return predict_


if __name__ == '__main__':
    while True:
        print("neg" if predict(read(input())) else "pos")
