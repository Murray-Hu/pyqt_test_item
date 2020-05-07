#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 21:47
# @Author  : Murray
# @File    : first simple example.py
# @Software: win10 python3.6.3

from PyQt5.QtWidgets import QApplication,QWidget
import sys

class SimpleExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.resize(250,150)
        self.move(300,300)
        self.setWindowTitle('SimpleExample')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = SimpleExample()
    sys.exit(app.exec_())
