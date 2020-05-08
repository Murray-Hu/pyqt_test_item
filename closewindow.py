#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 18:26
# @Author  : Murray
# @File    : closewindow.py
# @Software: win10 python3.6.3
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtCore import QCoreApplication

class CloseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        btn = QPushButton('close',self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Close Window')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    quitwindow = CloseWindow()
    sys.exit(app.exec_())
