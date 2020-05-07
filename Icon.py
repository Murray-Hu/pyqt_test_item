#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 22:19
# @Author  : Murray
# @File    : Icon.py
# @Software: win10 python3.6.3

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class Icon(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('hotIcon.png'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon = Icon()
    sys.exit(app.exec_())
