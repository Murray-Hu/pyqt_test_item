#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 19:14
# @Author  : Murray
# @File    : absolute position.py
# @Software: win10 python3.6.3
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel

class AbsolutePosition(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):

        lb1 = QLabel('Zetcode',self)
        lb1.move(15,10)

        lb2 = QLabel('Tutorials',self)
        lb2.move(35,40)

        lb3 = QLabel('For programmers',self)
        lb3.move(55,70)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Absolute Position')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    abposition = AbsolutePosition()
    sys.exit(app.exec_())
