# coding: UTF-8
# !/usr/bin/python
# encoding:utf-8
"""
@author: lance
@version: 1.0.0
@license: Apache Licence
@file: UI.py
@time: 2021/6/12 21:01
"""
import os
import sys

import qtawesome
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class MainUi(QtWidgets.QMainWindow):
    model_id = 0

    def __init__(self):
        super().__init__()
        self.clearbutton = QtWidgets.QPushButton(
            # qtawesome.icon('mdi.delete-outline', color='white'),
            "清空")
        self.submit = QtWidgets.QPushButton(qtawesome.icon('fa.check', color='white'), "提交")
        self.gender_combo = QComboBox()
        self.gender_label = QLabel('模型选择')
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.right_bar_layout = QtWidgets.QGridLayout()  # 聊天输入框网格布局
        self.right_bar_widget = QtWidgets.QTextEdit()  # 聊天输入框
        self.search_icon = QtWidgets.QLabel(chr(0xf011) + ' ' + ' HCS的情感分析器')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.left_img = QLabel()
        self.left_text = QLabel()
        self.setWindowTitle('HCS的情感分析器')
        self.init_ui()

    def slot_max_or_recv(self):  # 最大化
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def submited(self):  # 发送键
        self.model_id = self.gender_combo.currentIndex()
        s = self.right_bar_widget.toPlainText()
        print('输入:', s)
        print('TextRNN' if self.model_id else 'bert')
        self.reply(s)

    def clc(self):  # 清除键
        self.right_bar_widget.clear()

    def keyPressEvent(self, event):
        if str(event.key()) == '16777220':  # 回车
            print("按下回车")
            self.submited()

    def reply(self, s):  # 回复
        if self.model_id == 0:
            from RNN_test import read, predict
        else:
            from bert_test import read, predict
        _prdeict = predict(read(s))[0]
        print(_prdeict)
        if _prdeict == 0:
            self.left_img.setPixmap(QPixmap('img/smile_1.jpg').scaled(240, 240))
            self.left_text.setText(u"  积极")
        else:
            self.left_img.setPixmap(QPixmap('img/angry.jpg').scaled(240, 240))
            self.left_text.setText(u"  消极")

    def init_ui(self):
        self.setFixedSize(600, 300)
        self.main_widget.setLayout(self.main_layout)
        # 左
        self.left_widget.setObjectName('left_widget')
        self.left_widget.setLayout(self.left_layout)
        self.main_layout.addWidget(self.left_widget, 0, 0, 10, 4)
        # 左上
        self.left_close.clicked.connect(self.close)
        self.left_visit.clicked.connect(self.slot_max_or_recv)
        self.left_mini.clicked.connect(self.showMinimized)
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        # 左中(图片)
        self.left_img.setPixmap(QPixmap('img/smile_1.jpg').scaled(240, 240))
        self.left_layout.addWidget(self.left_img, 2, 0, 3, 3)
        # 左下text
        self.left_text.setText(u"输入句子试试")
        self.left_layout.addWidget(self.left_text, 5, 1, 1, 1)
        # 右
        self.right_widget.setObjectName('right_widget')
        self.right_widget.setLayout(self.right_layout)
        self.main_layout.addWidget(self.right_widget, 0, 4, 10, 6)
        self.setCentralWidget(self.main_widget)
        # 右上
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right_layout.addWidget(self.search_icon, 0, 0, 1, 2)
        # 右中上
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.right_layout.addWidget(self.right_bar_widget, 1, 0, 1, 5)
        # 右中下
        self.gender_combo.addItems(['bert', 'BiLSTM'])
        self.right_layout.addWidget(self.gender_label, 2, 0, 1, 2)
        self.right_layout.addWidget(self.gender_combo, 2, 3, 1, 2)
        # 右下
        self.submit.setObjectName('left_button')
        self.submit.clicked.connect(self.submited)
        self.right_layout.addWidget(self.submit, 3, 0, 1, 1)
        self.clearbutton.setObjectName('left_button')
        self.clearbutton.clicked.connect(self.clc)
        self.right_layout.addWidget(self.clearbutton, 3, 3, 1, 1)
        # Style
        self.left_close.setStyleSheet(
            '''
            QPushButton{
                background:#F76677;border-radius:5px;
            }
            QPushButton:hover{
                background:red;
            }
            ''')
        self.left_visit.setStyleSheet(
            '''
            QPushButton{
            background:#F7D674;border-radius:5px;
            }
            QPushButton:hover{
            background:yellow;
            }
            ''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}
            QPushButton:hover{background:green;}''')
        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QLabel{font-size:20px;}
            QWidget#left_widget{
                background:#148ecf;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;}''')
        self.right_widget.setStyleSheet('''
            QLabel{font-size:12px;}
            QPushButton{font-size:12px;}
            QComboBox{font-size:12px;}
            QTextEdit{font-size:12px;}
            QWidget#right_widget{
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;}''')
        self.main_layout.setSpacing(0)


def main():
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # qt分辨率自适应

    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    os.system("pause")
