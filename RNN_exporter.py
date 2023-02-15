#!/usr/bin/python
# encoding:utf-8
"""
@author: lance
@version: 1.0.0
@license: Apache Licence
@file: RNN_exporter.py
@time: 2021/6/10 9:40
"""
import logging
import os
import pickle as pkl
from importlib import import_module

import torch

from my_utils import build_iterator

UNK, PAD = '<UNK>', '<PAD>'  # 未知字，padding符号
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
dataset = 'data'
x = import_module('models.TextRNN')
# x = import_module('models.bert')
config = x.Config(dataset, embedding='embedding_SougouNews.npz')
model = x.Model(config)
# map_location = torch.device('cpu')
model.load_state_dict(torch.load('data/saved_dict/TextRNN.ckpt', map_location=torch.device('cpu')))


# model.load_state_dict(torch.load('data/saved_dict/bert.ckpt', map_location=torch.device('cpu')))

def read(s):
    contents = []
    pad_size = 32

    if os.path.exists(config.vocab_path):
        vocab = pkl.load(open(config.vocab_path, 'rb'))
    s = s.strip()
    words_line = []
    tokenizer = lambda x: [y for y in x]  # char-level
    token = tokenizer(s)
    seq_len = len(token)
    if pad_size:
        if len(token) < pad_size:
            token.extend([PAD] * (pad_size - len(token)))
        else:
            token = token[:pad_size]
            seq_len = pad_size
    # word to id
    for word in token:
        words_line.append(vocab.get(word, vocab.get(UNK)))
    contents.append((words_line, 0, seq_len))
    return contents  # [([...], 0), ([...], 1), ...]


def predict(data):
    data_ = build_iterator(data, config)
    for texts, labels in data_:
        outputs = model(texts)
    logging.info(outputs.data)
    logging.info(torch.softmax(outputs.data, dim=1))
    predict_ = torch.max(torch.softmax(outputs.data, dim=1), 1)[1].cpu().numpy()

    # predict_ = torch.max(outputs.data, 1)[1].cpu().numpy()
    return predict_


if __name__ == '__main__':
    while True:
        print("neg" if predict(read(input('请输入'))) else "pos")
