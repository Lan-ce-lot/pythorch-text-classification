# coding: UTF-8


import importlib
from unittest import TestCase


class TestBuildDataset(TestCase):
    def test_build_dataset(self):
        dataset = 'data'  # 数据集
        assert dataset == 'data'
